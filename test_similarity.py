from utlise.parser import extract_resume_text
from utlise.text_processor import clean_text
from utlise.similarity import calculate_similarity


# ==========================================
# Resume
# ==========================================

resume_file = "uploads/resume.pdf"


# Extract resume text
resume_text = extract_resume_text(
    resume_file
)


# Clean resume
cleaned_resume = clean_text(
    resume_text
)


# ==========================================
# Job Description
# ==========================================

job_description = """
We are looking for a Python Developer
with experience in Machine Learning,
SQL, Flask, Docker and GitHub.

The candidate should have knowledge of
REST API development, data analysis,
backend development and model deployment.
"""


# Clean JD
cleaned_jd = clean_text(
    job_description
)


# ==========================================
# Calculate Similarity
# ==========================================

similarity_score = calculate_similarity(
    cleaned_resume,
    cleaned_jd
)


# ==========================================
# Display Result
# ==========================================

print("\n======================================")
print("       TF-IDF SIMILARITY RESULT")
print("======================================")

print(
    "\nResume-JD Similarity:",
    similarity_score,
    "%"
)

print("======================================")