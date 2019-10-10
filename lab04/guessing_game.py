#Have the user guess the animal
#Keep repeating until they get it correct

def main():
    animal = "tardigrade"
    while (True):
        guess = input("Guess the animal! ").lower()
        if (guess == animal):
            print("Correct!")
            break
        elif (guess == "quit"):
            print("Seeya!")
            break
        else:
            print("Incorrect! Try again.")

main()
