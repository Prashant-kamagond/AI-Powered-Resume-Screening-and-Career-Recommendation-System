# Demo role prediction (expand with ML later)
def predict_job_roles(skills, text):
    # Map skill clusters to roles
    role_map = {
        'Data Scientist': {'machine learning', 'python', 'data analysis', 'pandas', 'numpy', 'scikit-learn'},
        'NLP Engineer': {'nlp', 'machine learning', 'python', 'deep learning'},
        'Software Engineer': {'python', 'sql', 'data analysis', 'leadership', 'project management'},
        'Business Analyst': {'analysis', 'communication', 'project management', 'sql'},
    }
    roles = []
    for role, keywords in role_map.items():
        if len(keywords.intersection(set(skills))) >= 2:
            roles.append(role)
    if not roles:
        # Simple fallback based on keywords in text
        if "developer" in text.lower():
            roles.append("Developer")
    return roles
