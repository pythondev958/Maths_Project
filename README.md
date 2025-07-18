# Maths Project

## Description

This project is designed to classify and categorize mathematical questions based on their topics using machine learning. The app uses a trained Support Vector Machine (SVM) model to categorize the questions into predefined categories such as **Algebra**, **Geometry**, **Number Theory**, **Probability**, and more.

The app is built using **Flask** for the backend and provides a simple user interface for downloading categorized questions in text format.

---

## Features

- **Machine Learning**: Trains a model to categorize math questions into predefined topics.
- **Flask Web App**: Simple web interface that allows users to download questions categorized by topic.
- **Data Storage**: Questions and their corresponding categories are stored in a text format for easy access and categorization.
- **Downloadable Text Files**: Users can download categorized questions based on topics like Algebra, Geometry, etc.

---

## Setup & Installation

To set up and run this project locally, follow the steps below.

### 1. Clone the repository

```bash
git clone https://github.com/pythondev958/Maths_Project.git
cd Maths_Project

2. Create and activate a virtual environment
For Windows:

python -m venv venv
venv\Scripts\activate
For macOS/Linux:

python3 -m venv venv
source venv/bin/activate
3. Install dependencies
Install all required dependencies by running:
pip install -r requirements.txt
4. Run the Flask app
python run.py
