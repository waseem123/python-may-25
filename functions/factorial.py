def factorial(n):
    f = 1
    for i in range(1,n+1):
        f = f * i
    return f

print(factorial(5))

n = int(input("ENTER A NUMBER - "))
print(factorial(n))