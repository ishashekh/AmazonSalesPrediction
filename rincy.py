import pandas as pd

# Load the dataset
file_path = 'C:/Jency_College/Semester2/CaseStudies/Project/data/Amazon.csv'
data = pd.read_csv(file_path)

# Step 1: Remove duplicate rows
data_cleaned = data.drop_duplicates()

# Commit message: "Added data loading and initial cleaning script."
