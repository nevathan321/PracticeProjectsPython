#MastermindGame

import random 

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10 
CODE_LENGTH = 4 

def generate_code():
    code = []


    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    
    return code

code = generate_code()


def guess_code():

    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue


        for color in guess:
            if color not in COLORS: 
                print(f"Invalid color: {color}. Try again")
                break 

            
        else:
            break
             


    return guess 
    


def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0 
    incorrect_pos = 0 

    for color in real_code:
        for color not in color_counts:
            color.counts[color] = 0 
        color_counts[color] += 1 
    
    for guess




 

