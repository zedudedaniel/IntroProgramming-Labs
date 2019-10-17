#CMPT Intro to Programming
# Lab #5 - Working with strings and functions
# Author: Daniel Mikhalchuk
# Created: 2019-10-17

# I remember doing this one but I guess git push failed :(

def main():
	#get user's first and last names
	first = input("Enter your first name: ")
	last = input("Enter your last name: ")

	#Make a marist-style username for them
	uname = first + "." + last

	#ask user for password
	passwd = input("Make a password for your email.")

	while (len(passwd) < 8):
		passwd = input("You need a longer password! 8 characters at least.")
	print("That's a good password")

	print("Account made. Your new email address is", uname+"@marist.edu")

main()
