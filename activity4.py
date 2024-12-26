num = int(input("Enter a number: "))
#t_digit = total digits
t_digit = 0
temp = num
while temp > 0:
   temp //= 10
   t_digit += 1
print("\nTotal number of digits in the number:", t_digit)