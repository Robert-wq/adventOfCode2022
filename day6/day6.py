


with open("input.txt", 'r') as f:

    datastream = f.readline()

    for i in range(0, len(datastream) - 4):
        listOfFour = []
        for j in range(0, 4):
            listOfFour.append(datastream[i + j])

        duplicateCounter = 0
        for j in range(0, len(listOfFour)):
            if(listOfFour[j] in listOfFour[j+1:len(listOfFour)]):
                duplicateCounter += 1
        if(duplicateCounter < 1):
            print(datastream[i] + datastream[i+1] + datastream[i+2]+ datastream[i+3])
            print(i + 4)
            break