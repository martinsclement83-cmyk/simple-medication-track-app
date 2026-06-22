# 💊 Medication Information Finder

A Streamlit-based medication information system that helps users search for drug details, understand medical information in simple language, and check for safety recalls using real-world APIs and AI assistance.

---

## 🚀 Features

- 🔍 Drug information lookup using OpenFDA API  
- ⚠️ Drug recall safety checker (FDA Enforcement API)  
- 🤖 AI-powered simplification of medical text (Gemini API)  
- 📚 Search history tracking (local file storage)  
- ❌ Input validation with custom error handling  
- 🌐 Network/API error handling  
- 📄 Clean Streamlit UI with tab-based layout (Info / AI / Safety)

---

## 🧠 Key Learning Concepts

### Object-Oriented Programming (OOP)
- `Medication` → Handles drug data retrieval
- `RecallChecker` → Checks FDA recall database
- `AITranslator` → Simplifies medical text using AI
- `SearchHistory` → Stores and retrieves past searches

### Exception Handling
- `InvalidDrugNameError` → Handles invalid input
- `DrugNotFoundError` → Handles missing API results
- `APIConnectionError` → Handles network/API failures
- Graceful fallback for missing fields

### File Handling
- Stores search history in local JSON file
- Reads and updates previous searches
- Ensures persistent user data

### Text Processing (Regex)
- Cleans and validates user input
- Removes unwanted characters
- Normalizes medication names

---

## ⚙️ Tech Stack

- **Language:** Python 3.8+
- **UI Framework:** Streamlit
- **APIs:**
  - OpenFDA Drug Labeling API
  - OpenFDA Recall/Enforcement API
  - Google Gemini API (AI simplification)
- **Libraries:**
  - requests
  - re (regex)
  - json

---

## 📁 Project Structure

    ```
    project/
    │
    ├── app.py               # Main Streamlit application
    ├── medication.py        # Drug information handler (OpenFDA API)
    ├── recall_checker.py    # Drug recall detection module
    ├── ai_translator.py     # Gemini AI text simplifier
    ├── search_history.py    # Local search history storage
    ├── text_processor.py    # Input cleaning & validation
    └── README.md
    ````

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install streamlit requests
````

### 2. Run the app

```bash
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 🧪 How It Works

1. User enters a drug name
2. App validates input
3. OpenFDA API fetches drug details
4. Recall API checks safety alerts
5. Gemini AI simplifies medical explanation
6. Search is saved to history
7. Results are displayed in structured tabs

---

## ⚠️ Error Handling

The system handles multiple failure cases:

* Invalid drug input → `InvalidDrugNameError`
* Drug not found → `DrugNotFoundError`
* Network failure → `APIConnectionError`
* Missing data → replaced with “Not available”

---

## 🔌 APIs Used

* OpenFDA Drug Labeling API
  [https://api.fda.gov/drug/label.json](https://api.fda.gov/drug/label.json)

* OpenFDA Recall API
  [https://api.fda.gov/drug/enforcement.json](https://api.fda.gov/drug/enforcement.json)

* Google Gemini API
  [https://ai.google.dev](https://ai.google.dev)

---

## 🎯 Purpose of Project

This project demonstrates:

* Real-world API integration
* Object-Oriented Programming design
* Exception handling strategies
* Data cleaning and validation
* AI-assisted information simplification
* UI development using Streamlit

---

## ⚠️ Disclaimer

This application is for *educational purposes only*.

* Not a substitute for medical advice
* Always consult a healthcare professional
* Do not rely solely on AI-generated explanations

---

## 👨‍💻 Contributors

# GRIUP MEMBERS NAME HERE
SIWES Group Project
Built collaboratively using modular Python architecture.

---

## 🚀 Future Improvements

* Drug interaction checker
* Voice-based search
* Mobile-friendly version
* Offline drug database caching
* Improved AI medical explanations

---