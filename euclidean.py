import collections
import math

# Function to read a text file and return its content as a list of words
def read_file(file_path):
    with open(file_path, "r") as file:
        words = file.read().split()
    return words

# Function to calculate word frequencies for a list of words
def calculate_word_frequencies(words):
    word_count = collections.Counter(words)
    return word_count

# Function to calculate Euclidean distance between two word frequency dictionaries
def calculate_euclidean_distance(word_count1, word_count2):
    all_words = set(word_count1) | set(word_count2)
    distance = math.sqrt(
        sum((word_count1[word] - word_count2[word]) ** 2 for word in all_words)
    )
    magnitude1 = math.sqrt(
        sum(word_count1[word] ** 2 for word in word_count1)
    )
    magnitude2 = math.sqrt(
        sum(word_count2[word] ** 2 for word in word_count2)
    )
    return distance, magnitude1, magnitude2

# Function to calculate normalized Euclidean distance
def calculate_normalized_euclidean(distance, magnitude1, magnitude2):
    if magnitude1 != 0 and magnitude2 != 0:
        normalized_distance = distance / (magnitude1 * magnitude2)
    else:
        normalized_distance = 0
    return normalized_distance

# Main function to calculate similarity
def calculate_similarity(file1_path, file2_path):
    words1 = read_file(file1_path)
    words2 = read_file(file2_path)

    word_count1 = calculate_word_frequencies(words1)
    word_count2 = calculate_word_frequencies(words2)

    distance, magnitude1, magnitude2 = calculate_euclidean_distance(
        word_count1, word_count2
    )
    normalized_distance = calculate_normalized_euclidean(
        distance, magnitude1, magnitude2
    )

    return {
        "common_words": list(set(word_count1) & set(word_count2)),
        "euclidean_distance": distance,
        "normalized_distance": normalized_distance,
    }

# Example usage:
file1_path = "text1.txt"
file2_path = "text2.txt"
results = calculate_similarity(file1_path, file2_path)
print(results)
