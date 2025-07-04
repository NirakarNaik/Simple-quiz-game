# Simple Quiz App in Python

# List of quiz questions (each is a dictionary)
quiz_questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Who wrote the play 'Romeo and Juliet'?", "answer": "William Shakespeare"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "What is the boiling point of water in Celsius?", "answer": "100"},
    {"question": "Who was the first President of the United States?", "answer": "George Washington"},
    {"question": "Which animal is known as the 'King of the Jungle'?", "answer": "Lion"},
    {"question": "How many continents are there in the world?", "answer": "7"},
    {"question": "What is the chemical symbol for Gold?", "answer": "Au"},
    {"question": "In which year did India get independence?", "answer": "1947"},
    {"question": "What is the square root of 64?", "answer": "8"}
]

score = 0

print("Welcome to the Quiz! 🧠\n")

# Manual loop using index
i = 0
while i < len(quiz_questions):
    q = quiz_questions[i]
    print(f"Q{i+1}: {q['question']}")
    user_answer = input("Your answer: ").strip()

    if user_answer.lower() == q['answer'].lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is: {q['answer']}\n")
    
    i += 1

print(f"Quiz Completed! 🎉 Your score: {score}/{len(quiz_questions)}")
