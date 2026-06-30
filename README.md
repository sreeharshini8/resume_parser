# 📄 Smart Resume Parser

## 📌 Project Overview

Smart Resume Parser is an AI-based application that automatically extracts important information from a resume PDF and displays it in a structured format. The project uses Natural Language Processing (NLP), Regular Expressions (Regex), and Streamlit to analyze resumes and identify key details such as name, email, phone number, skills, education, and experience.

---

## 🎯 Objectives

* Upload and analyze resume PDFs
* Extract candidate information automatically
* Identify technical skills from resumes
* Display resume details in a structured format
* Generate an ATS (Applicant Tracking System) score
* Export extracted information as a CSV report

---

## 🚀 Features

✅ Resume PDF Upload

✅ Automatic Text Extraction

✅ Name Extraction

✅ Email Extraction

✅ Phone Number Extraction

✅ Skills Detection

✅ Education Extraction

✅ Experience Extraction

✅ ATS Score Calculation

✅ Structured Resume Dashboard

✅ CSV Report Download

---

## 🛠️ Technologies Used

* Python
* Streamlit
* PyMuPDF (fitz)
* spaCy
* Pandas
* Regular Expressions (Regex)

---

## 📂 Project Structure

```text
resume-parser/
│
├── app.py
├── README.md
└── sample_resume.pdf
```

---

## ⚙️ Installation


### Create Virtual Environment

```bash
py -m venv .venv
```

### Activate Virtual Environment

```bash
.\.venv\Scripts\activate
```


### Install spaCy Model

```bash
python -m spacy download en_core_web_sm
```

---

## ▶️ Run Application

```bash
py -m streamlit run app.py
```

---

## 📊 Output

The application extracts:

* Candidate Name
* Email Address
* Phone Number
* Technical Skills
* Education Details
* Experience Details
* ATS Score

and displays the results in a structured dashboard.

---

## 📈 Future Enhancements

* Resume Ranking System
* Job Description Matching
* Skill Gap Analysis
* Resume Recommendation Engine
* Multiple Resume Comparison
* Advanced NLP-based Parsing

---

## 👩‍💻 Author

**JAGARLAMUDI SREE HARSHINI**

B.Tech – Artificial Intelligence & Data Science

---

## 📜 License

This project is developed for educational and internship purposes.
