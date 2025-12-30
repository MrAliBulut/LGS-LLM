import type { NextRequest } from "next/server"

// Mock soru havuzu
const QUESTION_POOL = {
  "Arkadaşlık (Ünite 1)": [
    "Gerçek arkadaşlık için en önemli özellik nedir?",
    "Aşağıdaki davranışlardan hangisi arkadaşlıkta güveni zedeler?",
    "İyi bir arkadaş nasıl olmalıdır?",
  ],
  "Ergenlik (Ünite 2)": [
    "Ergenlik döneminin en belirgin özelliği nedir?",
    "Ergenlik döneminde görülen fiziksel değişiklikler hangileridir?",
    "Ergenlikte duygusal değişimler nasıl yönetilir?",
  ],
  "Bilim (Ünite 3)": [
    "Bilimsel yöntemin ilk adımı nedir?",
    "Deney sonuçları nasıl değerlendirilir?",
    "Hipotez nedir ve nasıl oluşturulur?",
  ],
  "Teknoloji (Ünite 4)": [
    "Modern teknolojinin günlük hayattaki en önemli etkisi nedir?",
    "Yapay zeka uygulamaları hangi alanlarda kullanılır?",
    "Teknolojinin etik kullanımı neden önemlidir?",
  ],
  "Spor (Ünite 5)": [
    "Düzenli spor yapmanın sağlığa faydaları nelerdir?",
    "Takım sporlarının bireysel gelişime katkısı nedir?",
    "Olimpiyatların amacı nedir?",
  ],
  "Sağlık (Ünite 6)": [
    "Dengeli beslenme neden önemlidir?",
    "Su tüketiminin vücuda faydaları nelerdir?",
    "Uyku düzeninin önemi nedir?",
  ],
  "Doğa (Ünite 7)": [
    "Ekosistemin dengesi nasıl korunur?",
    "İklim değişikliğinin nedenleri nelerdir?",
    "Geri dönüşümün doğaya faydaları nelerdir?",
  ],
  "Sanat (Ünite 8)": [
    "Sanatın topluma katkısı nedir?",
    "Rönesans dönemi sanatının özellikleri nelerdir?",
    "Modern sanat akımları hangileridir?",
  ],
  "Tarih (Ünite 9)": [
    "Tarihi kaynak nedir ve türleri nelerdir?",
    "Osmanlı İmparatorluğu'nun kuruluş dönemi nasıl geçmiştir?",
    "Cumhuriyetin ilanının önemi nedir?",
  ],
  "Kültür (Ünite 10)": [
    "Kültürel miras nedir ve neden korunmalıdır?",
    "Türk kültürünün temel özellikleri nelerdir?",
    "Kültürel çeşitlilik neden önemlidir?",
  ],
}

const OPTIONS = [
  ["Güven ve dürüstlük", "Maddi değer", "Fiziksel güç", "Popülerlik"],
  ["Bilimsel düşünme", "Eleştirel yaklaşım", "Dikkatlice gözlem", "Hızlı sonuç"],
  ["Dengeli ve çeşitli beslenme", "Sadece et tüketimi", "Fastfood ağırlıklı beslenme", "Az yemek yeme"],
  ["İletişimi kolaylaştırma", "İnsanları yalnızlaştırma", "Maliyeti artırma", "Karmaşıklaştırma"],
]

// Soru generate fonksiyonu
function generateQuestion(topic: string, index: number, hasImage: boolean) {
  const questions = QUESTION_POOL[topic as keyof typeof QUESTION_POOL] || ["Örnek soru metni?"]
  const questionText = questions[Math.floor(Math.random() * questions.length)]
  const optionSet = OPTIONS[Math.floor(Math.random() * OPTIONS.length)]
  const correctIndex = Math.floor(Math.random() * 4)

  return {
    id: `q${index + 1}`,
    unit: topic.match(/\d+/)?.[0] || "1",
    topic,
    question: `${questionText}`,
    options: optionSet.map((opt, i) => `${String.fromCharCode(65 + i)}) ${opt}`),
    correctAnswer: String.fromCharCode(65 + correctIndex),
    hasImage,
    imageUrl: hasImage
      ? `/placeholder.svg?height=300&width=600&query=${encodeURIComponent(topic + " eğitim görseli")}`
      : undefined,
    explanation: `Bu sorunun doğru cevabı ${String.fromCharCode(65 + correctIndex)} şıkkıdır. Çünkü ${questionText.toLowerCase()} konusunda bu seçenek en doğru açıklamayı içermektedir.`,
  }
}

export async function POST(request: NextRequest) {
  const { distribution, visualCount } = await request.json()

  // Readable stream oluştur
  const encoder = new TextEncoder()
  const stream = new ReadableStream({
    async start(controller) {
      let questionIndex = 0
      let visualQuestionsAssigned = 0

      // Konu dağılımına göre sorular oluştur
      for (const [topic, count] of Object.entries(distribution)) {
        for (let i = 0; i < (count as number); i++) {
          const hasImage = visualQuestionsAssigned < visualCount
          if (hasImage) visualQuestionsAssigned++

          // Görselli sorular için daha uzun bekleme süresi (2000ms), normal sorular için 500ms
          const delay = hasImage ? 2000 : 500
          await new Promise((resolve) => setTimeout(resolve, delay))

          const question = generateQuestion(topic, questionIndex, hasImage)

          // JSON olarak stream'e yaz
          const data = encoder.encode(JSON.stringify(question) + "\n")
          controller.enqueue(data)

          questionIndex++
        }
      }

      controller.close()
    },
  })

  return new Response(stream, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
      "Transfer-Encoding": "chunked",
    },
  })
}
