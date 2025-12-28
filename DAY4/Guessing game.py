correct = 5
guess = None
while guess != correct:
    guess = int(input("Guess a nummber:"))
    if guess != correct:
        print("Try again")
print("Correct number") 
