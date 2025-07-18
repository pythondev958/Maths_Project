import ast
import os

# Load questions and their categories from the data files
def load_data():
    questions = []
    categories = []

    # Read questions from Questions.txt
    with open(os.path.join('data', 'Questions.txt'), 'r', encoding='utf-8') as f:
        questions = ast.literal_eval("[" + f.read().strip() + "]")

    # Read categories from Categories.txt
    with open(os.path.join('data', 'Categories.txt'), 'r', encoding='utf-8') as f:
        categories = ast.literal_eval("[" + f.read().strip() + "]")
    
    return questions, categories

# Get questions by category
def get_questions_by_category(category):
    questions, categories = load_data()
    # Filter questions based on the selected category
    return [q for q, c in zip(questions, categories) if c == category]
