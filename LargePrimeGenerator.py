# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:18:11 2022

@author: morga
"""

import math
import numpy as np
import random

# Find nunmber of bits in a number

def calculateNumberOfBits(n):


  # These two are the same
  bits = int(math.log2(n)) + 1
  bits = math.floor(math.log2(n))



  #bits = int(math.log2(2**1024)) + 1
  #print(bits)
  return bits




def findNumberOfTestsAndBitLengthAndProbability(base, exponent):

  base = 2

  exponent = 1024


  x = np.log(base)
  print(x)

  fleshedOutDenominator = math.ceil(exponent * x)
  print(fleshedOutDenominator)

  # Test Number; Amount of random ODD numbers you have to test before you have a prime
  # at bit length of exponent; exponent = bit length of prime you want
  reducedDenominator = fleshedOutDenominator/2
  print(reducedDenominator)

  reducedBase = base * 0.5


  probability = reducedBase/reducedDenominator
  print(probability)

  print(1/355)

  return reducedDenominator





def randN(min, max):

  #min = pow(10, n-1)
  #max = pow(10, n) - 1
  theRandom = random.randint(min, max)
  print('The Random: ' + str(theRandom))
  theRandomString = str(theRandom)
  lastNumber = theRandomString[-1]
  print('Last Number: ' + lastNumber)


  if (theRandomString[-1] == '1'):

    print('Candidate = ' + str(theRandom))
    return theRandom

  elif (theRandomString[-1] == '3'):
    
    print('Candidate = ' + str(theRandom))
    return theRandom

  elif (theRandomString[-1] == '7'):
    
    print('Candidate = ' + str(theRandom))
    return theRandom 

  elif (theRandomString[-1] == '9'):
    
    print('Candidate = ' + str(theRandom))
    return theRandom

  else:

    return randN(min, max)





# Generate a random number of a specified bit length

def createMinAndMaxForRandomGenerator(exponent):

  minBin = '0b1'

  for i in range(0, exponent-1):

    minBin = minBin + '0'

  print(minBin)

  binaryLength = len(minBin)
  print(binaryLength)

  maxBin = '0b1'

  for i in range(0, exponent-1):

    maxBin = maxBin + '1'

  print(maxBin)

  binaryLength2 = len(maxBin)
  print(binaryLength2)


  minBinToDecimal = int(minBin, 2)
  print('MinBinToDecimal: ' + str(minBinToDecimal))

  maxBinToDecimal = int(maxBin, 2)
  print('MaxBinToDecimal: ' + str(maxBinToDecimal))


  print(calculateNumberOfBits(minBinToDecimal))
  print(calculateNumberOfBits(maxBinToDecimal))

  return (minBinToDecimal, maxBinToDecimal)




#numberLength = binaryLength
#print(numberLength)



#t = randN(minBinToDecimal, maxBinToDecimal+10)
#t = randN(numberLength)

#print('t: ' + str(t))

#w = calculateNumberOfBits(t)




def millerRabin(candidate, security):

  if candidate == 2 or candidate == 3:

    return True                                           

  if candidate % 2 == 0:

    return False

  exponent = 0
  pMinus1 = candidate - 1
  #r, s = 0, candidate - 1

  while pMinus1 % 2 == 0:
    
    exponent += 1
    pMinus1 //= 2

  #print('pMin1: ' + str(pMinus1))

  for _ in range(security):

    a = random.randrange(2, candidate - 1)
    x = pow(a, pMinus1, candidate) # = to (a^pMinus1) mod candidate
    
    if x == 1 or x == candidate - 1:

        continue
    
    for _ in range(exponent - 1):

        x = pow(x, 2, candidate)
        
        if x == candidate - 1:
        
            break
    
    else:
    
        return False
  
  return True




def main():

  # Define base = 2 for binary
  base = 2
  
  
  # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  # Define the bit size of prime number you want with exponent size
  # Change this to change the bit size of your prime
  exponent = 1024

  # This number tells you the number of iterations for generating numbers to find a prime
  testNumber = int(findNumberOfTestsAndBitLengthAndProbability(base, exponent))

  # This gives you a tuple (min, max)
  minAndMaxTuple = createMinAndMaxForRandomGenerator(exponent)

  # Minimum for bit size you defined above
  min = minAndMaxTuple[0]

  # Maximum for bit size you defined above
  max = minAndMaxTuple[1]

  for i in range(0, testNumber*4):

    # A Random Number that is the bit size you requested
    randomNumber = randN(min, max)

    # Print Iteration
    print(str(i) + '. ')

    

    # Define number of different a's to test the primality of your randomly generated number
    security = 40

    # Assign your random number to candidate
    candidate = randomNumber

    # Call Miller Rabin and test your random numbers until you find a viable candidate
    determination = millerRabin(candidate, security)
    print(determination)

    if (determination == True):
      
      # Prime Number has been found!
      print('Prime Number has been found!')

      # Print the Random Number you generated
      print('Prime Number: ' + str(candidate))

      # Print the bit size of the random number you generated
      print('Number Of Bits: ' + str(calculateNumberOfBits(candidate)))

      break

    else:

      continue

  print('Congratulations!')

main()