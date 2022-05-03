# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:26:30 2022

@author: morga
"""

import random




def fermatLittleTheorem2(a, p):

  return (a**(p-1)) % p




# n = prime - 1

def fermatPrimalityTest(p, t):

  candidate = p

  if candidate == 1:

    return False

  if candidate == 2 or candidate == 3 or candidate ==5:

    return True
  
  n = candidate - 1


  for i in range(0, t):

    randVal = random.randrange(1, n)

    if (fermatLittleTheorem2(randVal, candidate) != 1):

      return False

  return True


# really starts to slow down
# passOrFail = fermatPrimalityTest(1245777, 1)
# (number to test, number OF tests)
passOrFail = fermatPrimalityTest(17, 100)
print(passOrFail)