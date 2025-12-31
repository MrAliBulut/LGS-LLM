# LGS-LLM: AI-Powered Exam Question Generator

An intelligent exam generation system that creates custom English language questions for the Turkish national high school entrance exam (LGS) using advanced Large Language Models.

## 🌟 Features

- **AI-Powered Question Generation** - Uses Groq's llama-3.3-70b-versatile model
- **Real-Time Streaming** - Questions stream to frontend as NDJSON for instant display
- **Text & Visual Questions** - Support for both text-based and image-based questions
- **Smart Distribution** - Randomly distributes visual questions across topics
- **10 English Units** - Friendship, Teen Life, Kitchen, Phone, Internet, Adventures, Tourism, Chores, Science, Natural Forces
- **CEFR A1-A2 Level** - Proper 8th-grade English difficulty
- **Progress Tracking** - Real-time progress bar with instant updates
- **PDF Export** - Download generated exams as PDF
- **Vocabulary Context** - Unit-specific vocabulary for accurate question generation

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9+** - [Download Python](https://www.python.org/downloads/)
- **Node.js 18+** - [Download Node.js](https://nodejs.org/)
- **Git** - [Download Git](https://git-scm.com/)
- **MongoDB Atlas Account** - [Create Account](https://www.mongodb.com/cloud/atlas)
- **Groq API Key** - [Get API Key](https://console.groq.com/keys)

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
GROQ_API_KEY=your_groq_api_key_here
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/
```

To get these:
- **Groq API Key**: Visit [console.groq.com](https://console.groq.com/keys)
- **MongoDB URI**: Go to MongoDB Atlas → Your Cluster → Connect → Drivers → Copy connection string

#### 2.4 Start Backend Server

```bash
python generate_exam.py
```

The backend will start on `http://localhost:8000`

You can verify it's working by visiting: `http://localhost:8000/health`

### 3. Frontend Setup (New Terminal)

#### 3.1 Install Node Dependencies

```bash
cd frontend
npm install
# or
pnpm install
```

#### 3.2 Start Frontend Development Server

```bash
npm run dev
# or
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
3. Watch questions stream in real-time
4. Answer questions or click "Show Answer" for explanation
5. Download exam as PDF when complete

### Custom Distribution
1. Click **"Custom Configuration"**
2. Select which topics you want questions from
3. Choose how many questions per topic (slider: 0-5)
4. Optionally add visual questions (images)
5. Click **"Start Exam"**
6. Questions will be generated and streamed to your screen

## 🏗️ Project Structure

```
LGS-LLM/
├── backend/
│   ├── generate_exam.py          # Main API server
│   ├── question_generator.py     # LLM integration
│   ├── prompts.py                # LLM prompt templates
│   ├── requirements.txt           # Python dependencies
│   └── vocab/                    # Vocabulary files (10 units)
│
├── frontend/
│   ├── app/                      # Next.js app directory
│   ├── components/               # React components
│   ├── package.json              # Node.js dependencies
│   └── tsconfig.json             # TypeScript config
│
├── README.md                      # This file
├── .gitignore                     # Git ignore rules
└── PROJECT_REPORT.html           # Detailed technical report
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
  "visualCount": 0
}
```

**Response:** NDJSON stream of questions

## 📦 Dependencies

### Backend (Python)
- **FastAPI** - Modern web framework
- **Uvicorn** - ASGI server
- **Motor** - Async MongoDB driver
- **Groq** - LLM API client
- **Python-dotenv** - Environment variable management
- **Pydantic** - Data validation

### Frontend (Node.js)
- **Next.js** - React framework
- **React** - UI library
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Shadcn UI** - Component library
- **jsPDF** - PDF generation

## 🔐 Environment Variables

### Backend (.env)

```env
# Required
GROQ_API_KEY=your_groq_api_key

# Optional (defaults to MongoDB Atlas)
MONGO_URI=mongodb+srv://user:password@cluster.mongodb.net/database
```

### Frontend
No environment variables needed for basic setup.

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

## 🐛 Troubleshooting

### Backend won't start on port 8000

**Issue:** "Port 8000 already in use"

**Solution:**
```bash
# Windows
taskkill /F /IM python.exe

# macOS/Linux
lsof -ti:8000 | xargs kill -9
```

### Groq API key not found

**Issue:** "GROQ_API_KEY not configured"

**Solution:**
1. Make sure `.env` file exists in `backend/` directory
2. Verify `GROQ_API_KEY=` is set correctly
3. Restart the backend server

### MongoDB connection failed

**Issue:** "MongoDB connection failed"

**Solution:**
1. Verify MongoDB Atlas URI in `.env`
2. Check IP whitelist in MongoDB Atlas dashboard
3. Ensure internet connection is active
4. Verify username and password are correct

### Frontend can't reach backend

**Issue:** "Failed to fetch questions" or "API error"

**Solution:**
1. Verify backend is running: `http://localhost:8000/health`
2. Check browser console for errors (F12)
3. Clear browser cache and reload
4. Restart both frontend and backend

## 📈 Performance

**Question Generation Time:**
- Single question: 1-3 seconds
- 5 questions: 5-15 seconds
- 10 questions: 10-30 seconds
- 20+ questions: 30-60+ seconds

*Times vary based on Groq API load*

## 🔄 How It Works

1. **User selects topics & quantities** on frontend
2. **Frontend sends POST request** to `/generate-exam` endpoint
3. **Backend calculates visual distribution** (random allocation)
4. **For each question:**
   - Backend calls LLM to generate question
   - LLM uses examples from database + vocabulary context
   - If visual: extracts image prompt
   - Streams question to frontend as NDJSON
5. **Frontend receives and displays:**
   - Parses JSON line-by-line
   - Updates progress bar in real-time
   - Renders question using QuestionCard component
6. **User can:**
   - Answer questions
   - View explanations
   - Download as PDF

## 🎓 Educational Standards

Questions are generated following:
- **CEFR Level:** A1-A2 (8th grade)
- **Grammar Focus:** Present Simple, Past Simple, "be going to", Basic Modals
- **Question Style:** LGS exam format with preferences and reasoning
- **Distractor Logic:** Based on common language learning mistakes

## 📝 License

This project is open source. Specify your license here.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues, questions, or suggestions:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Review the detailed [PROJECT_REPORT.html](./PROJECT_REPORT.html)
3. Open an issue on GitHub

## 🚀 Deployment

For production deployment:
- Follow security recommendations in PROJECT_REPORT.html
- Use environment variables for all sensitive data
- Set up proper CORS policies
- Implement rate limiting
- Use HTTPS/SSL certificates
- Set up monitoring and logging

## 📞 Contact

Your contact information here.

---

**Last Updated:** December 31, 2025  
**Status:** In Development ✨
