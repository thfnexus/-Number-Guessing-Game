"""
📄 Project: Number Guessing Game
👨‍💻 Created by: Hashir Adnan
🌐 Website: www.techthf.xyz
🗓️ Date: [Insert today's date]

🧠 Description:
This is a simple number guessing game where the computer randomly selects a number between 1 and 100.
The player must guess the number in the least possible attempts. The game gives feedback whether to guess higher or lower.

📦 Features:
- Random number generation between 1 and 100
- User input for guesses
- Feedback for higher/lower guesses
- Tracks number of attempts

💡 How to Use:
1. Run the program.
2. Enter your guess when prompted.
3. The program will let you know if your guess is higher or lower.
4. Once you guess the number correctly, it will display the number of attempts taken.

✅ Example:
Input: 45
Output: "Lower number please"
"""

import random

n = random.randint(1, 100)
a = -1
guesses = 1

while a != n:
    try:
        a = int(input("Guess the number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue  # Skips the rest of the loop and asks for a valid number again

    if a > n:
        print("Lower number please")
        guesses += 1
    elif a < n:
        print("Higher number Please")
        guesses += 1

print(f"You have guessed the number {n} correctly in {guesses} attempts")
