from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 1. Facility Data: Career Assessment Results
career_profiles = {
    "Technical": "You belong in Software Dev or Engineering. You love logic!",
    "Creative": "You belong in Design or Marketing. You have a great imagination!",
    "Social": "You belong in Teaching or Healthcare. You enjoy helping others!"
}

# 2. Facility Data: Mock Test Questions
mock_questions = [
    {"id": 1, "q": "What is 15% of 200?", "options": ["20", "30", "40"], "ans": "30"},
    {"id": 2, "q": "Which language is used for AI?", "options": ["Python", "HTML", "CSS"], "ans": "Python"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assessment')
def assessment():
    return render_template('assessment.html')

@app.route('/mock-test')
def mock_test():
    return render_template('mock_test.html', questions=mock_questions)

@app.route('/submit-assessment', methods=['POST'])
def submit_assessment():
    data = request.json
    # Simple logic: If they picked 'A' most, they are technical
    choice = data.get('top_choice') 
    result = career_profiles.get(choice, "Generalist")
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)