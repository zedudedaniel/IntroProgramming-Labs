#Have the user guess the animal
#Keep repeating until they get it correct

def main():
    animal = "tardigrade"
    while (True):
        guess = input("Guess the animal! ").lower()
        if (guess[0] == "q"):
            print("Seeya!")
            break
        elif (guess == animal):
            print("Correct!")
            likeanimal = input("Do you like them? y/n ").lower()
            if (likeanimal == "y"):
                print("I see you are a man of culture as well.")
            else:
                print("Thomas has never seen such bullshit before.")
            break
        else:
            print("Incorrect! Try again.")

main()
