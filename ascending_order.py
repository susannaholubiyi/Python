first_number = float(input("Enter first number: "))

second_number = float(input("Enter second number: "))

third_number = float(input("Enter third number: "))



if first_number < second_number:
	if second_number < third_number:
		print(first_number,second_number,third_number)


if first_number < third_number:
	if third_number < second_number:
		print(first_number, third_number, second_number)


if second_number < first_number:
	if first_number < third_number:
		print (second_number, first_number, third_number)


if second_number < third_number:
	if third_number <first_number:
		print(second_number, third_number, first_number)


if third_number < first_number:
	if first_number < second_number:
		print(third_number, first_number, second_number)


if third_number < second_number:
	if second_number < first_number:
		print(third_number,  second_number,  first_number)