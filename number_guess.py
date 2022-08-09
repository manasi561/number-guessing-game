#Version1 - Basic program with one attempt


correct_num = 6

while True:
    user_guess = int(input("What is your guess? "))
    
    if user_guess == correct_num:
        print("Your Answer is correct")
        break
    else:
        print("Sorry your guess is incorrect")
        break
        
# Version 2

#import required packages

import random 
random.randint(1, 100)

#assign variables
 
lower_bound = 1
upper_bound = 100
guess_counter = 0
guess_remaining = 5

#Store the randomly generated num
correct_number = random.randint(1, 100)

print(f"Guess the num between {lower_bound} and {upper_bound}. You have {guess_remaining} chances")


while True:
    user_guess = int(input("Enter your guess: "))
    guess_counter += 1
    guess_remaining = guess_remaining-1
    
    if lower_bound <= user_guess <= upper_bound:
        if user_guess == correct_number:
            print(f"Congrats! You got it in {guess_counter} guess")
            break
        
        elif user_guess < correct_number:
            print(f"Your guess is too low, try again! Guess remaining: {guess_remaining}")
        
        else:
            print(f"Your guess is too high, try again! Guess remaining: {guess_remaining}")
            
            
    else:
        print(f"Your guess is out of range. Please select a number between {lower_bound} and {upper_bound}. Guess remaining: {guess_remaining}")
        
        
    if guess_remaining == 0:
        print(f"Sorry you are out of guesses. Correct number is {correct_number}")
        break