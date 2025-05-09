import random

# you could also use randrange instead of randint just want include the y part of the bracket
# r = (random.randrange(0, 100))
# print(r)

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0: 
        print("Please type a number larger than 0 next time")
        quit()
    

else: 
    print("Please type in a number")
    quit()

random_number = random.randint(0,top_of_range)

guesses = 0 

while True: 

    guesses += 1 
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(top_of_range)
    
    else: 
        print("Please type in a number next time. ")
        continue
    
    if user_guess == random_number:
        print("You got it Right")
        break
    elif user_guess > random_number: 
        print("you were above the random number")
    else:
        print("You were below the number")

print("You got it in", guesses, "guesses")
    # you can also do print("You got it in " + str(guesses) + " guesses")