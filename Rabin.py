# -*- coding: utf-8 -*-
"""Rabin2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kJd1qcVwZa8fRoPTDXgAsHZJSVrMIzpw
"""







import random
import sympy as sym
import numpy as np
import math
debug = 3

def calculateNumberOfBits(n):


              # These two are the same
              bits = int(math.log2(n)) + 1
              #bits = math.floor(math.log2(n))



def millerRabin(candidate, security):

              if candidate == 2 or candidate == 3:

                return True                                           

              if candidate % 2 == 0:

                return False

              exponent = 0
              pMinus1 = candidate - 1
              
              while pMinus1 % 2 == 0:

                exponent += 1
                pMinus1 //= 2


              for _ in range(security):


                a = random.randint(2, (candidate-1))

                ## THERE IS A FASTER WAY TO DO THIS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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


              if ((theRandomString[-1] == '1') and (len(theRandomString) == 1)):

                return(randN(min, max))

              if (theRandomString[-1] == '1'):

                return theRandom

              elif (theRandomString[-1] == '3'):

                return theRandom

              elif (theRandomString[-1] == '7'):

                return theRandom 

              elif (theRandomString[-1] == '9'):

                return theRandom

              else:

                return randN(min, max)






def createMinAndMaxForRandomGenerator(exponent):

              minBin = '0b1'

              for i in range(0, exponent-1):

                minBin = minBin + '0'

              binaryLength = len(minBin)

              maxBin = '0b1'

              for i in range(0, exponent-1):

                maxBin = maxBin + '1'

              binaryLength2 = len(maxBin)


              minBinToDecimal = int(minBin, 2)

              maxBinToDecimal = int(maxBin, 2)


              return (minBinToDecimal, maxBinToDecimal)




def findNumberOfTestsAndBitLengthAndProbability(base, exponent):

              #base = 2

              #exponent = 1024


              x = np.log(base)

              fleshedOutDenominator = math.ceil(exponent * x)

              # Test Number; Amount of random ODD numbers you have to test before you have a prime
              # at bit length of exponent; exponent = bit length of prime you want
              reducedDenominator = fleshedOutDenominator/2

              reducedBase = base * 0.5


              probability = reducedBase/reducedDenominator

              return reducedDenominator








def LargePrimeGeneratorR():

  # Define base = 2 for binary
  base = 2
  # Define the bit size of prime number you want with exponent size
  # Change this to change the bit size of your prime
  # exponent = 8

  # This number tells you the number of iterations for generating numbers to find a prime
  testNumber = 10000

  # Minimum for bit size you defined above
  # 18 0's
  #min = 1000000000000000000
  #min = 10
  #min = 11, 15, breaks - 20
  min = 100000000000
  #max = 12, 16, breaks - 21
  max = 10000000000000000
  # 20 0's
  #max = 10000000000000000000000000
  #max = 1000

  for i in range(0, testNumber*4):

    # A Random Number that is the bit size you requested
    randomNumber = randN(min, max)

    # Print Iteration
    if (debug == 2): print(str(i) + '. ')

    

    # Define number of different a's to test the primality of your randomly generated number
    security = 10000

    # Assign your random number to candidate
    candidate = randomNumber


    # Call Miller Rabin and test your random numbers until you find a viable candidate
    determination = millerRabin(candidate, security)
    if (debug == 2): print(determination)

    if (determination == True):
      
      # Prime Number has been found!
      if (debug == 2): print('Prime Number has been found!')

      # Print the Random Number you generated
      if (debug == 2): print('Prime Number: ' + str(candidate))

      break

    else:

      continue

  print('Congratulations!')
  return candidate



