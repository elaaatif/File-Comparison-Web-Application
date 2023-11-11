# Specify the file paths for the two text files
file1_path = "text1.txt"
file2_path = "text2.txt"

# Initialize empty lists to store the contents of the files
file1_words = []
file2_words = []

# Read the first file and split it into words
with open(file1_path, "r") as file1:
    file1_words = file1.read().split()

# Read the second file and split it into words
with open(file2_path, "r") as file2:
    file2_words = file2.read().split()

# Print the words from the first file
print("Words from file1.txt:")
for word in file1_words:
    print(word)

# Print the words from the second file
print("Words from file2.txt:")
for word in file2_words:
    print(word)