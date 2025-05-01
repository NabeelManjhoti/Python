import random

def guessUser(a):
    low = 1
    high = a
    feedback = ''
    attempts = 0
    while feedback != 'c':
        guess = random.randint(low, high)
        attempts += 1
        print("\nDeveloped by: Nabeel Ali\n")
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback =='h':
            high = guess -1
        elif feedback == 'l':
            low = guess +1
    
    print(f"\nYay! The computer guessed your number, {guess}, correctly! It took {attempts} attempts.")
    print("Thank you for playing!")

guessUser(100)
    