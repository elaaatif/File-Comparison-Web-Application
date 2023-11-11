# import collections  # No need to import collections, it's not used in this code
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

# Function to calculate Levenshtein distance between two strings
def levenshtein_distance(str1, str2):
    len1, len2 = len(str1), len(str2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        dp[i][0] = i

    for j in range(len2 + 1):
        dp[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,  # Deletion
                dp[i][j - 1] + 1,  # Insertion
                dp[i - 1][j - 1] + cost,  # Substitution
            )

    return dp[len1][len2]

# Main function to calculate similarity
def calculate_similarity(file1_path, file2_path):
    words1 = read_file(file1_path)
    words2 = read_file(file2_path)

    similarity = levenshtein_distance(words1, words2)

    return {
        "levenshtein similarity": similarity,
    }

# Example usage:
file1_path = "text1.txt"
file2_path = "text2.txt"
result = calculate_similarity(file1_path, file2_path)
print(f"Levenshtein similarity between '{file1_path}' and '{file2_path}' is {result['levenshtein similarity']}")
