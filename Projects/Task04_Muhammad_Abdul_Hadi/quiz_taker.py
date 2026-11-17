# Project - 4 : General Knowledge Quiz - DecodeLabs

print("\nWelcome to the General Knowledge Quiz!")

name = input("How should we call you? (Name): ").strip()

if name.lower() == "quit":
    print("\nThank you for visiting the General Knowledge Quiz!")
    exit()

print("-" * 40)
print("       General Knowledge Quiz!")
print("-" * 40)

print(f"\nDear {name}!")
print("\nYou will be asked 5 questions. Try to answer them correctly.")
print("Type 'quit' anytime to exit the quiz.")
print("Let's get started!\n")

questions = [
    {
        "question": "What is the capital of Japan?",
        "options": ["A. Tokyo", "B. Osaka", "C. Kyoto", "D. Nagoya"],
        "answer": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "C"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A. Go", "B. Gd", "C. Au", "D. Ag"],
        "answer": "C"
    },
    {
        "question": "In which year did the Titanic sink?",
        "options": ["A. 1912", "B. 1905", "C. 1920", "D. 1898"],
        "answer": "A"
    }
]

while True:

    score = 0
    quit_quiz = False

    print("\n" + "=" * 40)
    print("           QUIZ STARTED")
    print("=" * 40 + "\n")

    for q in questions:

        while True:

            print(q["question"])

            for option in q["options"]:
                print(option)

            user_answer = input("\nYour answer (A/B/C/D): ").upper().strip()

            # Quit option
            if user_answer == "QUIT":
                quit_quiz = True
                break

            if user_answer not in ['A', 'B', 'C', 'D']:

                print("\nInvalid input! Please enter A, B, C, or D.")

                repeat_answer = input(
                    "Do you want to answer this question again? (yes/no): "
                ).lower().strip()

                if repeat_answer == "quit":
                    quit_quiz = True
                    break

                if repeat_answer in ['yes', 'y']:
                    print("\nLet's try again!\n")
                    continue

                else:
                    print("Skipping this question!\n")
                    break

            elif user_answer == q["answer"]:

                print("Correct!\n")
                score += 1
                break

            else:

                print(f"Wrong! The correct answer is {q['answer']}.\n")
                break

        if quit_quiz:
            break

    # Final Score
    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    print("\n" + "=" * 40)
    print("             QUIZ RESULT")
    print("=" * 40)

    print(f"\nDear {name}, here is your result!")
    print(f"Total Questions : {total_questions}")
    print(f"Correct Answers : {score}")
    print(f"Wrong / Skipped : {total_questions - score}")
    print(f"Percentage      : {percentage:.2f}%")

    # Grade the quiz based on the score

    if score == total_questions:

        print("\nExcellent! You got all the answers correct!")
        print("Grade: A+")

    elif score >= 4:

        print("\nGood job! You scored well.")
        print("Grade: B")

    elif score >= 2:

        print("\nNice effort! You can do even better with more practice.")
        print("Grade: C")

    elif score == 1:

        print("\nKeep trying! You can improve with more practice.")
        print("Grade: D")

    else:

        print("\nBetter luck next time! Keep learning and trying.")
        print("Grade: F")

    print("\n" + "=" * 40)

    # Check whether the user wants to quit

    if quit_quiz:
        print("\nYou have exited the quiz.")
        break

    # Play Again Option

    play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()

    if play_again == "quit":
        print("\nExiting the quiz...")
        break

    if play_again not in ['yes', 'y']:
        break

    print("\nStarting a new game...\n")

print("\nThank you for playing the General Knowledge Quiz!")
print(f"Goodbye, {name}! Have a great day.")