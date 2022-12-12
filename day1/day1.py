highestElf = 0
secondHighestElf = 0
thirdHighestElf = 0
currentElfTotal = 0

with open('input.txt', 'r') as f:
    
    for line in f:
        if line in ['\n', '\r', '\r\n']:
            if(currentElfTotal > highestElf):
                thirdHighestElf = secondHighestElf
                secondHighestElf = highestElf
                highestElf = currentElfTotal
            elif(currentElfTotal > secondHighestElf):
                thirdHighestElf = secondHighestElf
                secondHighestElf = currentElfTotal
            elif(currentElfTotal > thirdHighestElf):
                thirdHighestElf = currentElfTotal
            print(currentElfTotal)
            currentElfTotal = 0

        else:
            currentElfTotal += int(line)


print(highestElf + secondHighestElf + thirdHighestElf)


