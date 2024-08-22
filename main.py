import random

def guess_the_number():
    target_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        attempts += 1
        
    
        guess = int(input("Guess the number (between 1 and 100): "))
        
        
        if guess > target_number:
            difference = guess - target_number
            if difference >= 30 :
                print("Too high! Try again.")
            elif difference > 10 and difference < 30:
                print("Just high! Try again.")
            elif difference <= 10:
                print("Almost there! Just a little but high. Try again.")
        elif guess < target_number:
            difference = target_number - guess
            if difference >= 30 :
                print("Too low! Try again.")
            elif difference > 10 and difference < 30:
                print("Just low! Try again.")
            elif difference <= 10:
                print("Almost there! Just a little but low. Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {target_number} in {attempts} attempts.")
            break


guess_the_number()
