
def printCurrentMessageMarker(startOfMessageMarkerLength, startOfMessageMarker):
    for k in range(0, startOfMessageMarkerLength):
        print(datastream[startOfMessageMarker + k], end='')
    

def decodeMessage(datastream, startOfMessageMarkerLength):
    for i in range(0, len(datastream) - 4):
        listOfMessageMarker = []
        for j in range(0, startOfMessageMarkerLength):
            listOfMessageMarker.append(datastream[i + j])

        duplicateCounter = 0
        for j in range(0, len(listOfMessageMarker)):
            if(listOfMessageMarker[j] in listOfMessageMarker[j+1:len(listOfMessageMarker)]):
                duplicateCounter += 1
                
        if(duplicateCounter < 1):
            printCurrentMessageMarker(startOfMessageMarkerLength, i)

            print()
            print(i + startOfMessageMarkerLength)
            break


with open("input.txt", 'r') as f:

    datastream = f.readline()
    decodeMessage(datastream, 14)


