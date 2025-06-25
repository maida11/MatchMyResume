# 📄 MatchMyResume – AI-Powered Resume Screener

**MatchMyResume** is an AI-powered web app that intelligently compares a resume with a job description and provides a match score based on semantic similarity. It uses transformer-based NLP models to go beyond keyword matching and truly understand context.

---

## 🚀 Features

- 🧠 Semantic similarity using SentenceTransformer (MiniLM)
- 📄 Upload resumes in PDF, DOCX, or TXT format
- 📝 Paste job descriptions for comparison
- 💯 Get an instant match score (cosine similarity)
- 🧹 Preview extracted resume text for transparency
- 🔄 Compatible with scanned resumes via OCR (Tesseract)

---

## 🛠️ Tech Stack

- `Python`
- `Streamlit`
- `sentence-transformers`
- `pdfminer.six` / `PyMuPDF`
- `python-docx`
- `pytesseract` (optional for image-based PDFs)

---
