for i in range(1,6):
    for j in range(1,6):
        print("* ",end="")
    print()
print("__________________________")    
for i in range(1,6):
    for j in range(1,6):
        print(i,"",end="")
    print()
print("__________________________")
for i in range(1,6):
    for j in range(1,6):
        print(j,"",end="")
    print()

print("__________________________")
for i in range(1,26):
    print(f'{i:02d}',end=" ")
    if i % 5 == 0:
        print()

print("__________________________")
sum = 0
for i in range(1,6):
    for j in range (1,6):
        sum += 1
        if sum<10:
            print(f'0{sum}',end=" ")
        else:
            print(f'{sum}',end=" ")
    print()
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

# 1 2 3 4 5
# 1 2 3 4 5 
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# 01 02 03 04 05
# 06 07 08 09 10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25

# *
# * *
# * * *
# * * * *
# * * * * *