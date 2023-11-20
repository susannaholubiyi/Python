first_number= int(input("Enter first number: "))

second_number= int(input("Enter second number: "))

third_number= int(input("Enter third number: "))


if first_number > second_number:
	
	if first_number> third_number:
	
		print("Heighest number is: ", first_number)

if second_number > first_number:

	if second_number> third_number:

		print("Heighest number is: ", second_number)

if third_number > first_number:

	if third_number > second_number:
	
		print("Heighest number is: ", third_number)