import random as r

def choose_word():
    words = ["Arpan", "Singh", "Jarvis", "Syntax", "hosting"]
    return r.choice(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter.lower() in guessed_letters else '_' for letter in word])

def play_again():
    while True:
        response = input("Do you want to play again? (y/n): ").lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def hangman():
    while True:
        word_to_guess = choose_word()
        guessed_letters = []
        attempts = 6
        print("\nWelcome to Hangman game made by Arpan Singh.")
        while attempts > 0:
            print("\nAttempts left:", attempts)
            current_display = display_word(word_to_guess, guessed_letters)
            print("Current Word:", current_display)
            guess = input("Enter a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Enter a valid single letter.")
                continue
            if guess in guessed_letters:
                print("You've already guessed that letter.")
                continue
            guessed_letters.append(guess)
            if guess not in word_to_guess.lower():
                attempts -= 1
                print("Incorrect. Try again.")
            else:
                print("Good guess!")
            if set(word_to_guess.lower()) == set(guessed_letters):
                print("\nCongratulations! You guessed the word. It was:", word_to_guess)
                break
        if attempts == 0:
            print("\nYou ran out of attempts. The correct word was:", word_to_guess)
        if not play_again():
            break
if __name__ == "__main__":
    hangman()