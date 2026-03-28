# 🧠 AI Code Debugger & Explainer (GenAI Project)

An advanced **Generative AI (GenAI) powered developer assistant** that detects bugs, explains code, suggests fixes, and optimizes performance across multiple programming languages.

---

## 🚀 Features

- 🧠 GenAI Code Analysis using LLM (Gemini API)
- 🐛 Bug Detection (Syntax + Logical Errors)
- 📖 Code Explanation (Beginner-friendly)
- 🔧 Auto Fix Suggestions
- ⚡ Code Optimization (Time & Space Complexity)
- ▶ Multi-language Execution
  - Python
  - C++
  - Java
  - JavaScript
- 🔗 GitHub Repository Analyzer
- 🎨 Modern Interactive UI (Streamlit + Custom CSS)

---

## 🛠 Tech Stack

- Generative AI: Gemini API (LLM)
- Backend: FastAPI
- Frontend: Streamlit
- Static Analysis: Python AST
- Execution Engine: Subprocess-based multi-language runner
- Version Control: Git & GitHub

---

## 🧠 How It Works

1. User inputs code or GitHub repository  
2. System performs:
   - AST-based syntax analysis  
   - LLM-based reasoning (GenAI)  
3. Generates:
   - Bugs  
   - Fixes  
   - Explanation  
   - Optimized code  

---

## ▶ Run Locally

### 1. Install Dependencies
pip install -r requirements.txt

### 2. Start Backend
cd backend  
uvicorn main:app --reload  

### 3. Start Frontend
cd frontend  
streamlit run app.py  

---

## 📸 Demo

## 📸 Demo

![Screenshot](screenshot.png)

---

## 💡 Author

Sujay Barai

---

## 🎯 Key Highlights

- Built a GenAI-powered debugging system  
- Combines LLM + static analysis (AST)  
- Supports multi-language execution  
- Performs repository-level analysis  

---

## 🔥 Future Improvements

- Chat-based debugging UI  
- Docker sandbox execution  
- Deployment (AWS / Render)  
- Authentication system  