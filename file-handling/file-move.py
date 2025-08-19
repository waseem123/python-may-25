file_src = input("ENTER SOURCE FILE - ")
file_dst = input("ENTER DESTINATION FILE - ")

# 1. Read the data from source file
myfile = open('D:/python-may-2025/file-handling/'+file_src)
data = myfile.read()
myfile.close()

# 2. Write the data to the destination file
newfile = open('D:/python-may-2025/file-handling/'+file_dst,'w')
newfile.write(data)
newfile.close()

# 3. Write an empty string to the source file
myfile = open('D:/python-may-2025/file-handling/'+file_src,'w')
myfile.write("")
myfile.close()

# 4. Display the succesful message
print('File content moved succesfully')