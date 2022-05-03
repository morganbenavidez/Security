# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:21:32 2022

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


