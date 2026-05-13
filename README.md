# AI-Powered Resume Screening and Career Recommendation System

This project is an AI-powered system that automates resume screening and provides personalized career recommendations using NLP and machine learning. Upload your resume (PDF), extract your skills, predict suitable job roles, receive a resume quality score, and get tailored suggestions for improvement.

## 🚀 Features
- Upload and analyze PDF resumes
- Extract important skills (NLP-driven)
- Predict suitable job roles
- Generate a resume quality score
- Personalized suggestions to improve your resume
- Interactive web interface (Streamlit)

## 🛠️ Tech Stack
- Python
- Streamlit
- Natural Language Processing (spaCy / NLTK)
- scikit-learn
- PyPDF2

## 📁 Project Structure
```
├── app
│   └── main.py
├── data
├── models
│   └── job_predictor.py
├── utils
│   ├── pdf_parser.py
│   ├── skill_extractor.py
│   └── scorer.py
├── requirements.txt
└── README.md
```

## ⚡ Quick Start
1. **Clone the repository**
2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Run Streamlit app:**
    ```bash
    streamlit run app/main.py
    ```

## 📑 How it Works
1. Upload a resume PDF.
2. The system extracts text and skills using NLP.
3. It predicts job roles using a demo ML model (customizable).
4. It calculates a resume quality score.
5. It provides personalized suggestions based on analysis.

## 🙌 Contribution
Feel free to open issues or pull requests for features/bugfixes!

---

