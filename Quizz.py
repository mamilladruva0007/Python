questions = (
    "What is the capital of France?",
    "What is the capital of Germany?",
    "What is the capital of Italy?",
    "What is the capital of Spain?",
    "What is the capital of Portugal?"
)

options = (
    ("A. Paris", "B. Berlin", "C. Rome", "D. Madrid"),
    ("A. Paris", "B. Berlin", "C. Rome", "D. Lisbon"),
    ("A. Rome", "B. Madrid", "C. Paris", "D. Berlin"),
    ("A. Lisbon", "B. Rome", "C. Madrid", "D. Paris"),
    ("A. Berlin", "B. Lisbon", "C. Rome", "D. Madrid")
)

answers = ("A", "B", "A", "C", "B")

guesses = []
question_num = 0
score = 0

for question in questions:
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter the answer (A B C D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print(f"\nFinal Score: {score}/{len(questions)}")