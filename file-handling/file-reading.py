myfile = open("D:/python-may-2025/file-handling/demo.txt","r")
# Full file reading
# data = myfile.read()
# print(data)

# line by line reading
# print(myfile.readline())
# print(myfile.readline())
# print(myfile.readline())

# reading all lines of file one-by-one using for-in loop
# for i in myfile:
#     print(i)

data = myfile.readlines()
print(data)
for i in range(0,5):
    print(data[i])

