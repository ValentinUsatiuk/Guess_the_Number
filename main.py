from random import randint
random_number = randint(1,100)
print("Guess the secret number!")
user_number = int(input("Enter a number: "))
while random_number != user_number:
    if user_number > random_number:
        user_number = int(input("The secret number is less than what you entered. Try again:"))
    elif user_number < random_number:
        user_number = int(input("The secret number is greater. Try again!"))

print(f"Correct, the secret number is : {random_number}")