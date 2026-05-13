def compute_resume_score(skills, text):
    # Simple scoring: number of skills found out of expected (max 100)
    max_skills = 10
    score = int((min(len(skills), max_skills) / max_skills) * 100)
    # Bonus for text length
    if len(text) > 2000:
        score += 10
    return min(score, 100)

def get_improvement_suggestions(skills, text):
    suggestions = []
    expected = {'machine learning', 'python', 'nlp', 'data analysis', 'communication', 'project management'}
    missing = expected.difference(set(skills))
    for miss in sorted(missing):
        suggestions.append(f"Consider adding or highlighting your experience with '{miss}' if relevant.")
    if len(text) < 800:
        suggestions.append("Your resume seems brief; try expanding key sections for better clarity.")
    return suggestions
