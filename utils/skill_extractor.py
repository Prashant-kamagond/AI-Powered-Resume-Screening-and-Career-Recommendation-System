import spacy
import re

# Dummy skill list for demo purposes
default_skills = [
    'machine learning', 'python', 'data analysis', 'nlp', 'deep learning', 'streamlit', 'scikit-learn',
    'communication', 'project management', 'teamwork', 'leadership', 'sql', 'pandas', 'numpy', 'analysis'
]

try:
    nlp = spacy.load("en_core_web_sm")
except Exception:
    nlp = None

def extract_skills(text, skills_list=default_skills):
    text = text.lower()
    found_skills = set()
    for skill in skills_list:
        if re.search(r'\\b' + re.escape(skill) + r'\\b', text):
            found_skills.add(skill)
    # Optionally use NLP for more advanced extraction here
    return sorted(list(found_skills))
