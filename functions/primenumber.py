def isprime(n):
    for i in range(2,n): #(2,3,4,5,6)
        if n%i==0:
            return False
    return True

num = int(input("ENTER A NUMBER - "))
print(isprime(num))


# 0,1,1,2,3,5,8,13......