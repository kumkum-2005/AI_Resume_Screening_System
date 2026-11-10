from utlise.parser import extract_resume_text
from utlise.text_processor import clean_text
from utlise.skill_extractor import extract_skills


# Resume file path
file_path = "uploads/resume.pdf"


# Step 1: Extract text from resume
resume_text = extract_resume_text(file_path)


# Step 2: Clean extracted text
cleaned_text = clean_text(resume_text)


# Step 3: Extract skills
skills = extract_skills(cleaned_text)


# Display results
print("\n====================================")
print("        RESUME SKILL ANALYSIS")
print("====================================")

print("\nExtracted Skills:")

if skills:

    for skill in skills:
        print("✓", skill)

else:

    print("No skills detected.")


print("\nTotal Skills:", len(skills))