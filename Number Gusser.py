import random
low = 1
high = 50

correct_answer = int(random.randrange(low, high + 1))

chances = 5

print(f"Guess a number between {low} and {high}. You have {chances} chances.")

for attempt in range(1, chances + 1):

    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess < correct_answer:
        print("Correct answer is greater!")
    elif guess > correct_answer:
        print("Correct answer is smaller!")
    else:
        print("You Win!")
        break
else:
    print("You lose! The correct answer was:", correct_answer)
