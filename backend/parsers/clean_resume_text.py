import pandas as pd
import re
import spacy
import nltk
from nltk.corpus import stopwords

# Download stopwords if not already downloaded
nltk.download('stopwords')

# Define paths
INPUT_CSV = "../../data/complete_resume_data.csv"
OUTPUT_CSV = "../../data/cleaned_resume_data.csv"

# Load dataset
df = pd.read_csv(INPUT_CSV)

# Load NLP model
try:
    nlp = spacy.load("en_core_web_sm")  # Try loading model
except OSError:
    print("Downloading 'en_core_web_sm' model...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")  # Load model after download


# Get stopwords
stop_words = set(stopwords.words("english"))

def clean_text(text):
    """Cleans resume text by removing special characters, stopwords, and performing lemmatization."""
    if pd.isnull(text):  # Handle missing values
        return ""

    # Convert to lowercase
    text = text.lower()

    # Remove special characters, numbers, and extra whitespace
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()

    # Tokenize and lemmatize text
    doc = nlp(text)
    cleaned_text = " ".join([token.lemma_ for token in doc if token.text not in stop_words])

    return cleaned_text

# Apply cleaning function to both Resume_str and Text columns
df["Cleaned_Resume_str"] = df["Resume_str"].apply(clean_text)
df["Cleaned_Text"] = df["Text"].apply(clean_text)

# Save cleaned data
df.to_csv(OUTPUT_CSV, index=False)

print(f"Cleaned resume data saved to {OUTPUT_CSV}")
