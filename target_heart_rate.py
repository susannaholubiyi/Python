age_in_years = float(input("Enter your age: "))

maximum_heart_rate = 220 - age_in_years

min_target_heart_rate = 0.5 * maximum_heart_rate

max_target_heart_rate = 0.85 * maximum_heart_rate


print (f"Your target heart rate is {min_target_heart_rate} to {max_target_heart_rate}")