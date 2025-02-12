import os
import pymupdf as fitz

import pandas as pd

# Define paths (relative to where this script is executed)
INPUT_FOLDER = "../../data/resumes/"  # Folder containing categorized resume PDFs
OUTPUT_FOLDER = "../../data/resume_texts/"
OUTPUT_CSV = "../../data/resume_extracted_from_pdfs.csv"

# Ensure output folder exists
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file"""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

resume_data = []  # Store extracted resume details

# Iterate through each job category folder
for category in os.listdir(INPUT_FOLDER):
    category_path = os.path.join(INPUT_FOLDER, category)
    
    if os.path.isdir(category_path):  # Ensure it's a directory
        for pdf_file in os.listdir(category_path):
            if pdf_file.endswith(".pdf"):
                pdf_path = os.path.join(category_path, pdf_file)
                text = extract_text_from_pdf(pdf_path)
                
                # Store in structured format
                resume_data.append({
                    "ResumeID": pdf_file.replace(".pdf", ""),
                    "Text": text,
                    "Category": category
                })
                
                # Save extracted text to a file
                txt_filename = os.path.splitext(pdf_file)[0] + ".txt"
                with open(os.path.join(OUTPUT_FOLDER, txt_filename), "w", encoding="utf-8") as f:
                    f.write(text)

# Convert extracted data into a Pandas DataFrame
df_pdf_resumes = pd.DataFrame(resume_data)

# Save to CSV
df_pdf_resumes.to_csv(OUTPUT_CSV, index=False)

print(f"Resume text extracted and saved to {OUTPUT_CSV}")
