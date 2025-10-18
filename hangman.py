import random

word_list = ['apple', 'house', 'bread', 'light', 'chair']

secret_word = random.choice(word_list)
guessed_letters = []  # To store letters guessed by the user
tries = 6  # Max incorrect guesses allowed

display_word = ['_' for _ in secret_word]

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

while tries > 0 and '_' in display_word:
    print("Word: " + ' '.join(display_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Tries left: {tries}")
    
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Wrong guess!\n")
        tries -= 1

if '_' not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Out of tries! The word was:", secret_word)
