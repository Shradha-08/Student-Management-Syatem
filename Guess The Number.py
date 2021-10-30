import random
number = random.randint(1, 10)
for i in range(0, 3):
    user = int(input("Guess the number:"))
    if user ==  number:
        print("Hurry...!!")
        print("For you guessed the number is right it's {number}")
        break
    elif user > number:
        print("Your guess is too high")
    elif user < number:
        print("Your guess is too low")
    else:
        print("Nice try..!!, but the number is {number}")
        
