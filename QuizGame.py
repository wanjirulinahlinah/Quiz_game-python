def quiz_game():
    print("Welcome to the Quiz Game!")
    print("Instructions: Answer the following questions. Each correct answer will earn you 1 point.")

    questions = [
   
        {
            "question": "Which of the following is the odd one out'?",
            "options": ["A.Apple ", "B. Banana", "C. Orange", "D. Carrot"],
            "answer": "D"
        },
        {
            "question": "Match the country with its capital?",
            "options": ["A.Germany 1 Paris ", "B. France  2 Berlin", "C. Italy 3Rome"],
            "answer": "B"
        },
             {
            "question": "?",
            "options": ["A. Paris", "B. Rome", "C. London", "D. Madrid"],
            "answer": "A"
        }
        
        
    ]

    score = 0

    for question in questions:
        print("\n" + question["question"])
        for option in question["options"]:
            print(option)
        
        user_answer = input("Enter your answer (A, B, C, D): ")
        if user_answer.upper() == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print("\nQuiz Completed!")
    print("Your final score is:", score, "out of", len(questions))

if __name__ == "__main__":
    quiz_game()
