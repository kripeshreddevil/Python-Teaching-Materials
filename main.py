import csv
import pandas as pd
from PyPDF2 import PdfReader

# Load the CSV file
csv_file = "C:\\Users\\kripe\\Downloads\\Data-from-AI-Detections.csv"
csv_data = pd.read_csv(csv_file)

# Load the PDF file
pdf_file = "C:\\Users\\kripe\\Downloads\\Dataset from Validator.pdf"
pdf_reader = PdfReader(pdf_file)

# Function to extract data from the PDF
def extract_pdf_data(pdf_reader):
    rows = []
    for page in pdf_reader.pages:
        text = page.extract_text()
        lines = text.split('\n')
        for line in lines:
            columns = line.split()
            if len(columns) == 10:  # Ensure it's a valid row with 10 columns
                rows.append(columns)
    return rows

pdf_data = extract_pdf_data(pdf_reader)

# Remove rows from PDF where only photo_link exists (i.e., other columns are empty)
filtered_pdf_data = [row for row in pdf_data if any(row[2:])]  # Ignore rows where only photo_link is present

# Now compare photo_link column in both the PDF and CSV
mismatch_found = False

# Assuming both CSV and filtered PDF data have 1216 rows
for i, (pdf_row, csv_row) in enumerate(zip(filtered_pdf_data, csv_data.itertuples()), start=1):
    pdf_photo_link = pdf_row[1]  # Assuming photo_link is the 2nd column
    csv_photo_link = csv_row.photo_link  # Assuming photo_link column in CSV has this name
    if pdf_photo_link != csv_photo_link:
        print(f"Row no {i} has a mismatch")
        mismatch_found = True

if not mismatch_found:
    print("All photo_links match!")

