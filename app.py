
import streamlit as st
import fitz
import re
import pandas as pd
import spacy
from datetime import datetime
try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = None
st.set_page_config(
    page_title="Smart Resume Parser",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Smart Resume Parser")
st.write("Upload a Resume PDF and Extract Information Automatically")
SKILLS_DB = [
    "python", "java", "c", "c++", "sql",
    "machine learning", "deep learning",
    "data science", "data analysis",
    "artificial intelligence", "nlp",
    "tensorflow", "keras", "pandas",
    "numpy", "matplotlib", "seaborn",
    "streamlit", "flask", "django",
    "power bi", "tableau", "excel",
    "git", "github"
]
def extract_text_from_pdf(file):
    try:
        text = ""

        doc = fitz.open(
            stream=file.read(),
            filetype="pdf"
        )

        for page in doc:
            text += page.get_text() + "\n"

        return text

    except Exception as e:
        st.error(f"PDF Error: {e}")
        return ""
def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    return text.lower()
def extract_name(text):

    lines = text.split("\n")

    for line in lines[:10]:

        line = line.strip()

        if (
            len(line.split()) >= 2
            and len(line.split()) <= 5
            and "@" not in line
            and not any(char.isdigit() for char in line)
        ):
            return line.upper()

    return "Not Found"
def extract_email(text):
    emails = re.findall(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text
    )

    return list(set(emails))
def extract_phone(text):
    phones = re.findall(
        r'\b[6-9]\d{9}\b',
        text
    )

    return list(set(phones))
def extract_skills(text):

    found_skills = []

    for skill in SKILLS_DB:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return sorted(list(set(found_skills)))
def extract_education(text):

    education = []

    education_keywords = [
        "b.tech",
        "btech",
        "b.e",
        "be",
        "m.tech",
        "mtech",
        "mba",
        "mca",
        "bsc",
        "msc",
        "engineering",
        "college",
        "university",
        "cgpa"
    ]

    lines = text.split("\n")

    for line in lines:
        if any(keyword in line.lower() for keyword in education_keywords):
            education.append(line.strip())

    return list(set(education))
def extract_experience(text):

    experience = []

    keywords = [
        "Data Science Intern",
        "Data Analytics Intern",
        "Thiranex",
        "CodeAlpha",
        "Internship",
        "Intern",
        "project",
        "experience",
        "worked",
        "developed",
        "implemented",
        "company"
    ]

    for keyword in keywords:
        if keyword.lower() in text.lower():
            experience.append(keyword)

    return experience
def calculate_ats_score(skills):

    score = round(
        (len(skills) / len(SKILLS_DB)) * 100,
        2
    )

    return score
uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)
if uploaded_file:

    raw_text = extract_text_from_pdf(uploaded_file)

    if not raw_text.strip():
        st.error("No text could be extracted from this PDF.")
        st.stop()

    cleaned_text = clean_text(raw_text)

    name = extract_name(raw_text)
    emails = extract_email(raw_text)
    phones = extract_phone(raw_text)
    skills = extract_skills(cleaned_text)

    education = extract_education(raw_text)
    experience = extract_experience(raw_text)

    ats = calculate_ats_score(skills)
    st.subheader("📊 Resume Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("ATS Score", f"{ats}%")
    col2.metric("Skills Found", len(skills))
    col3.metric(
        "Date",
        datetime.now().strftime("%d-%m-%Y")
    )
    st.subheader("📌 Extracted Details")

    st.write("### 👤 Name")
    st.write(name)

    st.write("### 📧 Email")
    st.write(", ".join(emails) if emails else "Not Found")

    st.write("### 📱 Phone")
    st.write(", ".join(phones) if phones else "Not Found")

    st.write("### 🧠 Skills")
    st.write(", ".join(skills) if skills else "Not Found")

    st.write("### 🎓 Education")
    if education:
        for item in education:
            st.write("•", item)
    else:
        st.write("Not Found")

    st.write("### 💼 Experience")
    if experience:
        for item in experience:
            st.write("•", item)
    else:
        st.write("Not Found")
    st.subheader("📋 Structured Resume Data")

    df = pd.DataFrame({
        "Field": [
            "Name",
            "Email",
            "Phone",
            "Skills",
            "Education",
            "Experience",
            "ATS Score"
        ],
        "Value": [
            name,
            ", ".join(emails),
            ", ".join(phones),
            ", ".join(skills),
            ", ".join(education),
            ", ".join(experience),
            f"{ats}%"
        ]
    })

    st.dataframe(df, use_container_width=True)
    csv = df.to_csv(index=False)

    st.download_button(
        label="⬇ Download CSV Report",
        data=csv,
        file_name="resume_report.csv",
        mime="text/csv"
    )
    with st.expander("📄 View Extracted Resume Text"):
        st.text(raw_text[:5000])

