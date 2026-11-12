#Project 3: Random Password Generator - DecodeLabs Python Internship - 2026

import random
import string


def get_password_length():
    """Ask the user for a valid password length."""

    while True:
        try:
            length = int(input("\nEnter password length (8-256): "))

            if length < 8:
                print("Password must be at least 8 characters long.")

            elif length > 256:
                print("Password cannot be longer than 256 characters.")

            else:
                return length

        except ValueError:
            print("Please enter a valid number.")


def generate_password(length):
    """Generate a random password."""

    # Collect different types of characters.
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    # Combine all characters into one collection.
    all_characters = (
        lowercase_letters +
        uppercase_letters +
        numbers +
        special_characters
    )

    # Start with an empty list.
    password_characters = []

    # Make sure the password contains all character types.
    password_characters.append(random.choice(lowercase_letters))
    password_characters.append(random.choice(uppercase_letters))
    password_characters.append(random.choice(numbers))
    password_characters.append(random.choice(special_characters))

    # Generate the remaining random characters.
    for i in range(length - 4):
        password_characters.append(random.choice(all_characters))

    # Shuffle characters to mix their positions.
    random.shuffle(password_characters)

    # Convert the list into a single password.
    password = "".join(password_characters)

    return password


def main():
    """Run the password generator."""

    print("\n" + "=" * 45)
    print("       RANDOM PASSWORD GENERATOR")
    print("=" * 45)

    print("\nWelcome! Let's create your password.")

    # Step 1 : Get password length.
    password_length = get_password_length()

    # Step 2: Generate the password.
    password = generate_password(password_length)

    # Step 3: Display the generated password.
    print("\n" + "-" * 45)
    print("          PASSWORD GENERATED!")
    print("-" * 45)

    print("\nYour password:", password)

    print("Password length:", len(password), "characters")

    print("\nPassword generated successfully!")

    print("-" * 45)


# Start the program.
if __name__ == "__main__":
    main()
