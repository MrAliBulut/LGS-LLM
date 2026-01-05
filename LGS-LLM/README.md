# LGS-LLM: AI-Powered Exam Question Generator

An intelligent exam generation system that creates custom English language questions for the Turkish national high school entrance exam (LGS) using advanced Large Language Models and AI image generation.

## 🌟 Features

### Core Features
- **AI-Powered Question Generation** - Uses Groq's llama-3.3-70b-versatile model
- **AI Image Generation** - Supports Chroma and Zimage models for visual questions
- **Real-Time Streaming** - Questions stream to frontend as NDJSON for instant display
- **Text & Visual Questions** - Full support for both text-based and image-based questions
- **Smart Distribution** - Randomly distributes visual questions across topics
- **Priority Generation** - Text questions generated first for faster initial display

### Content Features
- **10 English Units** - Friendship, Teen Life, Kitchen, Phone, Internet, Adventures, Tourism, Chores, Science, Natural Forces
- **CEFR A1-A2 Level** - Proper 8th-grade English difficulty
- **Vocabulary Context** - Unit-specific vocabulary for accurate question generation

### Export Features
- **PDF Export with Images** - Full screenshot of exam with images (custom page height)
- **PDF Export Text-Only** - Clean text-based PDF without images
- **Answer Key** - Automatically appended to all PDF exports

