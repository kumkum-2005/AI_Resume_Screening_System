from utlise.parser import extract_resume_text


file_path = "uploads/resume.pdf"

text = extract_resume_text(file_path)


print("\n==============================")
print("EXTRACTED RESUME TEXT")
print("==============================\n")

print(text)