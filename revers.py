n = int(input("ENTER A NUMBER - "))
temp = n
rem = 0
reverse = 0

while temp!=0:
    rem = temp % 10 #9
    reverse = (reverse * 10) + rem # (758*10) + 9 = 7589
    temp = temp // 10 #0
    
print(f'REVERSE OF {n} IS {reverse}')

if reverse==n:
    print(f'{n} IS PALINDROME NUMBER')
else:
    print(f'{n} IS NOT A PALINDROME NUMBER')