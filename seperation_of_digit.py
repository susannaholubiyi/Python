digit = int(input("Enter a five digit number"))


first_digit =  (digit // 10000) 




second_digit = (digit % 10000) //1000




third_digit =(digit % 1000) //100




fourth_digit = (digit % 100)//10



fifth_digit = (digit % 10)



print(f"{first_digit}   {second_digit}   {third_digit}   {fourth_digit}   {fifth_digit}")