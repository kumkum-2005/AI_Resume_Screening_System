import pandas as pd
import os

# Skills list
skills = [
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript",
    "HTML",
    "CSS",
    "React",
    "Angular",
    "Node.js",
    "Express.js",
    "Flask",
    "Django",
    "FastAPI",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "NLP",
    "Computer Vision",
    "TensorFlow",
    "PyTorch",
    "Scikit-learn",
    "Pandas",
    "NumPy",
    "OpenCV",
    "Matplotlib",
    "Seaborn",
    "Git",
    "GitHub",
    "Docker",
    "AWS",
    "Azure",
    "Google Cloud",
    "Power BI",
    "Tableau",
    "Excel",
    "Data Analysis",
    "Data Science",
    "Statistics",
    "REST API",
    "Linux"
]

# Create DataFrame
df = pd.DataFrame(skills, columns=["Skill"])

# Create model folder if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save CSV
df.to_csv("model/skills.csv", index=False)

print("skills.csv created successfully!")
print(f"Total skills: {len(skills)}")