# General Knowledge Quiz

A simple command-line quiz application built in Python. It welcomes the user, asks a series of general knowledge questions, checks the answers, calculates the score, and shows a final grade.

## Overview

This project is a beginner-friendly Python quiz game designed to practice:

- user input handling
- loops and conditionals
- answer validation
- score tracking
- replay functionality

The quiz uses a fixed set of multiple-choice questions and runs entirely in the terminal.

## Features

- Personalized greeting with the player's name
- 5 general knowledge questions
- Multiple-choice format: A, B, C, D
- Input validation for invalid answer choices
- Option to quit the quiz at any time
- Final score and percentage calculation
- Grade assignment based on the result
- Ability to play again after finishing a round

## Project file

- `quiz_taker.py` – contains the quiz logic and user interaction flow

## Run the program

From this folder, run:

```bash
python quiz_taker.py
```

Then:

1. Enter your name
2. Answer each question with A, B, C, or D
3. Type `quit` at any time to exit the quiz
4. Choose whether to play again after the result screen

## Example flow

```text
Welcome to the General Knowledge Quiz!
How should we call you? (Name): Alice

Dear Alice!
You will be asked 5 questions. Try to answer them correctly.
Type 'quit' anytime to exit the quiz.
```

## Notes

- This is a small educational project and does not save scores or user data.
- No external libraries are required.
- The quiz questions are hardcoded in the script.

## Learning value

This project demonstrates essential Python programming ideas such as:

- lists and dictionaries
- `for` and `while` loops
- `if/else` decision-making
- string handling with `.strip()` and `.upper()`
- simple user experience design in the terminal
