import random 

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10 
CODE_LENGTH = 4 

def generate_code():
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]

def guess_code():
    while True:
        guess = input("Guess: ").upper().split()
        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        else:   # only runs if we never hit `break`
            return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0 
    incorrect_pos = 0 

    # count how many of each color are in the code
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1 

    # first pass: exact matches
    for g, r in zip(guess, real_code):
        if g == r:
            correct_pos += 1
            color_counts[g] -= 1

    # second pass: right color, wrong place
    for g, r in zip(guess, real_code):
        if g != r and color_counts.get(g, 0) > 0:
            incorrect_pos += 1
            color_counts[g] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to Mastermind! You have {TRIES} tries to guess the code.")
    print("The valid colors are:", *COLORS)

    code = generate_code()

    for attempt in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempt} {'try' if attempt == 1 else 'tries'}!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}")
    else:
        print("You ran out of tries. The code was:", *code)


game()