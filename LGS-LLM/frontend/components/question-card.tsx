"use client"

import { Card, CardContent, CardHeader } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Eye, EyeOff, Loader2, Check, X } from "lucide-react"
import { useState } from "react"
import Image from "next/image"

interface QuestionCardProps {
  question: any
  index: number
}

export function QuestionCard({ question, index }: QuestionCardProps) {
  const [showAnswer, setShowAnswer] = useState(false)
  const [imageLoading, setImageLoading] = useState(true)
  const [selectedAnswer, setSelectedAnswer] = useState<string | null>(null)

  // Handle both old format and LLM format
  const questionData = question.question || question
  const isLLMFormat = questionData.stem !== undefined
  
  const stemText = isLLMFormat ? questionData.stem : (question.question || "")
  const passageText = isLLMFormat ? questionData.passage : ""
  const optionsObj = isLLMFormat ? questionData.options : null
  const correctAnswer = isLLMFormat ? questionData.answer : question.correctAnswer
  
  // Convert options object to array format for display
  const optionsArray = optionsObj 
    ? Object.entries(optionsObj).map(([key, val]) => `${key}) ${val}`)
    : (question.options || [])
  
  const explanationText = isLLMFormat 
    ? Object.entries(question.distractor_logic || {})
        .map(([key, val]) => `${key}: ${val}`)
        .join("\n")
    : (question.explanation || "")

  const isCorrect = selectedAnswer && selectedAnswer.startsWith(correctAnswer)

  return (
    <Card className="overflow-hidden animate-fade-in-up shadow-sm hover:shadow-md transition-shadow flex flex-col">
      <CardHeader className="bg-gradient-to-r from-primary/5 to-accent/10 border-b">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Badge variant="outline" className="font-mono">
              Soru {index + 1}
            </Badge>
            <span className="text-sm text-muted-foreground">{question.topic || question.unit}</span>
          </div>
          <div className="flex items-center gap-2">
            {question.hasImage && <Badge variant="secondary">Görselli</Badge>}
            {selectedAnswer && (
              <Badge variant={isCorrect ? "default" : "destructive"} className="animate-fade-in">
                {isCorrect ? (
                  <>
                    <Check className="w-3 h-3 mr-1" />
                    Doğru
                  </>
                ) : (
                  <>
                    <X className="w-3 h-3 mr-1" />
                    Yanlış
                  </>
                )}
              </Badge>
            )}
          </div>
        </div>
      </CardHeader>
      <CardContent className={`space-y-4 flex flex-col flex-grow ${question.hasImage ? "p-4" : "p-6"}`}>
        {/* Image */}
        {question.hasImage && question.imageUrl && (
          <div className="relative w-full h-96 bg-gradient-to-br from-muted to-accent/20 rounded-xl overflow-hidden border border-border flex-shrink-0">
            {imageLoading && (
              <div className="absolute inset-0 flex items-center justify-center bg-muted/80 backdrop-blur-sm z-10">
                <div className="text-center space-y-3">
                  <Loader2 className="w-8 h-8 animate-spin text-primary mx-auto" />
                  <p className="text-sm text-muted-foreground">Görsel yükleniyor...</p>
                </div>
              </div>
            )}
            <Image
              src={question.imageUrl || "/placeholder.svg"}
              alt="Soru görseli"
              fill
              className="object-contain"
              onLoad={() => setImageLoading(false)}
            />
          </div>
        )}

        {/* Question Text */}
        <div className="prose prose-sm max-w-none space-y-3">
          {passageText && (
            <div className="p-3 bg-accent/10 border border-accent/30 rounded-lg italic text-sm text-muted-foreground">
              "{passageText}"
            </div>
          )}
          <p className="text-foreground leading-relaxed font-medium">{stemText}</p>
        </div>

        {/* Options */}
        <div className="space-y-2.5">
          {optionsArray.map((option: string, idx: number) => {
            const isSelected = selectedAnswer === option
            const isCorrectOption = option.startsWith(correctAnswer)
            const showCorrect = selectedAnswer && isCorrectOption
            const showIncorrect = isSelected && !isCorrectOption

            return (
              <button
                key={idx}
                onClick={() => setSelectedAnswer(option)}
                disabled={!!selectedAnswer}
                className={`w-full p-3.5 rounded-xl border-2 transition-all text-left ${
                  showCorrect
                    ? "border-primary bg-primary/10 shadow-sm"
                    : showIncorrect
                      ? "border-destructive bg-destructive/10"
                      : isSelected
                        ? "border-primary bg-primary/5"
                        : "border-border bg-card hover:bg-accent/50 hover:border-accent"
                } ${selectedAnswer ? "cursor-not-allowed" : "cursor-pointer"}`}
              >
                <div className="flex items-center justify-between">
                  <span className="text-sm font-medium">{option}</span>
                  {showCorrect && <Check className="w-5 h-5 text-primary" />}
                  {showIncorrect && <X className="w-5 h-5 text-destructive" />}
                </div>
              </button>
            )
          })}
        </div>

        {/* Show Answer Button */}
        <div className="pt-4 border-t">
          <Button
            variant="ghost"
            size="sm"
            onClick={() => setShowAnswer(!showAnswer)}
            className="w-full hover:bg-primary/10"
          >
            {showAnswer ? (
              <>
                <EyeOff className="w-4 h-4 mr-2" />
                Açıklamayı Gizle
              </>
            ) : (
              <>
                <Eye className="w-4 h-4 mr-2" />
                Açıklamayı Göster
              </>
            )}
          </Button>

          {showAnswer && (
            <div className="mt-4 p-4 bg-primary/5 border border-primary/20 rounded-xl animate-fade-in space-y-3">
              <p className="text-sm font-semibold text-primary">Doğru Cevap: {correctAnswer}</p>
              {isLLMFormat && question.distractor_logic && (
                <div className="space-y-2">
                  <p className="text-xs font-semibold text-primary/70 uppercase">Distractor Analizi:</p>
                  {Object.entries(question.distractor_logic).map(([key, val], idx) => (
                    <div key={idx} className="text-xs text-muted-foreground p-2 bg-background/50 rounded border border-border/50">
                      <span className="font-medium">{key}:</span> {String(val)}
                    </div>
                  ))}
                </div>
              )}
              {explanationText && !isLLMFormat && (
                <p className="text-sm text-muted-foreground leading-relaxed">{explanationText}</p>
              )}
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  )
}
