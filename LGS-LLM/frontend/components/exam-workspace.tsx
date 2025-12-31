"use client"

import { useState, useEffect } from "react"
import { Button } from "@/components/ui/button"
import { QuestionCard } from "@/components/question-card"
import { Progress } from "@/components/ui/progress"
import { ArrowLeft, Download, Loader2 } from "lucide-react"
import { Badge } from "@/components/ui/badge"
import jsPDF from "jspdf"

interface ExamWorkspaceProps {
  config: any
  onBack: () => void
}

export function ExamWorkspace({ config, onBack }: ExamWorkspaceProps) {
  const [questions, setQuestions] = useState<any[]>([])
  const [loading, setLoading] = useState(true)
  const [loadingCount, setLoadingCount] = useState(0)

  const totalQuestions = Object.values(config.distribution).reduce((sum: number, val: any) => sum + val, 0)

  useEffect(() => {
    loadQuestionsFromAPI()
  }, [config.distribution, config.visualCount])

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

  const handleDownloadPDF = () => {
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

      // Soru metni
      doc.setFontSize(10)
      doc.setFont("helvetica", "normal")
      const questionLines = doc.splitTextToSize(question.question, pageWidth - margin * 2)
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
      question.options.forEach((option: any) => {
        if (yPosition > pageHeight - 20) {
          doc.addPage()
          yPosition = margin
        }

        const optionText = `${option.label}) ${option.text}`
        const optionLines = doc.splitTextToSize(optionText, pageWidth - margin * 2 - 5)
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

      const dogruCevap = question.options.find((opt: any) => opt.isCorrect)
      doc.text(`${index + 1}. ${dogruCevap?.label || "-"}`, margin, yPosition)
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
              <Button
                onClick={handleDownloadPDF}
                variant="default"
                size="sm"
                className="bg-gradient-to-r from-primary to-primary/90 shadow-md"
              >
                <Download className="w-4 h-4 mr-2" />
                PDF İndir
              </Button>
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

        {/* Questions */}
        <div className="space-y-6 max-w-4xl mx-auto">
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
