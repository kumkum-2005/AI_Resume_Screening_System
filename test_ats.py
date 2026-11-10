from utlise.parser import extract_resume_text
from utlise.text_processor import clean_text
from utlise.skill_extractor import extract_skills
from utlise.matcher import compare_skills
from utlise.ats_analyzer import (
    calculate_ats_score,
    generate_suggestions
)


# ==========================================
# 1. Resume File
# ==========================================

resume_file = "uploads/resume.pdf"


# ==========================================
# 2. Extract Resume Text
# ==========================================

resume_text = extract_resume_text(resume_file)


# ==========================================
# 3. Clean Resume Text
# ==========================================

cleaned_resume = clean_text(resume_text)


# ==========================================
# 4. Extract Resume Skills
# ==========================================

resume_skills = extract_skills(cleaned_resume)


# ==========================================
# 5. Job Description
# ==========================================

job_description = """
We are looking for a Python Developer
with experience in Machine Learning,
SQL, Flask, Docker, AWS and GitHub.

The candidate should have knowledge of
Python programming, data analysis and
REST API development.
"""


# ==========================================
# 6. Clean Job Description
# ==========================================

cleaned_jd = clean_text(job_description)


# ==========================================
# 7. Extract Job Skills
# ==========================================

jd_skills = extract_skills(cleaned_jd)


# ==========================================
# 8. Compare Skills
# ==========================================

match_result = compare_skills(
    resume_skills,
    jd_skills
)


# ==========================================
# 9. Calculate ATS Score
# ==========================================

ats_result = calculate_ats_score(
    match_result["score"]
)


# ==========================================
# 10. Generate Suggestions
# ==========================================

suggestions = generate_suggestions(
    match_result["matched"],
    match_result["missing"],
    cleaned_resume
)


# ==========================================
# 11. Display Result
# ==========================================

print("\n==========================================")
print("        AI RESUME ATS ANALYZER")
print("==========================================")


print("\nResume Skills:")
for skill in resume_skills:
    print("✓", skill)


print("\nRequired Job Skills:")
for skill in jd_skills:
    print("✓", skill)


print("\nMatched Skills:")
for skill in match_result["matched"]:
    print("✓", skill)


print("\nMissing Skills:")
for skill in match_result["missing"]:
    print("✗", skill)


print("\n==========================================")
print("ATS SCORE")
print("==========================================")

print(
    "Score:",
    ats_result["score"],
    "%"
)

print(
    "Category:",
    ats_result["category"]
)


print("\n==========================================")
print("RESUME IMPROVEMENT SUGGESTIONS")
print("==========================================")


for number, suggestion in enumerate(
    suggestions,
    start=1
):

    print(
        f"{number}. {suggestion}"
    )


print("\n==========================================")