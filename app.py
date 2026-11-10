from flask import Flask, render_template, request
import os

from utlise.parser import extract_resume_text
from utlise.text_processor import clean_text
from utlise.skill_extractor import extract_skills
from utlise.matcher import compare_skills
from utlise.similarity import calculate_similarity

from utlise.ats_analyzer import (
    calculate_final_ats_score,
    generate_suggestions
)


# ==========================================
# Flask App
# ==========================================

app = Flask(__name__)


# ==========================================
# Upload Folder
# ==========================================

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder automatically
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ==========================================
# Allowed File Extensions
# ==========================================

ALLOWED_EXTENSIONS = {"pdf", "docx"}


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# Analyze Resume
# ==========================================

@app.route("/analyze", methods=["POST"])
def analyze():

    # ======================================
    # Get Uploaded Resume
    # ======================================

    resume_file = request.files.get("resume")

    # Get Job Description
    job_description = request.form.get(
        "job_description",
        ""
    )


    # ======================================
    # Validate Resume
    # ======================================

    if not resume_file:
        return "Please upload a resume."

    if resume_file.filename == "":
        return "Please select a resume file."

    if not allowed_file(resume_file.filename):
        return "Only PDF and DOCX files are allowed."


    # ======================================
    # Validate Job Description
    # ======================================

    if not job_description.strip():
        return "Please enter a Job Description."


    # ======================================
    # Save Resume
    # ======================================

    filename = resume_file.filename

    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    resume_file.save(file_path)


    try:

        # ==================================
        # 1. Extract Resume Text
        # ==================================

        resume_text = extract_resume_text(
            file_path
        )


        if not resume_text.strip():

            return (
                "Could not extract text from this resume. "
                "Please use a text-based PDF or DOCX file."
            )


        # ==================================
        # 2. Clean Resume Text
        # ==================================

        cleaned_resume = clean_text(
            resume_text
        )


        # ==================================
        # 3. Extract Resume Skills
        # ==================================

        resume_skills = extract_skills(
            cleaned_resume
        )


        # ==================================
        # 4. Clean Job Description
        # ==================================

        cleaned_jd = clean_text(
            job_description
        )


        # ==================================
        # 5. Extract Job Description Skills
        # ==================================

        jd_skills = extract_skills(
            cleaned_jd
        )


        # ==================================
        # 6. Compare Skills
        # ==================================

        match_result = compare_skills(
            resume_skills,
            jd_skills
        )


        # ==================================
        # 7. TF-IDF Similarity
        # ==================================

        similarity_score = calculate_similarity(
            cleaned_resume,
            cleaned_jd
        )


        # ==================================
        # 8. Final ATS Score
        # ==================================

        ats_result = calculate_final_ats_score(
            match_result["score"],
            similarity_score
        )


        # ==================================
        # 9. Generate Suggestions
        # ==================================

        suggestions = generate_suggestions(
            match_result["matched"],
            match_result["missing"],
            cleaned_resume
        )


        # ==================================
        # 10. Delete Uploaded Resume
        # ==================================

        if os.path.exists(file_path):
            os.remove(file_path)


        # ==================================
        # 11. Show Result
        # ==================================

        return render_template(
            "result.html",

            # Resume skills
            resume_skills=resume_skills,

            # Job description skills
            jd_skills=jd_skills,

            # Matching skills
            matched_skills=match_result["matched"],

            # Missing skills
            missing_skills=match_result["missing"],

            # Final ATS score
            score=ats_result["score"],

            # ATS category
            category=ats_result["category"],

            # Individual scores
            skill_match_score=match_result["score"],
            similarity_score=similarity_score,

            # Suggestions
            suggestions=suggestions
        )


    except Exception as e:

        # ==================================
        # Delete File If Error Occurs
        # ==================================

        if os.path.exists(file_path):
            os.remove(file_path)

        return (
            f"Error while analyzing resume: {str(e)}"
        )


# ==========================================
# Run Application
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )