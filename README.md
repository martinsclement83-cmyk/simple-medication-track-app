# 💊 Drug Information & Safety Checker App

A Streamlit-based application that provides simplified, reliable drug information using OpenFDA and AI assistance. The app helps users understand medication usage, warnings, side effects, and safety recalls in simple everyday language.

---

## 🚀 Features

- 🔍 Search drug information using OpenFDA API  
- ⚠️ Detect drug recalls and safety alerts  
- 🤖 AI-powered simplification of medical text (Gemini API)  
- 📚 Search history tracking (local storage)  
- ❌ Input validation for drug names  
- 🌐 Network error handling with custom exceptions  
- 📄 Clean UI with Streamlit tabs (Info / AI / Safety)

---

## 🧠 Core Functionality

- Fetches real-time drug data from OpenFDA
- Identifies missing or unavailable drug records
- Converts complex medical terms into simple language using AI
- Checks if a drug has been flagged in recall databases
- Stores user search history locally for later review

---

## 🏗️ Project Structure
project/
│
├── app.py # Main Streamlit UI
├── medication.py # OpenFDA API handler
├── text_processor.py # Input cleaning & validation
├── recall_checker.py # Drug recall checker
├── ai_translator.py # AI simplification module
├── search_history.py # Local search storage
└── README.md

---

## ⚙️ Technologies Used

- Python 🐍  
- Streamlit  
- Requests  
- Regex (text processing)  
- JSON handling  
- OpenFDA API  
- Google Gemini API  

---

## ⚠️ Error Handling

The system uses custom exception handling to ensure stability:

- `InvalidDrugNameError` → triggered for incorrect input format  
- `DrugNotFoundError` → triggered when API returns no drug data  
- `APIConnectionError` → triggered during network/API failure  
- Empty fields are handled gracefully with fallback values  

---

## 🔌 APIs Used

- OpenFDA Drug Labeling API  
  https://api.fda.gov/drug/label.json  

- OpenFDA Recall Enforcement API  
  https://api.fda.gov/drug/enforcement.json  

- Google Gemini API (for AI text simplification)

---

## ▶️ How to Run

```bash
pip install streamlit requests
streamlit run app.py



👨‍💻 Project Purpose

This project demonstrates:

API integration
Object-Oriented Programming (OOP)
Exception handling
Data cleaning using regex
Real-world healthcare data processing
AI-assisted text simplification

