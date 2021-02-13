import random
winning_number=random.randint(0,100)
user_number=int(input("Guess a number between 0 and 100 :"))
guess_num=0
while True:
    if winning_number == user_number:
        print(f"You win!!,you guessed this number in {guess_num}")
        break
    else:
        if winning_number < user_number:
            print("Too High")
        else:
            print("Too low")
        guess_num+=1
        user_number=int(int(input("Enter again :")))