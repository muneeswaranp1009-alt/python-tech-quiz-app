def run_quiz():

    quiz_data = {
        1: {
            "question": "What is the output of print(2 ** 3) in Python?",
            "options": ["A) 6", "B) 8", "C) 9", "D) 12"],
            "answer": "B"
        },
        2: {
            "question": "Which data type is used to store key-value pairs in Python?",
            "options": ["A) List", "B) Tuple", "C) Dictionary", "D) String"],
            "answer": "C"
        },
        3: {
            "question": "What does CPU stand for?",
            "options": ["A) Central Process Unit", "B) Computer Personal Unit", "C) Central Processing Unit", "D) Central Processor Unit"],
            "answer": "C"
        }
    }

    score = 0
    total_questions = len(quiz_data)

    print("===  Ultimate Python & Tech Quiz ===\n")
    print("Type A, B, C, or D as your answer.\n")

    for q_num, q_info in quiz_data.items():
        print(f"Question {q_num}: {q_info['question']}")
        
        for option in q_info['options']:
            print(option)
        
        user_answer = input("\nYour Answer: ").strip().upper()
        
        if user_answer == q_info['answer']:
            print("\nCorrect Answer! Super!\n")
            score += 1
        else:
            print(f"\nWrong! The correct answer is {q_info['answer']}.\n")
        
        print("-" * 40)
        
    print(f"\nFinal Score: {score} out of {total_questions}\n")
    
    percentage = (score / total_questions) * 100
    if percentage == 100:
        print("\nYou Got Full marks!\n")
    elif percentage >= 50:
        print("\nGood try! Keep learning!\n")
    else:
        print("\nOops! Need more practice.\n")

if __name__ == "__main__":
    run_quiz()