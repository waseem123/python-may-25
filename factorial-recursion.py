# 5! = 5*4*3*2*1
#     = 5*4!
# 4! = 4*3!
# 3! = 3*2!
# 2=2*1!
# 1! = 1
# n! = n*(n-1)!

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# 5 * factorial(4) #120
# 4 * factorial(3) #24
# 3 * factorial(2) #6
# 2  * factorial(1) #2
# 1 #1