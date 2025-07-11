# 📄 CVInsight – AI-Powered Resume Analyzer

CVInsight is a full-stack AI-powered web app that helps users optimize their resumes by analyzing how well they match a specific job description. The app uses GPT-4 to highlight missing skills, weak points, and offers tailored suggestions to improve the candidate's chances of landing the job.

---

## 🚀 Features

- 🔍 Upload resume (PDF or text)
- 📝 Paste any job description
- 🤖 GPT-4 analysis to:
  - Calculate a match score
  - Identify missing or weak skills
  - Suggest resume improvements
- 🗂 Store previous analyses (session-based)
- 💬 Clean and responsive UI

---

## 🧰 Tech Stack

| Layer      | Tech                |
|------------|---------------------|
| Frontend   | React, Tailwind CSS |
| Backend    | Python (Flask or FastAPI) |
| AI Engine  | OpenAI GPT-4 API    |
| Database   | PostgreSQL          |
| Others     | PDF parsing libs (`pdfminer`, `PyMuPDF`), REST API, Axios, etc.

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/cvinsight.git
cd cvinsight
