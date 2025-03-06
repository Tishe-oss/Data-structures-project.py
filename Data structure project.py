import random  

# List of numbers  
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  

# Randomly choose a number from the list  
chosen_number = random.choice(numbers)  

print("Welcome to the guessing game!")  
print("A number has been chosen from this list: ", numbers)  

# Get user's guess  
try:  
    guessed_number = int(input("Guess the number: "))  
    
    # Compare the guessed number with the chosen number  
    if guessed_number > chosen_number:  
        print("The guessed number is higher than the original.")  
    elif guessed_number < chosen_number:  
        print("The guessed number is smaller than the original.")  
    else:  
        print("Congratulations! You've guessed the correct number.")  
except ValueError:  
    print("Please enter a valid integer.")  