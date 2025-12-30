"use client"

import { useState, useEffect } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { Slider } from "@/components/ui/slider"
import { Badge } from "@/components/ui/badge"
import { Shuffle, AlertCircle } from "lucide-react"
import { Alert, AlertDescription } from "@/components/ui/alert"

const TOPICS = [
  "Arkadaşlık (Ünite 1)",
  "Ergenlik (Ünite 2)",
  "Bilim (Ünite 3)",
  "Teknoloji (Ünite 4)",
  "Spor (Ünite 5)",
  "Sağlık (Ünite 6)",
  "Doğa (Ünite 7)",
  "Sanat (Ünite 8)",
  "Tarih (Ünite 9)",
  "Kültür (Ünite 10)",
]

interface ExamConfiguratorProps {
  onStart: (config: any) => void
}

export function ExamConfigurator({ onStart }: ExamConfiguratorProps) {
  const [distribution, setDistribution] = useState<Record<string, number>>({})
  const [visualCount, setVisualCount] = useState(0)
  const [isRandom, setIsRandom] = useState(false)

  const totalQuestions = Object.values(distribution).reduce((sum, val) => sum + val, 0)
  const remainingQuestions = 10 - totalQuestions
  const estimatedTime = visualCount * 2

  useEffect(() => {
    if (isRandom) {
      randomizeDistribution()
    }
  }, [isRandom])

  const randomizeDistribution = () => {
    const newDist: Record<string, number> = {}
    let remaining = 10

    TOPICS.forEach((topic, index) => {
      if (index === TOPICS.length - 1) {
        newDist[topic] = remaining
      } else {
        const max = Math.min(remaining, 4)
        const count = Math.floor(Math.random() * (max + 1))
        newDist[topic] = count
        remaining -= count
      }
    })

    setDistribution(newDist)
  }

  const handleDistributionChange = (topic: string, value: number) => {
    const newDist = { ...distribution }
    const currentValue = newDist[topic] || 0
    const diff = value - currentValue

    if (totalQuestions + diff <= 10) {
      newDist[topic] = value
      setDistribution(newDist)
    }
  }

  const handleStart = () => {
    if (totalQuestions === 0) {
      randomizeDistribution()
      return
    }

    onStart({
      distribution,
      visualCount,
      isRandom,
    })
  }

  return (
    <Card className="w-full shadow-lg border-2">
      <CardHeader className="bg-gradient-to-r from-primary/5 to-accent/10">
        <CardTitle className="flex items-center justify-between">
          <span className="text-foreground">Sınav Yapılandırması</span>
          <Button
            variant={isRandom ? "default" : "outline"}
            size="sm"
            onClick={() => setIsRandom(!isRandom)}
            className={isRandom ? "bg-gradient-to-r from-primary to-primary/90" : ""}
          >
            <Shuffle className="w-4 h-4 mr-2" />
            Rastgele
          </Button>
        </CardTitle>
      </CardHeader>
      <CardContent className="space-y-6">
        {/* Question Distribution */}
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <Label className="text-base font-semibold">Konu Dağılımı</Label>
            <Badge variant={remainingQuestions === 0 ? "default" : "secondary"} className="font-medium">
              {remainingQuestions === 0 ? "✓ Tamamlandı" : `${remainingQuestions} soru kaldı`}
            </Badge>
          </div>

          <div className="space-y-3 max-h-[300px] overflow-y-auto pr-2">
            {TOPICS.map((topic) => (
              <div key={topic} className="space-y-2">
                <div className="flex items-center justify-between text-sm">
                  <span className="text-muted-foreground">{topic}</span>
                  <span className="font-medium">{distribution[topic] || 0} soru</span>
                </div>
                <Slider
                  value={[distribution[topic] || 0]}
                  onValueChange={([value]) => handleDistributionChange(topic, value)}
                  max={Math.min(10 - totalQuestions + (distribution[topic] || 0), 10)}
                  step={1}
                  disabled={isRandom}
                  className="w-full"
                />
              </div>
            ))}
          </div>
        </div>

        {/* Visual Questions */}
        <div className="space-y-4">
          <Label className="text-base font-semibold">Görselli Soru Sayısı</Label>
          <div className="flex items-center gap-4">
            <Slider
              value={[visualCount]}
              onValueChange={([value]) => setVisualCount(value)}
              max={Math.min(totalQuestions || 10, 10)}
              step={1}
              className="flex-1"
            />
            <span className="font-medium w-12 text-right">{visualCount}</span>
          </div>

          {visualCount > 0 && (
            <Alert className="border-primary/30 bg-primary/5">
              <AlertCircle className="h-4 w-4 text-primary" />
              <AlertDescription className="text-foreground">
                Tahmini bekleme süresi: <strong className="text-primary">{estimatedTime} dakika</strong>
                <br />
                <span className="text-sm text-muted-foreground">Her görselli soru yaklaşık 2 dakika sürer</span>
              </AlertDescription>
            </Alert>
          )}
        </div>

        {/* Start Button */}
        <Button
          onClick={handleStart}
          className="w-full bg-gradient-to-r from-primary to-primary/90 hover:from-primary/90 hover:to-primary shadow-md hover:shadow-lg transition-all"
          size="lg"
        >
          {totalQuestions === 0 ? "Rastgele Oluştur ve Başlat" : "Sınavı Başlat"}
        </Button>
      </CardContent>
    </Card>
  )
}
