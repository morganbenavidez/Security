# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:08:49 2022

@author: morga
"""

import random

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

def fermatLittleTheorem(a, exponent, p, multiplier):

  #if (fermatPrimalityTest(p, 100) == False):

  #  return 'p is not Prime'

  checkPrimeFirst = millerRabin(p, 40)

  if (checkPrimeFirst == False):

    return False

  else:

    #print(p)    

    j = p-1     #112
    #print(j)

    k = a**j      
    #print(k)

    m = 1 % p
    #print(m)

    n = int(exponent/j)
    #print('n: ' + str(n))

    if (n>=0):

      o = m**n
      #print('o: ' + str(o))

      q = exponent % j

      #print('q: ' + str(q))

      r = a**q
      #print(r)




      # ADD-ON
      mult = multiplier * r



      #s = r % p
      s = mult % p
      #print(s)

      return (s%p)

    else: return None 
    
    
    
# Algorithm 1

# Input: prime p where p = 3 (mod 4) & 'a' a = string of #'s 
# Inputs: prime p where p = t(mod v) & 'a'
def squareRootAlgorithm1(prime, cipher):

  #checkPrimeFirst = millerRabin(prime, 40)

  r = (fermatLittleTheorem(cipher, int((prime+1)/4), prime, 1))

  #primeFactors(int(prime+1)/4)
  #print(primeFactors)
  #r = cipher**(int(prime+1)/4)
  #r = cipher
  print('algo1 r: ' + str(r))

  if r == False:

    return 'First integer is not prime'

  else:

    r = r % prime

  return(r, -r)



def squareRootAlgorithm2(prime, cipher):

  #checkPrimeFirst = millerRabin(prime, 40)

  d = (fermatLittleTheorem(cipher, int((prime-1)/4),  prime, 1))
  
  if d == 1:

    r = (fermatLittleTheorem(cipher, int((prime+3)/8),  prime, 1))

    return (r, -r)

  elif d == (prime - 1):

    #r = fermatLittleTheorem((2*cipher)*(4*cipher), int((prime-5)/8), prime)

    r = fermatLittleTheorem((4*cipher), int((prime-5)/8), prime, (2*cipher))
    print('algo2 r: ' + str(r))
    #r2 = (2*cipher) % prime

    #r = r*r2

    return (r, -r)
        #((2*cipher)*((4*cipher)**()))

  #return r



def chooseSquareRootAlgorithm(prime, cipher):

  print(prime)
  print(cipher)

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



squareRoots = chooseSquareRootAlgorithm(277, 62111) 
print(squareRoots)