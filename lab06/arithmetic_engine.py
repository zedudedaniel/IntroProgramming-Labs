#CMPT 120 - Lab 06
#Daniel Mikhalchuk
# 10-24-2019

def show_intro():
	print("Welcome to the Arithmetic engine!")
	print("==========================\n")
	print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

def show_outro():
	print("\nThank you for using the Arithmetic Engine!")
	print("\nPlease come back again soon!")

def do_loop():
	while True:
		cmd = (input("What computation do you want to perform?: ")).lower()
		

		if cmd == "quit":
			break
		elif (cmd != "add" and cmd != "sub" and cmd!= "mult" and cmd != "div"):
			print(cmd + " is not a valid command.")
			continue

		num1 = int(input("Enter the first number: "))
		num2 = int(input("Enter the second number: "))

		result = calculate(num1, cmd, num2)
		print("The result is: " + str(result) + "\n")

def calculate(num1, cmd, num2):
	if cmd == "add":
		return (num1 + num2)
	elif cmd == "sub":
		return (num1 - num2)
	elif cmd == "mult":
		return (num1 * num2)
	elif cmd == "div":
		if num2 == 0:
			print("Unable to divide by zero!")
			return 0
		return (num1 / num2)

def tryNumbers()

def main():
	show_intro()
	do_loop()
	show_outro()

main()