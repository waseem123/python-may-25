isprime = True
N = int(input("ENTER A NUMBER - "))
r = N // 2
for i in range(2,r):
    if N % i == 0:
        isprime = False
        break
    
if isprime == True:
    print(f'{N} IS A PRIME NUMBER')
else:
    print(f'{N} IS NOT A PRIME NUMBER')