n = int(input("ENTER A NUMBER - "))
digits = 0
temp = n

# Step 1 - Counting the digits as d
while temp!=0:
    digits += 1
    temp //= 10
    
print(digits)
temp = n

# Step 2 - 
# a. Separating the digit
# b. Calculate the raise to power of that digit to d 
# c. Perform summation of all the resulting values and store in sum
sum = 0
rem = 0
while temp!=0:
    rem = temp%10
    sum = sum+(rem ** digits)
    temp //= 10
    
print(sum)


# Step 3 - Compare the value of sum with n. If matched then n is Armstrong else not
if n == sum:
    print(f'{n} is an ARMSTRONG number')
else:
    print(f'{n} is NOT an ARMSTRONG number')