def ExtendedEuclideanAlgorithm(a, b):

  if b > a: 

    a, b = b, a

  if b == a:

    return (a, None)

  # Create a Dictionary for values of r (rewritten)
  rdict = {}

  # Create a List keys after you complete them and add to dictionary and append here,
  # so we can recall last one easily
  lastRList = []

  # Create Symbols to easily manipulate without completely solving
  A = sym.Symbol('A')
  B = sym.Symbol('B')

  # Store copies of original values
  aOriginal = a
  bOriginal = b

  # Store the Symbols in the Dictionary to match with a and b if found
  rdict[str(a)] = A
  rdict[str(b)] = B
  
  # Create a trigger to break loop
  trigger = False

  # Initialize quotient and remainder variables
  q = 0
  r = 1

  # Start loop to begin calculations
  while (trigger == False):

    q = a // b
    r = a % b

    newa = rdict[str(a)]
    newb = rdict[str(b)]

    conclusion = newa - q*(newb)
    if (debug == 2): print(conclusion)
    rdict[str(r)] = conclusion

    if (r == 0):

      trigger = True

      GCD = b

    lastRList.append(str(r))

    a = b
    b = r

  # print the GCD
  if (debug == 2): print(GCD)

  # print the Integer Linear Combination
  if (debug == 2): print(rdict[str(lastRList[-2])])

  # print the coefficients of the Variable A
  coefficient1 = rdict[str(lastRList[-2])].coeff(A)
  print('Coefficient 1: ' + str(coefficient1))
  if (debug == 2): print(rdict[str(lastRList[-2])].coeff(A))

  # print the coefficients of the Variable B
  coefficient2 = rdict[str(lastRList[-2])].coeff(B)
  print('Coefficient 2: ' + str(coefficient2))
  if (debug == 2): print(rdict[str(lastRList[-2])].coeff(B))

  # print the coefficents of the Variable A * the original value of a
  if (debug == 2): print(rdict[str(lastRList[-2])].coeff(A)*aOriginal)

  # print the coefficents of the Variable B * the original value of b
  if (debug == 2): print(rdict[str(lastRList[-2])].coeff(B)*bOriginal)

  # print the value of the two multiplied out added together
  if (debug == 2): print(rdict[str(lastRList[-2])].coeff(A)*aOriginal+rdict[str(lastRList[-2])].coeff(B)*bOriginal)
  
  addedTogether = rdict[str(lastRList[-2])].coeff(A)*aOriginal+rdict[str(lastRList[-2])].coeff(B)*bOriginal

  integerLinearCombination = rdict[str(lastRList[-2])]

  return (coefficient1, coefficient2)

def squareRootAlgorithm1(prime, cipher):

  #checkPrimeFirst = millerRabin(prime, 40)

  r = pow(cipher, int((prime+1)/4), prime)

  print('r: ' + str(r))
  #r = (fermatLittleTheorem(cipher, int((prime+1)/4), prime, 1))

  #primeFactors(int(prime+1)/4)
  #print(primeFactors)
  #r = cipher**(int(prime+1)/4)
  #r = cipher
  print('algo1 r: ' + str(r))

  #if (debug==3): print('algo1 Roots: ' + str(r, -r))

  return(r, -r)

def squareRootAlgorithm2(prime, cipher):

  #checkPrimeFirst = millerRabin(prime, 40)

  d = pow(cipher, int((prime-1)/4),  prime)
  if (debug==3): print('d: ' + str(d))
  #d = (fermatLittleTheorem(cipher, int((prime-1)/4),  prime, 1))
  
  if d == 1:

    r = pow(cipher, int((prime+3)/8),  prime)
    if (debug==3): print('r: ' + str(r))
    #r = (fermatLittleTheorem(cipher, int((prime+3)/8),  prime, 1))

    return (r, -r)

  elif d == (prime - 1):

    #r = fermatLittleTheorem((2*cipher)*(4*cipher), int((prime-5)/8), prime)
    #r = ((2*cipher)%prime)*(pow((4*cipher), int((prime-5)/8), prime))
    r = pow((4*cipher), int((prime-5)/8), prime)
    r = (2*cipher)*r
    #r = fermatLittleTheorem((4*cipher), int((prime-5)/8), prime, (2*cipher))
    print('algo2 r: ' + str(r))
    #r2 = (2*cipher) % prime

    #r = r*r2

    return (r, -r)
        #((2*cipher)*((4*cipher)**()))

