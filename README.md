# Resume_Analyser
This Web application allows users to upload resume and match recommended jobs




mkdir resume-analyzer
cd resume-analyzer
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


pip install fastapi uvicorn pandas numpy spacy nltk scikit-learn joblib beautifulsoup4 requests transformers torch
pip install scrapy sqlalchemy psycopg2 pydantic pdfminer.six


pdfminer.six & PyMuPDF: Extract text from PDF resumes
spaCy & nltk: Natural Language Processing (NLP)
pandas: Data processing
scikit-learn: Machine learning
fastapi: Web framework for backend API



pip install kaggle
mkdir ~/.kaggle
mv kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
kaggle datasets download -d snehaanbhawal/resume-dataset
unzip resume-dataset.zip -d data/resumes/

