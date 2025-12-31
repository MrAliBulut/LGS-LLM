"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { ExamConfigurator } from "@/components/exam-configurator"
import { ExamWorkspace } from "@/components/exam-workspace"
import { BookOpen, Sparkles } from "lucide-react"

export default function Home() {
  const [showConfigurator, setShowConfigurator] = useState(false)
  const [examStarted, setExamStarted] = useState(false)
  const [examConfig, setExamConfig] = useState<any>(null)

  const handleQuickStart = () => {
    // Quick start with balanced distribution
    const generalDistribution = {
      "Friendship": 1,
      "Teen Life": 1,
      "In The Kitchen": 1,
      "On The Phone": 1,
      "The Internet": 1,
      "Adventures": 1,
      "Tourism": 1,
      "Chores": 1,
      "Science": 1,
      "Natural Forces": 1,
    }

    setExamConfig({
      distribution: generalDistribution,
      visualCount: 0,
      isRandom: false,
    })
    setExamStarted(true)
  }

  const handleCustomStart = (config: any) => {
    setExamConfig(config)
    setExamStarted(true)
  }

  if (examStarted && examConfig) {
    return <ExamWorkspace config={examConfig} onBack={() => setExamStarted(false)} />
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-background via-primary/5 to-accent/10">
      <div className="container mx-auto px-4 py-16">
        <div className="flex flex-col items-center justify-center min-h-[80vh]">
          {/* Header */}
          <div className="text-center mb-12 animate-fade-in">
            <div className="inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-primary/10 to-accent/20 rounded-full mb-6 border border-primary/20">
              <Sparkles className="w-4 h-4 text-primary" />
              <span className="text-sm font-semibold text-primary">Yapay Zeka Destekli</span>
            </div>
            <h1 className="text-4xl md:text-6xl font-bold mb-4 text-balance bg-gradient-to-br from-foreground to-foreground/70 bg-clip-text">
              LGS Sınav Oluşturucu
            </h1>
            <p className="text-lg md:text-xl text-muted-foreground max-w-2xl mx-auto text-pretty leading-relaxed">
              10 soruluk genel LGS denemesi için hazır mısınız? Hemen başlayın.
            </p>
          </div>

          {/* Main Action */}
          <div className="w-full max-w-md space-y-6 animate-fade-in-up">
            <Button
              size="lg"
              className="w-full h-14 text-lg font-semibold shadow-lg hover:shadow-xl transition-all bg-gradient-to-r from-primary to-primary/90 hover:from-primary/90 hover:to-primary"
              onClick={handleQuickStart}
            >
              <BookOpen className="w-5 h-5 mr-2" />
              Sınav Oluştur
            </Button>

            {/* Expand Configurator */}
            <button
              onClick={() => setShowConfigurator(!showConfigurator)}
              className="w-full text-sm text-muted-foreground hover:text-foreground transition-colors flex items-center justify-center gap-2 group"
            >
              <span>Konular ve Görselleri Özelleştir</span>
              <svg
                className={`w-4 h-4 transition-transform ${showConfigurator ? "rotate-180" : ""}`}
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
              </svg>
            </button>

            {/* Configurator Panel */}
            {showConfigurator && (
              <div className="animate-fade-in-up">
                <ExamConfigurator onStart={handleCustomStart} />
              </div>
            )}
          </div>

          {/* Features */}
          <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-4xl">
            {[
              {
                title: "Konu Seçimi",
                description: "10 üniteden istediğiniz dağılımı seçin",
              },
              {
                title: "Görselli Sorular",
                description: "Görselli soru sayısını belirleyin",
              },
              {
                title: "Canlı Önizleme",
                description: "Sorular hazır olduğunda anında görün",
              },
            ].map((feature, index) => (
              <div
                key={index}
                className="p-6 rounded-xl bg-card border-2 border-border hover:border-primary/50 hover:shadow-md transition-all"
              >
                <h3 className="font-semibold mb-2 text-foreground">{feature.title}</h3>
                <p className="text-sm text-muted-foreground leading-relaxed">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}
