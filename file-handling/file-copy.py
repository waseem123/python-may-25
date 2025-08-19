myfile = open('D:/python-may-2025/file-handling/demo.txt')
data = myfile.read()
print(data)
myfile.close()

newfile = open('D:/python-may-2025/file-handling/sample.txt','w')
newfile.write(data)
print('File Copied Succesfully')
newfile.close()
