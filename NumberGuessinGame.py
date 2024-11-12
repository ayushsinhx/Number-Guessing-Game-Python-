import random
Lowest_num=1
Highest_num=100
answer=random.randint(Lowest_num, Highest_num)
guesses=0
is_running=True
print("Python Number Guessing Game")
print(f"Select a Number Between {Lowest_num} and {Highest_num}")
while is_running:
    guess=input("Enter Your Guess: ")
    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess<Lowest_num or guess>Highest_num:
            print("That Number Is Out Of Range")
            print(f"Please Select a Number Between {Lowest_num} and {Highest_num}")
        elif guess<answer:
            print("Too Low! Try Again!")
        elif guess>answer:
            print("Too High! Try Again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number Of Guessess: {guesses}")
            is_running=False

    else:
        print("Invalid Guess")
        print(f"Please Select a Number Between {Lowest_num} and {Highest_num}")
