file = open('file.txt', 'r')
f = file.readlines()

print(f)

newList = []
for line in f:
    # to remove \n
#    if line[-1]=='\n':
#        newList.append(line[:-1])
#    else:
#        newList.append(line)
#to remove \n
    newList.append(line.strip())
print(newList)
