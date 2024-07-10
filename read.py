file = open("file.txt", "r")

for fil in file.readlines():
    print (fil)

#print(file.read())
#print(file.readable())
#print(file.readline())
#print(file.readlines())
file.close()