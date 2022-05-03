# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 21:21:28 2022

@author: morga
"""


import random
import math
import numpy as np
import random
from sympy import *
 
#a = random.randint(2, 10)



def calculateNumberOfBits(n):


  # These two are the same
  bits = int(math.log2(n)) + 1
  bits = math.floor(math.log2(n))



  #bits = int(math.log2(2**1024)) + 1
  #print(bits)
  
 
    

  
  
  
def millerRabin(candidate, security):

  if candidate == 2 or candidate == 3:

    return True                                           

  if candidate % 2 == 0:

    return False

  exponent = 0
  pMinus1 = candidate - 1
  #r, s = 0, candidate - 1
  print('Miller Rabin, Prime Candidate - 1: ' + str(pMinus1))
  while pMinus1 % 2 == 0:
    
    exponent += 1
    pMinus1 //= 2

  #print('pMin1: ' + str(pMinus1))

  for _ in range(security):
      
    #a = random.randint(2, 10)

    #a = random.randrange(2, (candidate - 1))

    a = random.randint(2, (candidate-1))

    ## THERE IS A FASTER WAY TO DO THIS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    #x = (exp_func(a, pMinus1)) % candidate
    x = pow(a, pMinus1, candidate) # = to (a^pMinus1) mod candidate
    
    if x == 1 or x == candidate - 1:

        continue
    
    for _ in range(exponent - 1):

        ## THERE IS A FASTER WAY TO DO THIS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        #x = (exp_func(x, 2)) % candidate
        x = pow(x, 2, candidate)
        
        if x == candidate - 1:
        
            break
    
    else:
    
        return False
  
  return True








def randN(min, max):

  #min = pow(10, n-1)
  #max = pow(10, n) - 1
  theRandom = random.randint(min, max)
  print('The Random: ' + str(theRandom))
  theRandomString = str(theRandom)
  lastNumber = theRandomString[-1]
  print('Last Number: ' + lastNumber)
  print('MINIMUM: ' + str(min))
  print('MAXIMUM: ' + str(max))


  if ((theRandomString[-1] == '1') and (len(theRandomString) == 1)):

    return(randN(min, max))

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







def findNumberOfTestsAndBitLengthAndProbability(base, exponent):

  #base = 2

  #exponent = 1024


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
  print('Probability: ' + str(probability))

  #print(1/355)

  return reducedDenominator








def LargePrimeGenerator(exponent):

  # Define base = 2 for binary
  base = 2
  # Define the bit size of prime number you want with exponent size
  # Change this to change the bit size of your prime
  # exponent = 8

  # This number tells you the number of iterations for generating numbers to find a prime
  testNumber = int(findNumberOfTestsAndBitLengthAndProbability(base, exponent))

  # This gives you a tuple (min, max)
  minAndMaxTuple = createMinAndMaxForRandomGenerator(exponent)

  # Minimum for bit size you defined above
  min = minAndMaxTuple[0]

  # Maximum for bit size you defined above
  max = minAndMaxTuple[1]

  for i in range(0, testNumber*4):

    print('MINIMUM: ' + str(min))
    print('MAXIMUM: ' + str(max))
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
  return candidate






 
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)
 
# Generating large random numbers
def gen_key(q):
 
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
 
    return key
 
# Modular exponentiation
def power(a, b, c):
    x = 1
    y = a
 
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
 
    return x % c
 
# Asymmetric encryption
def encrypt(msg, q, h, g):
 
    en_msg = []
 
    k = gen_key(q)# Private key for sender
    s = power(h, k, q)
    p = power(g, k, q)
     
    for i in range(0, len(msg)):
        en_msg.append(msg[i])
 
    print("g^k used : ", p)
    print("g^ak used : ", s)
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])
 
    return en_msg, p
 
def decrypt(en_msg, p, key, q):
 
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i]/h)))
         
    return dr_msg
 
# Driver code
def main(msg):
 
    #msg = 'The enemy is coming!'
    print("Original Message :", msg)
    
    q = LargePrimeGenerator(1024)
    #q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)
 
    key = gen_key(q)# Private key for receiver
    h = power(g, key, q)
    print("g used : ", g)
    print("g^a used : ", h)
    
    
    PrivateKey = key
    PublicKey = (q, h, g)
    en_msg, p = encrypt(msg, q, h, g)
    cipher = en_msg
    dr_msg = decrypt(en_msg, p, key, q)
    dmsg = ''.join(dr_msg)
    decrypted = dmsg
    print("Decrypted Message :", dmsg);
    
    return cipher, decrypted, PrivateKey, PublicKey 
 
main('Hello')