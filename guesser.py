import random

print("Hello, user!\nThat's a number guess game. Shall we start? (Y/N)")

answer = input()

if answer.lower() == "y":
    print("Let's start!")
    print("Guess my number! It's between 1 and 100")
    randomNum = random.randint(1, 100)
    
    while True:
        userNum = int(input())
        if userNum > randomNum:
            print("No, my number is smaller. Try again:")
        elif userNum < randomNum:
            print("No, my number is bigger. Try again:")
        else:
            print(f"Yes! My number is {randomNum}")
            break
else:
    print("Goodbye then!")