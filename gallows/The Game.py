import random


print("Welcome to the Gallows Game!")
print("Enter number of players:")

players = input()
guessed_word = ""
letter_guess = ""
lives = 6  # some variables
word_length = 0
count = 0

if int(players) == 1:
    file = open("dictionary.txt", "r").read().splitlines()
    guessed_word = random.choice(file)  # random dictionary word
else:
    print("Input guessed word:")
    guessed_word = input()
print(guessed_word)

print("You have " + str(lives) + " lives!")

guessed_word_list = list(guessed_word)
for letter in guessed_word:  # letter counting
    word_length += 1

print("This word a " + str(word_length) + " letter length.")

guess_list = ["-"] * word_length

while guessed_word_list != guess_list and lives > 0:
    print("Enter a letter of guess: ")
    letter_guess = input().capitalize()
    for number_list in range(word_length):
        if letter_guess == guessed_word_list[number_list]:
            del guess_list[number_list]
            guess_list.insert(number_list, letter_guess)
        else:
            count += 1
    if count == word_length:
        lives -= 1
        print("You have " + str(lives) + " lives left!")
    count = 0
    print(guess_list)

if lives > 0:
    print("You win with " + str(lives) + " lives left. That's great!!!")
else:
    print("You lose. Better luck next time:)")
