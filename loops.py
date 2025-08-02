import random
secret_number = random.randint(1,100)
print("я загадал число от 1 до 100. Попробуй угадать!")
while True:
    guess = int(input("введи число: "))
    if guess < secret_number:
        print("слишком маленькое!")
    elif guess > secret_number:
        print("слишком большое!")
    else:
        print("поздравляю! Ты угадал число!")
        break































































