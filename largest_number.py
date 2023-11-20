first_number=int(input("Enter first number: "))

second_number= int(input("Enter second number: "))

third_number= int(input("Enter third number"))


if first_number> second_number and second_number> third_number:
	print("heighest number is", first_number)

if first_number>third_number and third_number>second_number:
	print("heighest number is: ", first_number)

if second_number>first_number and first_number>third_number:
	print("heighest number is", second_number)

if second_number> second_number and second_number> first_number:
	print("heighest number is", second_number)

if third_number>first_number and first_number> second_number:
	print("heighest number is: ", third_number)

if third_number>second_number and second_number>first_number:
	print("heighest number is: ", third_number)
