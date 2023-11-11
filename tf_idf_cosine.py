from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Specify the file paths for the two text files
file1_path = "text1.txt"
file2_path = "text2.txt"
# Initialize empty strings to store the contents of the files
file1_text = ""
file2_text = ""
# Read the first file and store its content in a string
with open(file1_path, "r") as file1:
    file1_text = file1.read()
# Read the second file and store its content in a string
with open(file2_path, "r") as file2:
    file2_text = file2.read()
# Function to calculate the cosine similarity using TF-IDF
def cosine_similarity_tfidf(doc1, doc2):
    # Create a TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer()

    # Transform the documents into TF-IDF vectors
    tfidf_matrix = tfidf_vectorizer.fit_transform([doc1, doc2])

    # Calculate the cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

    return cosine_sim[0][0]
# Calculate the cosine similarity using TF-IDF
cosine_sim = cosine_similarity_tfidf(file1_text, file2_text)

# Print the cosine similarity
print(f"Cosine Similarity (TF-IDF): {cosine_sim}")

# using TF-IDF based on the contents of the two text files. 
# The result will be the cosine similarity score between the two files based on their TF-IDF representations.