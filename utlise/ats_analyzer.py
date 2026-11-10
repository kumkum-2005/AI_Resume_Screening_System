def calculate_ats_score(match_score):
    """
    Skill match score ko ATS score me convert karta hai.
    """

    if match_score >= 80:
        category = "Excellent Match"

    elif match_score >= 60:
        category = "Good Match"

    elif match_score >= 40:
        category = "Moderate Match"

    else:
        category = "Low Match"

    return {
        "score": match_score,
        "category": category
    }


def generate_suggestions(
    matched_skills,
    missing_skills,
    resume_text
):
    """
    Resume improvement suggestions generate karta hai.
    """

    suggestions = []

    # Missing skills
    if missing_skills:

        suggestions.append(
            "Consider adding relevant missing skills "
            "if you genuinely have experience with them."
        )

    # GitHub
    if "github" not in resume_text.lower():

        suggestions.append(
            "Add your GitHub profile or relevant project links."
        )

    # Projects
    if "project" not in resume_text.lower():

        suggestions.append(
            "Add a Projects section with 2-4 relevant projects."
        )

    # Experience
    if (
        "experience" not in resume_text.lower()
        and "internship" not in resume_text.lower()
    ):

        suggestions.append(
            "Add internship, training, or relevant experience "
            "if applicable."
        )

    # Skills
    if len(matched_skills) < 3:

        suggestions.append(
            "Highlight your most relevant technical skills "
            "near the top of the resume."
        )

    # General ATS suggestion
    suggestions.append(
        "Use clear section headings such as Skills, "
        "Education, Experience and Projects."
    )

    return suggestions

def calculate_final_ats_score(
    skill_match_score,
    similarity_score
):
    """
    Skill matching aur TF-IDF similarity ko combine
    karke final ATS score calculate karta hai.
    """

    # Make sure both values are numbers
    skill_match_score = float(skill_match_score)
    similarity_score = float(similarity_score)

    final_score = (
        (skill_match_score * 0.70)
        +
        (similarity_score * 0.30)
    )

    final_score = round(final_score, 2)

    if final_score >= 80:
        category = "Excellent Match"

    elif final_score >= 60:
        category = "Good Match"

    elif final_score >= 40:
        category = "Moderate Match"

    else:
        category = "Low Match"

    return {
        "score": final_score,
        "category": category
    }