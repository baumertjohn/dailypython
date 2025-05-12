# A basic quiz program...

quiz_questions = [("What is the capital of France?", ["Berlin", "Paris", "Madrid", "Rome"], 2),
                  ("Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], 3),
                  ("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "H2"], 1), ]


def print_question(question_num):
    question, choices, correct_answer = quiz_questions[question_num]
    print(question)
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")
    user_choice = check_valid_answer()
    return user_choice, correct_answer, choices


def check_valid_answer():
    while True:
        error = "Enter integer between 1 and 4!"
        try:
            user_answer = int(input("Your answer (1/2/3/4): "))
            if 0 < user_answer < 5:
                return user_answer
            print(error)
            continue
        except ValueError:
            print(error)
    

def main():
    score = 0
    for question in range(len(quiz_questions)):
        user_answer, correct_answer, choices = print_question(question)
        if user_answer == correct_answer:
            score += 1
            print("Correct!\n")
        else:
            correct_text = f"{correct_answer}. {choices[correct_answer-1]}"
            print(f"Wrong! The correct answer was {correct_text}\n")
        
    print(f"Quiz completed! Your final score is {score}/3.")
        

if __name__ == "__main__":
    main()
