import pandas as pd

# Define paths
CSV_PATH = "../../data/resume_data.csv"
PDF_EXTRACTED_PATH = "../../data/resume_extracted_from_pdfs.csv"
MERGED_OUTPUT_PATH = "../../data/complete_resume_data.csv"

# Load existing CSV dataset
df_csv = pd.read_csv(CSV_PATH)
df_csv.rename(columns={"ID": "ResumeID"}, inplace=True)  # Rename for consistency

# Load extracted PDF text dataset
df_pdf = pd.read_csv(PDF_EXTRACTED_PATH)

# Merge based on ResumeID, keeping all columns
df_combined = pd.merge(df_csv, df_pdf, on=["ResumeID", "Category"], how="outer")

# Save final dataset
df_combined.to_csv(MERGED_OUTPUT_PATH, index=False)

print(f"Merged dataset saved as {MERGED_OUTPUT_PATH}")
