
def getHalfStringLength(string):
    return int(len(string) / 2)


totalPoints = 0



'''
Finds the duplicate items and proritses them
with open('input.txt', 'r') as f:
    for line in f:
        string = line
        halfStringLength = getHalfStringLength(string)
        firstHalf = line[0:halfStringLength]
        secondHalf = line[halfStringLength:]

        for l in firstHalf:
            if(l in secondHalf):
                if(ord(l) >= 97):
                    totalPoints += (ord(l) - 96)
                    print(l + ": " + str(ord(l) - 96))
                else:
                    totalPoints += (ord(l) - 38)
                    print(l + ": " + str(ord(l) - 38))
                break
print(totalPoints)
        
'''

with open('input.txt', 'r') as f:
    
    lineNumber = 0
    for line in f:
        lineNumber += 1
        string = line

        
        if(lineNumber % 3 == 1):
            elf1 = line
        elif(lineNumber % 3 == 2):
            elf2 = line
        elif(lineNumber % 3 == 0):
            elf3 = line

        
        if(lineNumber % 3 == 0):
        
            print(str(lineNumber) + ": "+ elf1)
            print(str(lineNumber) + ": "+ elf2)
            print(str(lineNumber) + ": "+ elf3)

            for letter in elf1:
                if(letter in elf2 and letter in elf3):
                    print("letter " + letter)
                    print("\n")


                    if(ord(letter) >= 97):
                        totalPoints += (ord(letter) - 96)
                        print(letter + ": " + str(ord(letter) - 96))
                    else:
                        totalPoints += (ord(letter) - 38)
                        print(letter + ": " + str(ord(letter) - 38))
                    break

                
print(totalPoints)


