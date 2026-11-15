"""
DecodeLabs Internship
Python Programming - Project 4
Project: General Knowledge Quiz

"""

# Welcome message
print("=" * 45)
print("       GENERAL KNOWLEDGE QUIZ")
print("          DecodeLabs Project 4")
print("=" * 45)

print("\nWelcome to the General Knowledge Quiz!")
print("You will be asked 3 questions.")
print("Each correct answer gives you 1 point.")
print("Let's begin!\n")


# Initialize score
score = 0


# -----------------------------------
# QUESTION 1
# -----------------------------------

print("Question 1:")
print("What is the capital of Turkey?")

answer = input("Your answer: ")

# Sanitize user input
answer = answer.strip().lower()

if answer == "ankara":
    print("Correct! Well done.\n")
    score += 1

else:
    print("Incorrect! The correct answer is Ankara.\n")


# -----------------------------------
# QUESTION 2
# -----------------------------------

print("Question 2:")
print("Which planet is known as the Red Planet?")

answer = input("Your answer: ")

# Sanitize user input
answer = answer.strip().lower()

if answer == "mars":
    print("Correct! Excellent work.\n")
    score += 1

else:
    print("Incorrect! The correct answer is Mars.\n")


# -----------------------------------
# QUESTION 3
# -----------------------------------

print("Question 3:")
print("How many countries are there in the world?")

answer = input("Your answer: ")

# Sanitize user input
answer = answer.strip().lower()

if answer == "195" or answer == "one hundred ninety five":
    print("Correct! Great job.\n")
    score += 1

else:
    print("Incorrect! The correct answer is 195.\n")


# -----------------------------------
# FINAL RESULTS
# -----------------------------------

print("=" * 45)
print("             QUIZ RESULTS")
print("=" * 45)

print(f"Your Final Score: {score:>2} / 3")

percentage = (score / 3) * 100

print(f"Your Percentage: {percentage:.2f}%")

# Final performance feedback
if score == 3:
    print("Grade: A+")
    print("Outstanding! You answered every question correctly.")

elif score == 2:
    print("Grade: B")
    print("Good job! You have a good knowledge base.")

elif score == 1:
    print("Grade: C")
    print("Not bad! Keep learning and improving.")

else:
    print("Grade: F")
    print("Keep practicing! You can do better next time.")

print("=" * 45)
print("       THANK YOU FOR PLAYING!")
print("=" * 45)