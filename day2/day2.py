
# 'A' and 'X' == Rock
# 'B' and 'Y' == Paper
# 'C' and 'Z' == Scissors

"""Choices for my score
X - A - Draw
X - B - Lose
X - C - Win
Y - A - Win
Y - B - Draw
Y - C - Lose
Z - A - Lose
Z - C - Win
Z - Z - Draw
"""
"""
totalPoints = 0
with open ('input.txt', 'r') as f:
   for line in f:
      cleanedLine = line.strip()

      opponentsChoice = cleanedLine[0]
      yourChoice = cleanedLine[2]

      if(yourChoice == 'X'):
         totalPoints += 1
         if(opponentsChoice == 'C'):
            totalPoints += 6
         elif(opponentsChoice == 'A'):
            totalPoints += 3
      elif(yourChoice == 'Y'):
         totalPoints += 2
         if(opponentsChoice == 'A'):
            totalPoints += 6
         elif(opponentsChoice == 'B'):
            totalPoints += 3
      elif(yourChoice == 'Z'):
         totalPoints += 3
         if(opponentsChoice == 'B'):
            totalPoints += 6
         elif(opponentsChoice == 'C'):
            totalPoints += 3
      
print(totalPoints)
"""
totalPoints = 0
with open ('input.txt', 'r') as f:
   for line in f:
      cleanedLine = line.strip()

      opponentsChoice = cleanedLine[0]
      yourChoice = cleanedLine[2]

      if(opponentsChoice == 'A'):
         if(yourChoice == 'X'):
            totalPoints += 3
         elif(yourChoice == 'Y'):
            totalPoints += 4
         else:
            totalPoints += 8

      elif(opponentsChoice == 'B'):
         if(yourChoice == 'X'):
            totalPoints += 1
         elif(yourChoice == 'Y'):
            totalPoints += 5
         else:
            totalPoints += 9
      
      elif(opponentsChoice == 'C'):
         if(yourChoice == 'X'):
            totalPoints += 2
         elif(yourChoice == 'Y'):
            totalPoints += 6
         else:
            totalPoints += 7

print(totalPoints)