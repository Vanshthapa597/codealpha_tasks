
import random 

words = ["python", "laptop", "mobile", "coding" , "Codeaplha"]
word = random.choice(words).lower()

guess_word = ["_"] * len(word)
chance = 6

print("\n.....Welcome to Hangman Game....")

while chance > 0 and "_" in guess_word:

    print("\nWord:", " ".join(guess_word))
    letter = input("Enter a letter: ").lower()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guess_word[i] = letter
        print("Correct!")
    else:
        chance -= 1
        print("Wrong! Chances left:", chance)

if "_" not in guess_word:
    print("\nYou Win!")
    print("Word was:", word)
else:
    print("\nGame Over!")
    print("Correct word:", word)
               