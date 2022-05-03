# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:27:53 2022

@author: morga
"""


# a, exponent, p

def checkIfpIsPrime(p):

  for i in range(2, p-1):

    if ((p % i) == 0):

      return False

  return True

# gcd(a, p) = 1 


def fermatLittleTheorem(a, exponent, p):

  #if (fermatPrimalityTest(p, 100) == False):

  #  return 'p is not Prime'

  if (checkIfpIsPrime(p) == False):

    return 'p is not Prime'

  else:

    print(p)    

    j = p-1     #112
    print(j)

    k = a**j      
    print(k)

    m = 1 % p
    print(m)

    n = int(exponent/j)
    print('n: ' + str(n))

    if (n>=0):

      o = m**n
      print('o: ' + str(o))

      q = exponent % j

      print('q: ' + str(q))

      r = a**q
      print(r)

      s = r % p
      print(s)

      return (s%p)

    else: return None 


x = fermatLittleTheorem(7, 222, 11)
#x = fermatLittleTheorem(2, 1, 23111347539713119724140943160767373975198399111031433148915311553170917212371239324472633278928332897304131093217337133733527354735933671369140574153421142974363440944514517451947294903496950595081553160296481656968336911704372197297745975377559758376037691772780118101816785398573896989719013913793119377951196199643972197439851994110247102711036910391104571045910501105671065710691108311090911087111971127311779)


print(x)