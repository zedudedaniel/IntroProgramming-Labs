#CMPT Intro to Programming
# Lab #5 - Working with strings and functions
# Author: Daniel Mikhalchuk
# Created: 2019-10-17

# I remember doing this one but I guess git push failed :(

def main():
	names = getNames()

	uname = makeName(names)
	passwd = makePass()
	print("Account made. Your new email address is", uname.lower()+"@marist.edu")
	

def getNames():
	#get user's first and last names
	first = input("Enter your first name: ")
	last = input("Enter your last name: ")
	names = [first,last]
	return names

def makeName(names):
	return names[0] + "." + names[1]

def makePass():
	#ask user for password
	passwd = input("Make a password for your email. ")

	while (PassStrength(passwd) == False):
		passwd = input("You need a better password! 8 characters at least, one upper and one lowercase! ")
	print("That's a good password.")

	return passwd

def PassStrength(passwd):
		if (len(passwd) < 8):
			return False
		if (passwd.lower() == passwd):
			return False
		if (passwd.upper() == passwd):
			return False
		return True

main()
