from utlise.parser import extract_resume_text
from utlise.text_processor import clean_text
from utlise.skill_extractor import extract_skills
from utlise.matcher import compare_skills


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
# 8. Compare Resume and Job Skills
# ==========================================

result = compare_skills(
    resume_skills,
    jd_skills
)


# ==========================================
# 9. Display Results
# ==========================================

print("\n========================================")
print("       AI RESUME SCREENING RESULT")
print("========================================")


print("\nResume Skills:")
for skill in resume_skills:
    print("✓", skill)


print("\nJob Required Skills:")
for skill in jd_skills:
    print("✓", skill)


print("\nMatched Skills:")
for skill in result["matched"]:
    print("✓", skill)


print("\nMissing Skills:")
for skill in result["missing"]:
    print("✗", skill)


print("\n----------------------------------------")
print("Match Score:", result["score"], "%")
print("----------------------------------------")