#!/usr/bin/env python3

print("Welcome to Python Pizza Deliveries! 🍕")
size= input("What size pizza do you want? S, M, L? ")
add_pepperoni = input("would you like pepperoni? Y or N ")
add_cheese = input("would you like some cheese? Y or N ")

bill = 0

if size == "S" or "s":
	bill += 15
	if add_pepperoni == "Y" or "y":
		bill +=2
		if add_cheese == "N" or "n":
			bill += 3
			
elif size == "M" or "m":
	bill += 20
	if add_pepperoni == "Y" or "y":
		bill +=3
		if add_cheese == "N" or "n":
			bill += 3
			
elif size == "L" or "l":
	bill += 25
	if add_pepperoni == "Y" or "y":
		bill +=4
		if add_cheese == "N" or "n":
			bill += 3

print(f"Your final bill is £{bill}")

	#else:
	#print("Sorry no pizza for you😕")