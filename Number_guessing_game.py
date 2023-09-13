import random
import time
from os import system

MAX_ATTEMPTS = 5
MIN_NUMBER = 1
MAX_NUMBER = 100


def introduce() -> None:
    """Introduces player to the rules of the game."""
    print("You will get a total of 10 guesses.")
    time.sleep(2)
    print("In 10 guesses you have to guess the correct no. between 1 to 50.")
    time.sleep(2)
    print("READY???")
    for count in range(1, 4):
        print(count)
        time.sleep(1)
    print("GO")
    time.sleep(1)
    system("cls")

def play_number_guessing_game() -> None:
    """
    Plays the number guessing game.
    
    A random number is generated between MIN_NUMBER and MAX_NUMBER.

    The player is prompted to guess the number within a limited number of attempts.
    Feedback is provided after each guess.
    
    The game ends when the player guesses the correct number or exhausts all attempts.
    """
    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    guess_list = []

    introduce()
    attempt = 1
    while attempt != (MAX_ATTEMPTS + 1):
        try:
            guess = int(input("Guess a no.:"))

        except ValueError:
            print("Enter a valid number!!")
            continue

        if guess == num:
            print(f"\n\nYou got it right in {attempt} attempts.\nThe no. is {num}")
            return
        elif guess in guess_list:
            print("You already guessed this no. before!")
        elif guess > num:
            print(f"The no. is less than {guess}")
            attempt += 1
            print(11-attempt,"Attempts left")
        elif guess < num:
            print(f"The no. is greater than {guess}")
            attempt += 1
            print(11-attempt,"Attempts left")
        guess_list.append(guess)

    if attempt>=10:
        system("cls")
        print("GAME OVER")
        print("The correct no. was",num)

if __name__ == "__main__":
    play_number_guessing_game()