def chooseSquareRootAlgorithm(prime, cipher):

  if (debug == 3): print(prime)
  if (debug == 3): print(cipher)

  if ((prime % 4) == (3 % 4)):

    print('algo 1')

    roots = squareRootAlgorithm1(prime, cipher)

    return roots

  elif((prime % 8) == (5 % 8)):

    print('algo 2')

    roots = squareRootAlgorithm2(prime, cipher)

    return roots

  else:

    return False

def RabinSchemeDecryption(p, q, n, cipher):

  firstSetOfRoots = chooseSquareRootAlgorithm(p, cipher)
  if (firstSetOfRoots == False):

    return 'p is not prime'
    
  print('the p before ssr: ' + str(p))
  print('the cipher before ssr: ' + str(cipher))
  print('fsr: ' + str(firstSetOfRoots))

  print('the q before ssr: ' + str(q))
  print('the cipher before ssr: ' + str(cipher))
  secondSetOfRoots = chooseSquareRootAlgorithm(q, cipher)

  if (secondSetOfRoots == False):

    return 'q is not prime'
    
  print('ssr: ' + str(secondSetOfRoots))

  values = ExtendedEuclideanAlgorithm(p, q)
  print('Values: ' + str(values))
  first = values[0]*q
  print('First: ' + str(first))
  second = values[1]*p
  print('Second: ' + str(second))
  total = first + second
  print('Total: ' + str(total))

  if (total ==1):

    print('THIS - second')
    print('secondSetOfRoots: ' + str(secondSetOfRoots))
    print('firstSetOfRoots: ' + str(firstSetOfRoots))
    x = ((firstSetOfRoots[0] * values[0] * q) + (secondSetOfRoots[0] * values[1] * p)) % n
    y = ((firstSetOfRoots[0] * first) - (secondSetOfRoots[0] * second)) % n
    print('n: ' + str(n))
    print('x: ' + str(x))
    print('y: ' + str(y))
    xNeg = ((firstSetOfRoots[1] * values[0] * q) + (secondSetOfRoots[1] * values[1] * p)) % n
    yNeg = ((firstSetOfRoots[1] * first) - (secondSetOfRoots[1] * second)) % n
    print('xNeg: ' + str(xNeg))
    print('yNeg: ' + str(yNeg))
    rootList = [x, y, xNeg, yNeg]
    return rootList

  else: 

    print('Decryption not possible')

def RabinSchemeEncryption(message, n):

  # max message length is 20 numbers
  #message = 9999999999999999999999
  
  
  
  #22
  #message = 999999999999999999999
  #message = 40569
  
  
  #message = 123456789123456789123456789123456789123456789
  
  
  # $$$  NEW  $$$$
  #masterCipher = ''
  
  cipher = pow(message, 2, n)

  return (cipher, message)



def RabinScheme(message):
 
  #exponent = 1024
  p = LargePrimeGeneratorR()
  q = LargePrimeGeneratorR()
  #p = 277
  #q = 331
  n = p*q
  
  PrivateKey = (p, q)
  PublicKey = n
  
  
  if (p == q):

    q = LargePrimeGeneratorR()

  if (p > q):

    p, q = q, p

  if (debug == 1): print('p is: ' + str(p))
  if (debug == 1): print('q is: ' + str(q))
  if (debug == 1): print('n is: ' + str(n))
  
  
  TotalCipher = []
  TotalDecrypted = []
  
  for i in range(0, len(message)):
      
      cipherAndMessage = RabinSchemeEncryption(message[i], n)
      cipher = cipherAndMessage[0]
      print('Cipher: ' + str(cipher))
      if (debug == 1): print('cipher is: ' + str(cipher))
      Message = cipherAndMessage[1]
      if (debug == 1): print('message is: ' + str(Message))
      TotalCipher.append(cipher)

      decryptedMessage = RabinSchemeDecryption(p, q, n, cipher)
    
      print(decryptedMessage)
      
      for i in range(0, len(decryptedMessage)):
    
        if (decryptedMessage[i]==Message):
            
          decrypted = Message
    
          print("Encryption and Decryption Successful!!")
          
          TotalDecrypted.append(decrypted)
    
      #return cipher, decryptM, PrivateKey, PublicKey
  print('Total Cipher: ' + str(TotalCipher))
  print('Total Decrypted: ' + str(TotalDecrypted))
  return TotalCipher, TotalDecrypted, PrivateKey, PublicKey


