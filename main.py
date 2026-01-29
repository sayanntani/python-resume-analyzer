import os
import pdfplumber

def analyze_pdf_resume(file_path):
    resume_text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                resume_text += text + "\n"

    print("DEBUG: Extracted text from PDF:")
    print(repr(resume_text))  # Shows hidden characters

    keywords = ["Python", "Machine Learning", "Data Analysis", "Communication"]
    found_keywords = [kw for kw in keywords if kw.lower() in resume_text.lower()]

    print("\nResume Analysis Report")
    print("----------------------")
    print(f"Total words: {len(resume_text.split())}")
    print(f"Keywords found: {', '.join(found_keywords) if found_keywords else 'None'}")

if __name__ == "__main__":
    resume_file = "resume.pdf"
    if os.path.exists(resume_file):
        analyze_pdf_resume(resume_file)
    else:
        print("No resume.pdf file found. Please add one!")