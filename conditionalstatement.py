#Write a script that takes a number as input 
#Prints  out a statement that indicates whether the number is even is or odd 

#Ask the user to input a number 
number = int(input("Enter a number: "))

#Check if the number is even or odd 

if number %2 == 0: 
	print(f"{number} is even.")

else:
	print(f"{number} is odd.")
