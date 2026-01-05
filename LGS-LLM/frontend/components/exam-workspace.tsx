"use client"

import { useState, useEffect, useRef } from "react"
import { Button } from "@/components/ui/button"
import { QuestionCard } from "@/components/question-card"
import { Progress } from "@/components/ui/progress"
import { ArrowLeft, Download, Loader2, Image, FileText } from "lucide-react"
import { Badge } from "@/components/ui/badge"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import jsPDF from "jspdf"

interface ExamWorkspaceProps {
  config: any
  onBack: () => void
}

export function ExamWorkspace({ config, onBack }: ExamWorkspaceProps) {
  const [questions, setQuestions] = useState<any[]>([])
  const [loading, setLoading] = useState(true)
  const [loadingCount, setLoadingCount] = useState(0)
  const [generatingPdf, setGeneratingPdf] = useState(false)
  const hasFetchedRef = useRef(false)
  const examContainerRef = useRef<HTMLDivElement>(null)

  const totalQuestions = Object.values(config.distribution).reduce((sum: number, val: any) => sum + val, 0)

  useEffect(() => {
    // Prevent duplicate API calls (React StrictMode, re-renders, etc.)
    if (hasFetchedRef.current) return
    hasFetchedRef.current = true
    
    loadQuestionsFromAPI()
  }, [])

  const loadQuestionsFromAPI = async () => {
    try {
      const response = await fetch("http://localhost:8000/generate-exam", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          distribution: config.distribution,
          visualCount: config.visualCount,
        }),
      })

      const reader = response.body?.getReader()
      const decoder = new TextDecoder()
      let buffer = ""

      if (!reader) return

      setLoading(false)

      while (true) {
        const { done, value } = await reader.read()

        if (done) {
          // Process any remaining data in buffer at the end of stream
          if (buffer.trim()) {
            try {
              const question = JSON.parse(buffer)
              console.log("[DEBUG] Soru alındı (end of stream):", question.id)
              setQuestions((prev) => {
                const newQuestions = [...prev, question]
                return newQuestions.sort((a, b) => {
                  const aIndex = Number.parseInt(a.id.substring(1))
                  const bIndex = Number.parseInt(b.id.substring(1))
                  return aIndex - bIndex
                })
              })
              setLoadingCount((prev) => prev + 1)
            } catch (e) {
              console.error("[DEBUG] JSON parse error (end):", e, buffer)
            }
          }
          break
        }

        buffer += decoder.decode(value, { stream: true })
        const lines = buffer.split("\n")

        // Keep last line in buffer (might be incomplete)
        buffer = lines.pop() || ""

        // Process complete lines
        for (const line of lines) {
          if (line.trim()) {
            try {
              const question = JSON.parse(line)
              console.log("[DEBUG] Soru alındı:", question.id, question.topic)
              setQuestions((prev) => {
                const newQuestions = [...prev, question]
                return newQuestions.sort((a, b) => {
                  const aIndex = Number.parseInt(a.id.substring(1))
                  const bIndex = Number.parseInt(b.id.substring(1))
                  return aIndex - bIndex
                })
              })
              setLoadingCount((prev) => prev + 1)
            } catch (e) {
              console.error("[DEBUG] JSON parse hatası:", e)
            }
          }
        }
      }
    } catch (error) {
      console.error("[v0] API hatası:", error)
    }
  }

