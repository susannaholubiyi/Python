cost_of_car = eval(input("Enter the price of your car to know your tax: "))

if cost_of_car < 1000000:
	ten_percent = 1000000 *0.10

	print(ten_percent)

elif cost_of_car >= 1000000 and cost_of_car<3000000:
	fiften_percent = cost_of_car * 0.15
	print(fiften_percent)

elif cost_of_car >=3000000 and cost_of_car < 5000000:
	twenty_percent = cost_of_car * 0.20
	print(twenty_percent)

elif cost_of_car >=5000000:
	thirty_percent = cost_of_car * 0.30
	print(thirty_percent)