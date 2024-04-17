import random

def guess(x):
    low = 1
    high = x
    feedback = " "
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (h), too low (l), correct (c)? ')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'YAY! The computer guessed your number {guess} correctly!')

guess(100)