def callRabin(userMessage):
    
    
    print('Length User Message: ' + str(len(userMessage)))
    
    
    if (len(userMessage) % 5 == 0):
        
        limit = 5
        
    elif (len(userMessage) % 4 == 0):
        
        limit = 4
            
    elif (len(userMessage) % 3 == 0):
        
        limit = 3
    
    elif (len(userMessage) % 2 == 0):
        
        limit = 2
        
    else:
        
        limit = 1
        
    
    listOfStrings = []
    
    counter = 0
    placeHolder = ''
    
    for i in range(0, len(userMessage)):
        
        placeHolder = placeHolder + userMessage[i]
        counter += 1
        if (counter == limit):
            
            listOfStrings.append(placeHolder)
            counter = 0
            placeHolder = ''
            
        else: 
            
            continue
    
    print('List Of Strings: ' + str(listOfStrings))
    
    listOfIntStrings = []
    
    for chunk in listOfStrings:
        
        integerStringMessage = ''
    
        for letter in chunk: 
            
            x = ord(letter)
            x = str(x)
            if(len(x) == 2):
                x = '0' + x
            integerStringMessage = integerStringMessage + x
            #print(x)
            #print(chr(int(x)))
            
        listOfIntStrings.append(integerStringMessage)
    
    print('List of Converted Strings: ' + str(listOfIntStrings))
    
    
    listOfConvertedToInts = []
    
    
    for i in range(0, len(listOfIntStrings)):
        
        toInt = int(listOfIntStrings[i])
        listOfConvertedToInts.append(toInt)
    
    print('List of Converted to Integers: ' + str(listOfConvertedToInts))
       
     
        
     
    KeysAndMessage = RabinScheme(listOfConvertedToInts)
    print('KeysAndMessage: ' + str(KeysAndMessage))
    
    
    
    
    
    returnedTotalCipher = KeysAndMessage[0]
    returnedTotalDecrypted = KeysAndMessage[1]
    PrivateKey = KeysAndMessage[2]
    PublicKey = KeysAndMessage[3]
    
    CompleteCipher = ''
    for i in range(0, len(returnedTotalCipher)):
        
        c = str(returnedTotalCipher[i])
        CompleteCipher = CompleteCipher + c
        
    
    successCount = 0
    
    for i in range(0, len(returnedTotalDecrypted)):
    
        #After Decryption
        backToString = str(returnedTotalDecrypted[i])
        print('backToString: ' + backToString)
        print('lined Up: ' + str(listOfIntStrings[i]))
    
        numberOfZeros = 0
    
        if (len(backToString) < len(listOfIntStrings[i])):
            
            numberOfZeros = len(listOfIntStrings[i]) - len(backToString)  
    
            for j in range(0, numberOfZeros):
            
                backToString = '0' + backToString 
                #print('newbackTostring: ' + newbackToString)
                
            if (listOfIntStrings[i] == backToString):
                
                print('HERE')
                print('Successful Match!')
                print('\n')
                
                successCount += 1
    
        #print(numberOfZeros)
        #print(backToString)
    
        elif (listOfIntStrings[i] == backToString):
            
            print('Successful Match!')
            print('\n')
            
            successCount += 1
            
            #answer = (TotalCipher, userMessage, PrivateKey, PublicKey)
            
            
    if (successCount == len(returnedTotalDecrypted)):
        
        print('IT WAS A COMPLETE SUCCESS!')
        
        print(CompleteCipher)
        
        return CompleteCipher, userMessage, PrivateKey, PublicKey
       
        
example = callRabin('1234 They 854 who !@#$%^&*')
print(example)