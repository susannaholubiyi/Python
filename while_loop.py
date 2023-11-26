score = float(input("Enter score"))

total = 0

count = 1 

while score != -1:

	total += score
	count += 1
	score = float(input ("Enter scores: "))

average = total / count
print ("The average is ", average)

if count == 1:
    print("No score was entered")