import random
import art as a
import words as w

chosen_word = random.choice(w.word_list)
display = ["_" for _ in chosen_word]
lives = 6

print(a.logo)

while "_" in display and lives > 0:
    guess = input("Please guess a letter...\n").lower()

    if guess in display:
        print(f"You have already guessed the letter {guess}")
        continue

    if guess not in chosen_word:
        print(f"{guess} is not in the word, you have lost 1 life.")
        lives -= 1
        print(f"Lives remaining: {lives}")
        print(a.stages[lives])
    else:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess

    print(" ".join(display))

if "_" not in display:
    print("You win!")
else:
    print(f"You lose, the word was {chosen_word}")