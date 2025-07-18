import os
from flask import render_template, request, send_file
from app import app
from app.utils import get_questions_by_category

# Path to the downloads folder
DOWNLOADS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'downloads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download/<category>', methods=['GET'])
def download(category):
    # Get questions for the selected category
    questions = get_questions_by_category(category)

    # Dynamically create a filename based on the category
    filename = f"{category.replace(' ', '_')}_questions.txt"
    file_path = os.path.join(DOWNLOADS_PATH, filename)

    # Ensure the downloads directory exists
    if not os.path.exists(DOWNLOADS_PATH):
        os.makedirs(DOWNLOADS_PATH)

    # Write questions to the text file
    with open(file_path, 'w', encoding='utf-8') as f:
        for question in questions:
            f.write(f"{question}\n")

    # Send the file for download
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return f"File {filename} not found!", 404
