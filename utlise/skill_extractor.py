import pandas as pd
import re


def load_skills():
    """
    skills.csv se skills load karta hai.
    """

    skills_df = pd.read_csv("model/skills.csv")

    skills = skills_df["Skill"].dropna().tolist()

    return skills


def extract_skills(text):
    """
    Resume text me available skills find karta hai.
    """

    skills = load_skills()

    detected_skills = []

    text_lower = text.lower()

    for skill in skills:

        skill_lower = skill.lower()

        pattern = r'(?<!\w)' + re.escape(skill_lower) + r'(?!\w)'

        if re.search(pattern, text_lower):

            detected_skills.append(skill)

    return detected_skills