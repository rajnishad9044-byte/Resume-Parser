import re
import PyPDF2

# Skills Database
SKILLS_DB = [
    "Python", "Java", "C", "C++", "JavaScript",
    "HTML", "CSS", "SQL", "MySQL",
    "Machine Learning", "Data Science",
    "AI", "React", "NodeJS"
]


# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""

    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except FileNotFoundError:
        print("Error: PDF file not found!")
        return ""

    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

    return text


# Extract Email
def extract_email(text):
    emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
    return emails[0] if emails else "Not Found"


# Extract Phone Number
def extract_phone(text):
    phones = re.findall(r'\b\d{10}\b', text)
    return phones[0] if phones else "Not Found"


# Extract Name
def extract_name(text):
    lines = [line.strip() for line in text.split("\n") if line.strip()]

    # Try to find line before Email
    for i, line in enumerate(lines):
        if "email" in line.lower():
            if i > 0:
                return lines[i - 1]

    # Fallback
    return lines[0] if lines else "Not Found"


# Extract Skills
def extract_skills(text):
    found_skills = []

    for skill in SKILLS_DB:
        pattern = r'\b' + re.escape(skill) + r'\b'

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills


# Extract Education
def extract_education(text):
    education_keywords = [
        "B.Tech",
        "BCA",
        "MCA",
        "B.Sc",
        "M.Sc",
        "MBA",
        "Diploma",
        "Intermediate",
        "B.Pharma",
        "M.Pharma"
    ]

    education = []

    for item in education_keywords:
        pattern = r'\b' + re.escape(item) + r'\b'

        if re.search(pattern, text, re.IGNORECASE):
            education.append(item)

    return education


# Parse Resume
def parse_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)

    if not text:
        return None

    result = {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "Skills": extract_skills(text),
        "Education": extract_education(text)
    }

    return result


# Main Program
if __name__ == "__main__":

    print("===== RESUME PARSER =====")

    resume_file = input("Enter Resume PDF Path: ").strip()

    data = parse_resume(resume_file)

    if data:
        print("\n===== RESUME DETAILS =====")

        for key, value in data.items():
            print(f"{key}: {value}")

    else:
        print("\nFailed to parse resume.")