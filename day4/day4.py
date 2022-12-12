#every section has a unique ID num
#each elf is assigned a range of section IDs
#Many assignments overlap
#elves pair up and make a list of assignments for each pair

#Get the range of each elf in the pair
#See which elf has the largest range
#check to the if the smaller range is within the larger range
    #could be done by
        #checking the lower bound is >= big range lower bound
        #and the upper bound is <= big range upper bound


#PART2
#Find the pairs where any number over laps at all



total = 0

totalOverlapAtAll = 0

with open("day4.txt", 'r') as f:
    for line in f:
        splitLine = line.split(',')
        
        elf1 = splitLine[0]
        elf2 = splitLine[1]

        elf1Split = elf1.split('-')
        elf1LowerRange = int(elf1Split[0])
        elf1UpperRange = int(elf1Split[1])

        elf2Split = elf2.split('-')
        elf2LowerRange = int(elf2Split[0])
        elf2UpperRange = int(elf2Split[1])

        elf1TotalRange = elf1UpperRange - elf1LowerRange
        elf2TotalRange = elf2UpperRange - elf2LowerRange

        print("elf1 range " + 
                str(elf1LowerRange) + 
                " - " + 
                str(elf1UpperRange))

        print("elf1 total range: " + str(elf1TotalRange))

        print("elf2 range " + 
                str(elf2LowerRange) + 
                " - " + 
                str(elf2UpperRange))

        print("elf2 total range: " + str(elf2TotalRange))

        if(elf1TotalRange > elf2TotalRange):
        
            if(elf2LowerRange >= elf1LowerRange and elf2UpperRange <= elf1UpperRange):
                total += 1    
                print("elf2 in elf1 range")      
        
        elif(elf1TotalRange < elf2TotalRange):
            
            if(elf1LowerRange >= elf2LowerRange and elf1UpperRange <= elf2UpperRange):
                total += 1
                print("elf1 in elf2 range")  

        elif(elf1TotalRange == elf2TotalRange):
            if(elf1LowerRange == elf2LowerRange and elf1UpperRange == elf2UpperRange):
                total += 1
                print("Equal Range")


        if(elf1TotalRange == 0):
            l = [elf1LowerRange]
            elf1set = set(l)
        else:
            elf1set = set(list(range(elf1LowerRange, elf1UpperRange + 1)))
        
        if(elf2TotalRange == 0):
            l = [elf2LowerRange]
            elf2set = set(l)
        else:
            elf2set = set(list(range(elf2LowerRange, elf2UpperRange + 1)))
        
        
        #elf2set = set(list(range(elf2LowerRange, elf2UpperRange)))
        print(elf1set)
        print(elf2set)
        if(elf1set & elf2set):
        
            print(True)
            totalOverlapAtAll += 1
            print(elf1set & elf2set)
        else:
            print(False)
        
        

print("total overlap completely = " + str(total))      
print("total overlap at all = " + str(totalOverlapAtAll))

       