import collections
import math

# Function to read a text file and return its content as a list of words
def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        # Tokenize the content into words (split by whitespace and remove punctuation)
        words = content.split()
        words = [word.strip('.,!?()[]{}\'"') for word in words]  # Remove common punctuation
        words = [word.lower() for word in words]  # Convert words to lowercase
    return words

# Function to calculate cosine similarity between two lists of words
def calculate_cosine_similarity(words1, words2):
    word_count1 = collections.Counter(words1)
    word_count2 = collections.Counter(words2)

    common_words = set(word_count1.keys()) & set(word_count2.keys())

    dot_product = sum(word_count1[word] * word_count2[word] for word in common_words)

    magnitude1 = math.sqrt(sum(word_count1[word] ** 2 for word in word_count1))
    magnitude2 = math.sqrt(sum(word_count2[word] ** 2 for word in word_count2))

    if magnitude1 != 0 and magnitude2 != 0:
        cosine_similarity = dot_product / (magnitude1 * magnitude2)
    else:
        cosine_similarity = 0

    return cosine_similarity

# Main function to calculate similarity
def calculate_similarity(file1_path, file2_path):
    words1 = read_file(file1_path)
    words2 = read_file(file2_path)

    similarity = calculate_cosine_similarity(words1, words2)

    return {
        "cosine_similarity": similarity,
    }

# Example usage:
file1_path = "text1.txt"
file2_path = "text2.txt"
results = calculate_similarity(file1_path, file2_path)
print("Cosine Similarity:", results["cosine_similarity"])