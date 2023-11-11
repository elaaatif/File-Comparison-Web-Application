from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import euclidean_distances

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

# Function to calculate the Euclidean distance using TF-IDF
def euclidean_distance_tfidf(doc1, doc2):
    # Create a TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer()

    # Transform the documents into TF-IDF vectors
    tfidf_matrix = tfidf_vectorizer.fit_transform([doc1, doc2])

    # Calculate the Euclidean distance
    euclidean_dist = euclidean_distances(tfidf_matrix[0], tfidf_matrix[1])

    return euclidean_dist[0][0]

# Calculate the Euclidean distance using TF-IDF
euclidean_dist = euclidean_distance_tfidf(file1_text, file2_text)

# Print the Euclidean distance
print(f"Euclidean Distance (TF-IDF): {euclidean_dist}")
    