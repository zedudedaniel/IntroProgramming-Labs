#Have the user guess the animal
#Keep repeating until they get it correct

def main():
    animal = "Tardigrade"
    while (True):
        guess = input("Guess the animal! ")
        if (guess == animal):
            print("Correct!")
            break
        else:
            print("Incorrect! Try again.")

main()
