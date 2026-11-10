def compare_skills(resume_skills, jd_skills):
    """
    Resume skills aur Job Description skills ko compare karta hai.
    """

    # Lowercase sets
    resume_set = set(skill.lower() for skill in resume_skills)
    jd_set = set(skill.lower() for skill in jd_skills)

    # Common skills
    matched_skills = resume_set.intersection(jd_set)

    # Skills present in JD but missing from resume
    missing_skills = jd_set - resume_set

    # Calculate match score
    if len(jd_set) > 0:
        score = (len(matched_skills) / len(jd_set)) * 100
    else:
        score = 0

    return {
        "matched": sorted(matched_skills),
        "missing": sorted(missing_skills),
        "score": round(score, 2)
    }