import streamlit as st
from utils.pdf_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from models.job_predictor import predict_job_roles
from utils.scorer import compute_resume_score, get_improvement_suggestions

st.title("AI-Powered Resume Screening and Career Recommendation System")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Parsing and analyzing your resume..."):
        text = extract_text_from_pdf(uploaded_file)
        st.subheader("Extracted Resume Text")
        st.write(text[:2000] if text else "[No text found]")
        
        skills = extract_skills(text)
        st.subheader("Detected Skills")
        st.write(", ".join(skills) if skills else "[No skills detected]")
        
        predicted_roles = predict_job_roles(skills, text)
        st.subheader("Predicted Job Roles")
        st.write(", ".join(predicted_roles) if predicted_roles else "[No suitable roles predicted]")
        
        score = compute_resume_score(skills, text)
        st.subheader("Resume Quality Score")
        st.write(f"{score}/100")
        
        suggestions = get_improvement_suggestions(skills, text)
        st.subheader("Improvement Suggestions")
        if suggestions:
            for s in suggestions:
                st.markdown(f"- {s}")
        else:
            st.write("No major suggestions. Your resume looks good!")
