# Random Password Generator

A command-line Python program that generates a random password containing lowercase letters, uppercase letters, digits, and special characters.

## Features

- Choose a password length from 8 to 256 characters
- Includes at least one character from each supported character type
- Randomizes the character order before displaying the password
- Reports the generated password and its length

## Run

From this folder, run:

```bash
python password_generator.py
```

Enter a password length when prompted. The program uses Python's `random` module and is intended for this project; use a cryptographically secure generator for passwords protecting sensitive accounts.