### Developer Features
- **Session Logging** - Per-session JSON logs with timestamps
- **Debug Categories** - Organized debug output ([DEBUG], [DEBUG IG], [WARNING], [ERROR])
- **Prompt Engineering** - Customizable prompt templates for both text and visual questions

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9+** - [Download Python](https://www.python.org/downloads/)
- **Node.js 18+** - [Download Node.js](https://nodejs.org/)
- **pnpm** (recommended) - `npm install -g pnpm`
- **Groq API Key** - [Get API Key](https://console.groq.com/keys)

### Optional (for image generation)
- **Chroma API** - For Chroma image generation model
- **Zimage API** - For Zimage image generation model

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/LGS-LLM.git
cd LGS-LLM
```

### 2. Backend Setup

#### 2.1 Create Python Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 2.2 Install Python Dependencies

```bash
cd backend
pip install -r requirements.txt
```

#### 2.3 Set Environment Variables

Create a `.env` file in the `backend` directory:

```env
# Required
GROQ_API_KEY=your_groq_api_key_here

# Image Generation (optional)
IMAGE_GENERATION_MODEL=chroma  # or "zimage"
CHROMA_API_URL=your_chroma_api_url
ZIMAGE_API_URL=your_zimage_api_url
```

#### 2.4 Start Backend Server

```bash
python generate_exam.py
```

The backend will start on `http://localhost:8000`

Verify it's working: `http://localhost:8000/health`

### 3. Frontend Setup (New Terminal)

#### 3.1 Install Node Dependencies

```bash
cd frontend
pnpm install
```

#### 3.2 Start Frontend Development Server

```bash
pnpm dev
```

The frontend will start on `http://localhost:3000`

### 4. Access the Application

Open your browser and navigate to:
```
http://localhost:3000
```

## 📖 Usage

### Quick Start (Easiest)
1. Click **"Quick Start"** button on the home page
2. This generates 1 question for each of the 10 topics
3. Watch questions stream in real-time (text questions first, then visual)
4. Answer questions or click "Show Answer" for explanation
5. Download exam as PDF when complete

### Custom Distribution
1. Click **"Custom Configuration"**
2. Select which topics you want questions from
3. Choose how many questions per topic (slider: 0-5)
4. Optionally add visual questions (images)
5. Click **"Start Exam"**
6. Questions will be generated and streamed to your screen

### PDF Export Options
When all questions are loaded, click **"PDF İndir"** to see options:
- **Görseller ile** - Full visual PDF with images (single scrollable page + answer key)
- **Görseller olmadan** - Text-only PDF with questions and answer key

## 🏗️ Project Structure

```
LGS-LLM/
├── backend/
│   ├── generate_exam.py          # Main API server
│   ├── question_generator.py     # LLM integration
│   ├── prompts.py                # LLM prompt templates
│   ├── session_logger.py         # Per-session logging system
│   ├── requirements.txt          # Python dependencies
│   ├── logs/                     # Session log files (JSON)
│   ├── vocab/                    # Vocabulary files (10 units)
│   └── image_generation/         # Image generation modules
│       ├── generate_image.py     # Main image generation functions
│       ├── image_prompts.py      # Prompt engineering for images
│       ├── chroma_client.py      # Chroma API client
│       └── z_image_client.py     # Zimage API client
│
├── frontend/
│   ├── app/                      # Next.js app directory
│   ├── components/               # React components
│   │   ├── exam-configurator.tsx # Topic selection UI
│   │   ├── exam-workspace.tsx    # Question display & PDF export
│   │   ├── question-card.tsx     # Individual question component
│   │   └── ui/                   # Shadcn UI components
│   ├── types/                    # TypeScript type definitions
│   ├── package.json              # Node.js dependencies
│   └── tsconfig.json             # TypeScript config
│
├── changelogs/                   # Development documentation
│   ├── DEBUG_CATEGORIZATION.md   # Debug print system docs
│   └── SESSION_LOGGING.md        # Session logging system docs
│
├── README.md                     # This file
├── PROJECT_REPORT.html           # Detailed technical report
└── start_servers.ps1             # PowerShell script to start both servers
```

## 🔧 API Endpoints

### Health Check
```
GET http://localhost:8000/health
```

### Generate Exam
```
POST http://localhost:8000/generate-exam
Content-Type: application/json

{
  "distribution": {
    "Friendship": 2,
    "Teen Life": 1,
    ...
  },
  "visualCount": 2
}
```

**Response:** NDJSON stream of questions (text questions first, then visual)

## 📦 Dependencies

### Backend (Python)
- **FastAPI** - Modern web framework
- **Uvicorn** - ASGI server
- **Groq** - LLM API client
- **Python-dotenv** - Environment variable management
- **httpx** - Async HTTP client for image generation

### Frontend (Node.js)
- **Next.js 16** - React framework
- **React 19** - UI library
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Shadcn UI** - Component library
- **jsPDF** - PDF generation
- **dom-to-image-more** - DOM to image capture for PDF with images

## 📊 Supported Topics

| # | Topic | Words | Focus |
|----|-------|-------|-------|
| 1 | Friendship | 31 | Social relationships |
| 2 | Teen Life | 19 | Adolescent activities |
| 3 | In The Kitchen | 28 | Food & cooking |
| 4 | On The Phone | 15 | Communication |
| 5 | The Internet | 17 | Technology |
| 6 | Adventures | 18 | Travel |
| 7 | Tourism | 16 | Destinations |
| 8 | Chores | 17 | Household tasks |
| 9 | Science | 18 | Science concepts |
| 10 | Natural Forces | 15 | Natural phenomena |

## 🖼️ Image Generation

The system supports two image generation models:

### Chroma Model
- High-quality educational illustrations
- Prompt engineering with positive/negative prompts
- Configurable seed, steps, and guidance scale

### Zimage Model
- Fast image generation
- Single prompt approach
- Configurable dimensions and parameters

Set the model in `.env`:
```env
IMAGE_GENERATION_MODEL=chroma  # or "zimage"
```

## 📝 Session Logging

Every exam generation session creates a JSON log file in `backend/logs/`:

```
logs/
├── 2026-01-01_18-30-45-123.json
├── 2026-01-01_19-15-22-456.json
└── ...
```

Each log contains:
- Session timestamp and configuration
- Distribution logic and visual assignments
- All generated questions (without base64 image data)
- Image generation metadata
- Errors and completion status

## 🐛 Troubleshooting

### Backend won't start on port 8000

```bash
# Windows
taskkill /F /IM python.exe

# macOS/Linux
lsof -ti:8000 | xargs kill -9
```

### Groq API key not found

1. Make sure `.env` file exists in `backend/` directory
2. Verify `GROQ_API_KEY=` is set correctly
3. Restart the backend server

### Frontend can't reach backend

1. Verify backend is running: `http://localhost:8000/health`
2. Check browser console for errors (F12)
3. Clear browser cache and reload

### PDF Export Issues

- **"Görseller ile" not downloading**: Check browser console for errors
- **Content cut off**: The system uses custom page heights to prevent cutting

## 📈 Performance

**Question Generation Time:**
- Text question: 1-3 seconds
- Visual question: 5-15 seconds (includes image generation)
- 10 text questions: 10-30 seconds
- 10 visual questions: 50-150 seconds

*Text questions are prioritized and generated first for faster initial display*

## 🔄 How It Works

1. **User selects topics & quantities** on frontend
2. **Frontend sends POST request** to `/generate-exam` endpoint
3. **Backend creates session log** with timestamp
4. **Backend calculates visual distribution** (random allocation)
5. **Questions are sorted**: text first, visual last
6. **For each question:**
   - Backend calls LLM to generate question
   - LLM uses vocabulary context and prompt templates
   - If visual: generates image using Chroma/Zimage
   - Streams question to frontend as NDJSON
   - Logs question to session file
7. **Frontend receives and displays:**
   - Parses JSON line-by-line
   - Updates progress bar in real-time
   - Renders question using QuestionCard component
8. **User can:**
   - Answer questions
   - View explanations
   - Download as PDF (with or without images)

## 🎓 Educational Standards

Questions are generated following:
- **CEFR Level:** A1-A2 (8th grade)
- **Grammar Focus:** Present Simple, Past Simple, "be going to", Basic Modals
- **Question Style:** LGS exam format with preferences and reasoning
- **Distractor Logic:** Based on common language learning mistakes

## 📝 License

This project is open source.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues, questions, or suggestions:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Review the detailed [PROJECT_REPORT.html](./PROJECT_REPORT.html)
3. Check changelogs in `changelogs/` directory
4. Open an issue on GitHub

---

**Last Updated:** January 1, 2026  
**Status:** Completed ✅
