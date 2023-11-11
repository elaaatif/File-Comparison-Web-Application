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

# Function to calculate word frequencies for a list of words
def calculate_word_frequencies(words):
    word_count = collections.Counter(words)
    return word_count

# Function to calculate cosine similarity between two word frequency dictionaries
def calculate_cosine_similarity(word_count1, word_count2):
    common_words = set(word_count1) & set(word_count2)
    dot_product = sum(word_count1[word] * word_count2[word] for word in common_words)
    
    magnitude1 = math.sqrt(sum(word_count1[word] ** 2 for word in word_count1))
    magnitude2 = math.sqrt(sum(word_count2[word] ** 2 for word in word_count2))
    
    if magnitude1 != 0 and magnitude2 != 0:
        cosine_similarity = dot_product / (magnitude1 * magnitude2)
    else:
        cosine_similarity = 0

    return cosine_similarity, dot_product

# Main function to calculate similarity
def calculate_similarity(file1_path, file2_path):
    words1 = read_file(file1_path)
    words2 = read_file(file2_path)

    word_count1 = calculate_word_frequencies(words1)
    word_count2 = calculate_word_frequencies(words2)

    similarity, dot_product = calculate_cosine_similarity(word_count1, word_count2)

    return {
        "common_words": list(set(word_count1) & set(word_count2)),
        "dot_product": dot_product,
        "cosine_similarity": similarity,
    }

# Example usage:
file1_path = "text1.txt"
file2_path = "text2.txt"
results = calculate_similarity(file1_path, file2_path)
print(results)
