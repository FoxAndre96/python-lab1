line = input("Tell me something: ")

cutString = line[0:2] + line[len(line)-2:len(line)]

print(cutString)