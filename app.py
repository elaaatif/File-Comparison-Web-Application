from flask import Flask, render_template, request
import os
from cosine import calculate_cosine_similarity 
from euclidean import calculate_euclidean_distance
from levenshtein import levenshtein_distance
from tf_idf_cosine import cosine_similarity_tfidf
from tf_idf_euclidean import euclidean_distance_tfidf
from werkzeug.utils import secure_filename  

app = Flask(__name__)

# Specify the allowed file extensions and create the 'uploads' directory if it doesn't exist
ALLOWED_EXTENSIONS = {'txt'}

if not os.path.exists("uploads"):
    os.makedirs("uploads")

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html', results=None)

@app.route('/compare', methods=['POST'])
def compare_files():
    # Get the selected calculation method
    calculation_method = request.form.get('calculation_method')

    # Check if the calculation method is selected
    if not calculation_method:
        return render_template('index.html', results=None)

    # Get the uploaded files
    file1 = request.files['file1']
    file2 = request.files['file2']

    # Check if both files are provided
    if 'file1' not in request.files or 'file2' not in request.files:
        return render_template('index.html', results=None)

    # Check if the file extensions are allowed
    if not allowed_file(file1.filename) or not allowed_file(file2.filename):
        return render_template('index.html', results=None)

    # Save the uploaded files to a temporary directory
    file1_path = os.path.join("uploads", secure_filename(file1.filename))
    file2_path = os.path.join("uploads", secure_filename(file2.filename))

    file1.save(file1_path)
    file2.save(file2_path)

    result = None  # Store the result

    if calculation_method == "cosine":
        result = calculate_cosine_similarity(file1_path, file2_path)
    elif calculation_method == "euclidean":
        result = calculate_euclidean_distance(file1_path, file2_path)
    elif calculation_method == "levenshtein":
        result = levenshtein_distance(file1_path, file2_path)
    elif calculation_method == "tf_idf_cosine":
        result = cosine_similarity_tfidf(file1_path, file2_path)   
    elif calculation_method == "tf_idf_euclidean":
        result = euclidean_distance_tfidf(file1_path, file2_path)   
    # Add more methods as needed

    # Delete the temporary files
    os.remove(file1_path)
    os.remove(file2_path)

    # Create a dictionary of method explanations and result comparisons
    method_info = {
        "cosine": {
            "explanation": "Cosine Similarity measures the cosine of the angle between two vectors, providing a value between -1 (completely dissimilar) and 1 (completely similar).",
            "comparison": "A cosine similarity result closer to 1 indicates high similarity, while a result closer to -1 indicates dissimilarity.",
        },
        "euclidean": {
            "explanation": "Euclidean Distance measures the straight-line distance between two points in space. Smaller values indicate greater similarity.",
            "comparison": "Smaller Euclidean distance values indicate greater similarity between the documents.",
        },
        "levenshtein": {
            "explanation": "Levenshtein Distance measures the minimum number of single-character edits required to change one word into the other. Smaller values indicate greater similarity.",
            "comparison": "Smaller Levenshtein distance values indicate greater similarity between the documents.",
        },
        "tf_idf_cosine": {
            "explanation": "TF-IDF Cosine Similarity uses the Term Frequency-Inverse Document Frequency metric to measure the similarity between two documents.",
            "comparison": "A cosine similarity result closer to 1 indicates high similarity, while a result closer to -1 indicates dissimilarity.",
        },
        "tf_idf_euclidean": {
            "explanation": "TF-IDF Euclidean Distance measures the Euclidean distance between the TF-IDF vectors of two documents.",
            "comparison": "Smaller Euclidean distance values indicate greater similarity between the documents.",
        },
        # Add more explanations and comparisons as needed
    }

    # Get the explanation and comparison for the selected method
    method_info_selected = method_info.get(calculation_method, {"explanation": "No explanation available.", "comparison": "No comparison available."})

    return render_template('index.html', results=result, result_method=calculation_method,
                           explanation=method_info_selected["explanation"], comparison=method_info_selected["comparison"])

if __name__ == '__main__':
    app.run(debug=True)