const handleDownloadPDFWithImages = async () => {
    if (!examContainerRef.current) {
      console.error("[DEBUG] examContainerRef is null")
      return
    }

    setGeneratingPdf(true)
    console.log("[DEBUG] Starting PDF with images generation...")

    try {
      const domtoimage = (await import("dom-to-image-more")).default

      const container = examContainerRef.current
      
      // Use getBoundingClientRect for accurate dimensions
      const rect = container.getBoundingClientRect()
      const domWidth = rect.width
      const domHeight = rect.height
      
      console.log("[DEBUG] Container size:", domWidth, "x", domHeight)
      
      // Save original styles to restore later
      const originalStyle = container.style.cssText
      const originalClass = container.className
      
      // Temporarily neutralize container styling for accurate capture
      container.style.cssText = `
        width: ${domWidth}px !important;
        max-width: none !important;
        margin: 0 !important;
        padding: 16px !important;
        transform: none !important;
        box-sizing: border-box !important;
        background-color: #ffffff !important;
      `
      
      const scale = 2 // High resolution render
      
      console.log("[DEBUG] Capturing image with dom-to-image...")
      
      const imgData = await domtoimage.toPng(container, {
        quality: 1,
        bgcolor: "#ffffff",
        width: domWidth * scale,
        height: domHeight * scale,
        style: {
          transform: `scale(${scale})`,
          transformOrigin: "top left",
          width: `${domWidth}px`,
          height: `${domHeight}px`,
        },
      })
      
      // Restore original styles
      container.style.cssText = originalStyle
      container.className = originalClass
      
      console.log("[DEBUG] Image captured successfully")
      
      // Load image to get dimensions
      const img = document.createElement("img")
      img.src = imgData
      await new Promise<void>((resolve) => { img.onload = () => resolve() })
      
      // A4 dimensions in mm: 210 x 297
      const a4Width = 210
      const a4Height = 297
      const margin = 10
      const printableWidth = a4Width - margin * 2
      
      // Calculate the height in mm that the image will occupy at full width
      const imgAspectRatio = (domHeight * scale) / (domWidth * scale)
      const totalImageHeightMm = printableWidth * imgAspectRatio
      
      console.log("[DEBUG] Image will be", printableWidth, "x", totalImageHeightMm.toFixed(1), "mm")
      
      // Create PDF - first page(s) will be custom height to fit content without cutting
      // We'll use A4 width but custom height for exam pages
      const examPageHeight = Math.min(totalImageHeightMm + margin * 2, 3000) // Max 3000mm per page
      
      // If content fits on one page (with some buffer), use that
      // Otherwise, create a tall page that fits everything
      const doc = new jsPDF({
        orientation: "portrait",
        unit: "mm",
        format: [a4Width, examPageHeight]
      })
      
      // Add the entire exam image on the first page (no slicing!)
      doc.addImage(
        imgData,
        "PNG",
        margin,
        margin,
        printableWidth,
        totalImageHeightMm
      )
      
      console.log("[DEBUG] Added exam content - single page, no cuts!")
      
      // Answer Key Page - add as standard A4
      console.log("[DEBUG] Adding answer key page...")
      doc.addPage([a4Width, a4Height])
      
      let y = margin + 20
      const pageHeight = a4Height
      const pageWidth = a4Width
      
      doc.setFont("helvetica", "bold")
      doc.setFontSize(18)
      doc.text("Cevap Anahtari", pageWidth / 2, y, { align: "center" })
      
      y += 20
      
      doc.setFont("helvetica", "normal")
      doc.setFontSize(12)
      
      questions.forEach((q, index) => {
        if (y > pageHeight - 20) {
          doc.addPage()
          y = margin + 20
        }
        
        const answer = q.answer ?? q.correctAnswer ?? q.question?.answer ?? "-"
        doc.text(`${index + 1}. ${answer}`, margin, y)
        y += 10
      })
      
      doc.save(`LGS_Sinav_Gorselli_${Date.now()}.pdf`)
  } catch (error) {
    console.error("[DEBUG] PDF Error:", error);
  } finally {
    setGeneratingPdf(false);
  }
};


  // PDF without images (text-based)
  const handleDownloadPDFTextOnly = () => {
    const doc = new jsPDF()
    const pageWidth = doc.internal.pageSize.getWidth()
    const pageHeight = doc.internal.pageSize.getHeight()
    const margin = 20
    const lineHeight = 7
    let yPosition = margin

    // Başlık
    doc.setFontSize(18)
    doc.setFont("helvetica", "bold")
    doc.text("LGS Deneme Sinavi", pageWidth / 2, yPosition, { align: "center" })
    yPosition += lineHeight * 2

    // Tarih
    doc.setFontSize(10)
    doc.setFont("helvetica", "normal")
    const tarih = new Date().toLocaleDateString("tr-TR")
    doc.text(`Tarih: ${tarih}`, pageWidth / 2, yPosition, { align: "center" })
    yPosition += lineHeight * 2

    // Sorular
    questions.forEach((question, index) => {
      // Sayfa sonu kontrolü
      if (yPosition > pageHeight - 40) {
        doc.addPage()
        yPosition = margin
      }

      // Soru numarası ve konusu
      doc.setFontSize(11)
      doc.setFont("helvetica", "bold")
      doc.text(`Soru ${index + 1} - ${question.topic}`, margin, yPosition)
      yPosition += lineHeight

      // Soru metni - extract from nested structure
      doc.setFontSize(10)
      doc.setFont("helvetica", "normal")
      
      // Get the actual question data (handle nested structure)
      const questionData = question.question || question
      const passage = questionData.passage || ""
      const stem = questionData.stem || questionData.text || ""
      const questionText = passage ? `${passage}\n\n${stem}` : stem
      
      const questionLines = doc.splitTextToSize(questionText || "[Soru metni bulunamadi]", pageWidth - margin * 2)
      doc.text(questionLines, margin, yPosition)
      yPosition += questionLines.length * lineHeight

      // Görselli soru uyarısı
      if (question.hasImage) {
        yPosition += lineHeight * 0.5
        doc.setFontSize(9)
        doc.setTextColor(100, 100, 100)
        doc.text("[Gorselli Soru]", margin, yPosition)
        doc.setTextColor(0, 0, 0)
        yPosition += lineHeight
      }

      // Şıklar
      yPosition += lineHeight * 0.5
      
      // Get options from nested structure
      const rawOptions = questionData.options || question.options || {}
      
      // Handle both array and object formats for options
      const optionsArray = Array.isArray(rawOptions) 
        ? rawOptions 
        : Object.entries(rawOptions).map(([key, value]) => ({ label: key, text: value }))
      
      optionsArray.forEach((option: any) => {
        if (yPosition > pageHeight - 20) {
          doc.addPage()
          yPosition = margin
        }

        const optionLabel = option.label || option.key || ''
        const optionText = option.text || option.value || option || ''
        const fullOptionText = `${optionLabel}) ${optionText}`
        const optionLines = doc.splitTextToSize(fullOptionText, pageWidth - margin * 2 - 5)
        doc.text(optionLines, margin + 5, yPosition)
        yPosition += optionLines.length * lineHeight
      })

      yPosition += lineHeight

      // Cevap anahtarı için yer
      if (yPosition > pageHeight - 30) {
        doc.addPage()
        yPosition = margin
      }
    })

    // Yeni sayfa - Cevap Anahtarı
    doc.addPage()
    yPosition = margin

    doc.setFontSize(14)
    doc.setFont("helvetica", "bold")
    doc.text("Cevap Anahtari", pageWidth / 2, yPosition, { align: "center" })
    yPosition += lineHeight * 2

    doc.setFontSize(10)
    doc.setFont("helvetica", "normal")

    questions.forEach((question, index) => {
      if (yPosition > pageHeight - 20) {
        doc.addPage()
        yPosition = margin
      }

      // Get correct answer - could be question.answer, question.correctAnswer, or question.question.answer
      const correctAnswer = question.answer || question.correctAnswer || question.question?.answer || "-"
      doc.text(`${index + 1}. ${correctAnswer}`, margin, yPosition)
      yPosition += lineHeight
    })

    // PDF'i indir
    doc.save(`LGS_Sinav_${new Date().getTime()}.pdf`)
  }

  const progress = Math.min((loadingCount / totalQuestions) * 100, 100)
  const allQuestionsLoaded = loadingCount === totalQuestions

  return (
    <div className="min-h-screen bg-gradient-to-br from-background via-primary/5 to-accent/10">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="flex items-center justify-between mb-8">
          <Button variant="ghost" onClick={onBack} className="hover:bg-primary/10">
            <ArrowLeft className="w-4 h-4 mr-2" />
            Geri
          </Button>

          <div className="flex items-center gap-4">
            <Badge variant="outline" className="text-sm font-medium border-2 px-3 py-1.5">
              {Math.min(loadingCount, totalQuestions)} / {totalQuestions} Soru Yüklendi
            </Badge>
            {allQuestionsLoaded && (
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <Button
                    variant="default"
                    size="sm"
                    className="bg-gradient-to-r from-primary to-primary/90 shadow-md"
                    disabled={generatingPdf}
                  >
                    {generatingPdf ? (
                      <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                    ) : (
                      <Download className="w-4 h-4 mr-2" />
                    )}
                    {generatingPdf ? "Oluşturuluyor..." : "PDF İndir"}
                  </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent align="end">
                  <DropdownMenuItem onClick={handleDownloadPDFWithImages} className="cursor-pointer">
                    <Image className="w-4 h-4 mr-2" />
                    Görseller ile
                  </DropdownMenuItem>
                  <DropdownMenuItem onClick={handleDownloadPDFTextOnly} className="cursor-pointer">
                    <FileText className="w-4 h-4 mr-2" />
                    Görseller olmadan
                  </DropdownMenuItem>
                </DropdownMenuContent>
              </DropdownMenu>
            )}
          </div>
        </div>

        {/* Progress */}
        {!allQuestionsLoaded && (
          <div className="mb-8 space-y-2">
            <div className="flex items-center justify-between text-sm">
              <span className="text-muted-foreground">Sorular oluşturuluyor...</span>
              <span className="font-medium">{Math.round(progress)}%</span>
            </div>
            <Progress value={progress} className="h-2.5" />
          </div>
        )}

        {/* Questions - wrapper handles centering, container is neutral for PDF capture */}
        <div className="flex justify-center">
        <div ref={examContainerRef} className="space-y-6 w-full max-w-4xl bg-white p-4 rounded-xl">
          {Array.from({ length: totalQuestions }).map((_, index) => {
            const question = questions.find((q) => q.id === `q${index + 1}`)

            if (question) {
              return <QuestionCard key={question.id} question={question} index={index} />
            }

            return (
              <div
                key={`loading-${index}`}
                className="bg-card border-2 border-dashed border-border rounded-xl p-8 animate-pulse"
              >
                <div className="flex items-center justify-center py-12">
                  <Loader2 className="w-8 h-8 animate-spin text-primary" />
                  <span className="ml-3 text-muted-foreground font-medium">Soru {index + 1} hazırlanıyor...</span>
                </div>
              </div>
            )
          })}
        </div>
        </div>

        {/* Success Message */}
        {allQuestionsLoaded && (
          <div className="mt-8 p-6 bg-gradient-to-r from-primary/10 to-accent/20 border-2 border-primary/30 rounded-xl text-center max-w-4xl mx-auto shadow-md">
            <h3 className="text-lg font-semibold text-primary mb-2">✓ Tüm Sorular Hazır!</h3>
            <p className="text-sm text-muted-foreground">
              Sınavınız başarıyla oluşturuldu. İnceleyebilir veya PDF olarak indirebilirsiniz.
            </p>
          </div>
        )}
      </div>
    </div>
  )
}
