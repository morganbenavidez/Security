# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 21:17:58 2022

@author: Morgan
"""

import collections
import binascii
import math
import codecs




debug = 10


def permutateList(permutationTable, itemToConvert):

    # Declare the converted item to return

    convertedItem = ''

    # Loop through the table

    for i in range(0, len(permutationTable)):

      # Store the value at each index in the table

      convertedItem = convertedItem + itemToConvert[permutationTable[i]-1]

    return convertedItem





def takeUserInput(EorD, PassedMessage, SecretKey):

    if(EorD == 'E'):

      PlaintextMessage = PassedMessage

      if (debug == 5): print('Original Plain Text: ' + PlaintextMessage)

      # Convert the Plaintext that they type into Hex Here

      HexMessage = PlaintextMessage.encode("utf-8").hex()

      if (debug == 5): print('Original Plain Text Converted To Hex: ' + str(HexMessage))


    if(EorD == 'D'):

      HexMessage = PassedMessage

        
    # Hex Key Entry
    
    HexString = SecretKey
    
    print('HEXSTRING INFO: ')
    print(HexString)
    print(type(HexString))
    
    HexInt = int(SecretKey, 16)
    
    print('HEXINT INFO: ')
    print(HexInt)
    print(type(HexInt))
    
    HexKey = HexInt
    
    print('HEXKEY INFO: ')
    print(HexKey)
    print(type(HexKey))
    
    #HexKey = 0x133457799BBCDFF1
    if (debug == 5): print('Hex Key: ' + str(HexKey))
    
    return HexMessage, HexKey, EorD





def formSixteenBlocks(UserInput):

    HexKey = UserInput[1]
    EorD = UserInput[2]

    HexKeyConvertedToBinary = f'{HexKey:0>64b}' # 64 Bits 

    if (debug == 5): print('Hex Key Converted To Binary: ' + HexKeyConvertedToBinary)

    # PC1 table skips every 8th element to make a 56 bit permutation
    # Can Randomly Generate this later for different schemes, but must be the same per set of encryption/decryption

    PC1table = [57,49,41,33,25,17,9,
                1,58,50,42,34,26,18,
                10,2,59,51,43,35,27,
                19,11,3,60,52,44,36,
                63,55,47,39,31,23,15,
                7,62,54,46,38,30,22,
                14,6,61,53,45,37,29,
                21,13,5,28,20,12,4]    # 56 Bits 

    Kplus = permutateList(PC1table, HexKeyConvertedToBinary)

    if (debug == 5): print('Kplus: ' + Kplus)

    # Kplus is now 56 bits long
    KplusLength = len(Kplus)

    # Split Kplus into left and right half
    KplusHalf = int(KplusLength/2)

    CLeft = Kplus[:KplusHalf]
    DRight = Kplus[KplusHalf:]

    if (debug ==1): print('Left Side of Kplus: ' + CLeft)
    if (debug ==1): print('Right Side of Kplus: ' + DRight)

    CSubKeyList = []
    DSubKeyList = []
    
    if (EorD == 'E'):

      ShiftList = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

      if (debug == 1): print(type(CSubKeyList))


      for i in range (0, len(ShiftList)):

        if (i == 0):

          C = CLeft
          if (debug == 1): print(C)
          if (debug == 1): print(type(C))
          D = DRight
          if (debug == 1): print(D)
          if (debug == 1): print(type(D))

        else: 

          C = tempC
          D = tempD


        CKeyToRotate = collections.deque(C)
        DKeyToRotate = collections.deque(D)

        CKeyToRotate.rotate(-ShiftList[i])
        AfterShiftC = list(CKeyToRotate)
        tempC = AfterShiftC

        DKeyToRotate.rotate(-ShiftList[i])
        AfterShiftD = list(DKeyToRotate)
        tempD = AfterShiftD

        CSubKeyList.append(AfterShiftC)
        DSubKeyList.append(AfterShiftD)

      ConcatList = []

      for i in range(0, len(CSubKeyList)):

        x = CSubKeyList[i]
        y = DSubKeyList[i]
        z = x + y
        ConcatList.append(z)

      if (debug == 1):
        
        if (debug == 1): print('Concat List: ')  # Each list in the list has 56 bits

        for i in range(0, len(ConcatList)):

          if (debug == 1): print(str(i+1) + '. ' + str(ConcatList[i]))

      return ConcatList

    elif (EorD == 'D'):

      ShiftList = [0,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

      if (debug == 1): print(type(CSubKeyList))


      for i in range (0, len(ShiftList)):

        if (i == 0):

          C = CLeft
          if (debug == 1): print(C)
          if (debug == 1): print(type(C))
          D = DRight
          if (debug == 1): print(D)
          if (debug == 1): print(type(D))

        else: 

          C = tempC
          D = tempD


        CKeyToRotate = collections.deque(C)
        DKeyToRotate = collections.deque(D)

        CKeyToRotate.rotate(ShiftList[i])
        AfterShiftC = list(CKeyToRotate)
        tempC = AfterShiftC

        DKeyToRotate.rotate(ShiftList[i])
        AfterShiftD = list(DKeyToRotate)
        tempD = AfterShiftD

        CSubKeyList.append(AfterShiftC)
        DSubKeyList.append(AfterShiftD)

      ConcatList = []

      for i in range(0, len(CSubKeyList)):

        x = CSubKeyList[i]
        y = DSubKeyList[i]
        z = x + y
        ConcatList.append(z)

      if (debug == 1):
        
        if (debug == 1): print('Concat List: ')  # Each list in the list has 56 bits

        for i in range(0, len(ConcatList)):

          if (debug == 1): print(str(i+1) + '. ' + str(ConcatList[i]))

      return ConcatList





def generateSubKeys(ConcatList):

    ListOfSubkeys = []

    PC2table = [14,17,11,24,1,5,
                3,28,15,6,21,10,
                23,19,12,4,26,8,
                16,7,27,20,13,2,
                41,52,31,37,47,55,
                30,40,51,45,33,48,
                44,49,39,56,34,53,
                46,42,50,36,29,32]  # 48 bits

    for i in range(0, len(ConcatList)):

      permutatedItem = permutateList(PC2table, ConcatList[i])

      ListOfSubkeys.append(permutatedItem)

    if (debug == 1):

      for i in range(0, len(ListOfSubkeys)):

        if (debug == 1): print(ListOfSubkeys[i])

    return ListOfSubkeys


def convertHexStringToBinary(itemToConvertToBinary):

    
    # Come back to this, you need to make a conversion program from hex, to decimal, to binary, to ASCII
    HexString = itemToConvertToBinary
    if (debug == 1): print('HexString: ' + HexString)

    scale = 16  ## equals to hexadecimal
    num_of_bits = 8 
    y = bin(int(HexString, scale))[2:].zfill(num_of_bits)
    if (debug == 1): print('bin: ' + y)

    
    
    return y



def calculateNumberOfBlocksOfData(StringInBits):

    LengthOfMessage = len(StringInBits)

    if (debug == 1): print('Original Length: ' + str(LengthOfMessage))

    ModulusNumber = LengthOfMessage % 64

    if (ModulusNumber == 0):

      NumberOfBlocks = int(LengthOfMessage/64)

    elif (ModulusNumber != 0):

      ExtraZeros = 64 - ModulusNumber

      ListOfZeros = []

      for i in range(0, ExtraZeros):

        ListOfZeros.append('0')

      StringInBits = list(StringInBits)
      
      StringInBits = ListOfZeros + StringInBits
      #StringInBits = StringInBits + ListOfZeros
      
      StringInBits = ''.join(StringInBits)
      NewLength = len(StringInBits)
      if (debug == 1): print('String In Bits: ' + StringInBits)
      if (debug == 1): print('New Length: ' + str(NewLength))

      NumberOfBlocks = int(NewLength/64)

    ListOfBinaryBlocks = []
    tempList = []
    bitCounter = 0

    for binaryDigit in StringInBits:

      tempList.append(binaryDigit)
      bitCounter += 1

      if (bitCounter == 64):

        tempList = ''.join(tempList)
        ListOfBinaryBlocks.append(tempList)
        tempList = []
        bitCounter = 0
        
      else: 

        continue


    return ListOfBinaryBlocks, NumberOfBlocks


def initialPermutationMessage(UserInput):

    HexMessage = UserInput[0]
    if (debug == 1): print('Plaintext Message: ' + HexMessage)
    
    StringInBits = convertHexStringToBinary(HexMessage)
    if (debug == 1): print('String In Bits: ' + str(StringInBits))

    NumberOfBlocksAndActualBlocks = calculateNumberOfBlocksOfData(StringInBits)

    ActualDataBlocks = NumberOfBlocksAndActualBlocks[0]
    NumberOfDataBlocks = NumberOfBlocksAndActualBlocks[1]

    if (debug == 1): print('Actual Data Blocks: ' + str(NumberOfBlocksAndActualBlocks[0]))
    if (debug == 1): print('Number of Blocks: ' + str(NumberOfBlocksAndActualBlocks[1]))


    ipTable = [58,50,42,34,26,18,10,2,
               60,52,44,36,28,20,12,4,
               62,54,46,38,30,22,14,6,
               64,56,48,40,32,24,16,8,
               57,49,41,33,25,17,9,1,
               59,51,43,35,27,19,11,3,
               61,53,45,37,29,21,13,5,
               63,55,47,39,31,23,15,7]


    ListOfPermutatedBlocks = []

    for i in range(0, NumberOfDataBlocks):

      ListOfPermutatedBlocks.append(permutateList(ipTable, ActualDataBlocks[i]))

    if (debug == 1): print(ListOfPermutatedBlocks)


    ListOfPermutatedLeftBlocks = []
    ListOfPermutatedRightBlocks = []

    for block in ListOfPermutatedBlocks:

      ListOfPermutatedLeftBlocks.append(block[0:32])
      ListOfPermutatedRightBlocks.append(block[32:])

    if (debug == 1): print('Left Blocks: ' + str(ListOfPermutatedLeftBlocks))
    if (debug == 1): print(len(ListOfPermutatedLeftBlocks[0]))
    if (debug == 1): print('Right Blocks: ' + str(ListOfPermutatedRightBlocks))
    if (debug == 1): print(len(ListOfPermutatedRightBlocks[0]))

    return ListOfPermutatedLeftBlocks, ListOfPermutatedRightBlocks


def XOR(StringOfBits, fooOrKey):

    xordItem = ''
    byteArrayString = bytearray(StringOfBits, "utf8")
    if (debug == 1): print(byteArrayString)
    byteArrayFooOrKey = bytearray(fooOrKey, "utf8")
    if (debug == 1): print(byteArrayFooOrKey)

    for i in range(0, len(StringOfBits)):

      bit1 = StringOfBits[i]
      bit1 = int(bit1)

      bit2 = fooOrKey[i]
      bit2 = int(bit2)

      if (bit1 == 0 and bit2 == 0):

        bit3 = 0

      elif (bit1 == 1 and bit2 == 1):

        bit3 = 0

      else:

        bit3 = 1

      xordItem = xordItem + str(bit3)
      bit1 = 0
      bit2 = 0
      bit3 = 0

    return xordItem


def SBoxFunction(ByteList, SBoxList):

    MasterList = ''

    for i in range(0, len(ByteList)):
      
      currentByte = ByteList[i]
      if (debug == 1): print(currentByte)
      currentSBox = SBoxList[i]
      if (debug == 1): print(currentSBox)

      RowNumber = currentByte[0] + currentByte[-1]
      RowNumber = int(RowNumber, 2)
      if (debug == 1): print(RowNumber)
      ColumnNumber = currentByte[1:-1]
      ColumnNumber = int(ColumnNumber, 2)
      if (debug == 1): print(ColumnNumber)

      if (RowNumber == 0): index = ColumnNumber
      elif (RowNumber == 1): index = ColumnNumber + 16
      elif (RowNumber == 2): index = ColumnNumber + 32
      elif (RowNumber == 3): index = ColumnNumber + 48

      Value = currentSBox[index]
      if (debug == 1): print('Value: ' + str(Value))


      temp = '{0:04b}'.format(Value) # YES!
      
      if (debug == 1): print('Temp: ' + str(temp))

      MasterList = MasterList + temp

    if (debug == 1): print(MasterList)

    return MasterList


def f(SinglePermutatedRightBlock, SingleSubkey):

    if (debug == 1): print('SinglePermutatedRightBlock: ' + str(SinglePermutatedRightBlock))
    if (debug == 1): print(len(SinglePermutatedRightBlock))
    if (debug == 1): print('Key: ' + str(SingleSubkey))

    EbitSelectionTable = [32,1,2,3,4,5,
                          4,5,6,7,8,9,
                          8,9,10,11,12,13,
                          12,13,14,15,16,17,
                          16,17,18,19,20,21,
                          20,21,22,23,24,25,
                          24,25,26,27,28,29,
                          28,29,30,31,32,1]

    E = permutateList(EbitSelectionTable, SinglePermutatedRightBlock) # Might need to separate these into 6 bit blocks
    if (debug == 1): print('E: ' + str(E))
    if (debug == 1): print(len(E))

    xordItem = XOR(E, SingleSubkey)
    if (debug == 1): print('xord Item: ' + xordItem)

    B1 = xordItem[:6]
    B2 = xordItem[6:12]
    B3 = xordItem[12:18]
    B4 = xordItem[18:24]
    B5 = xordItem[24:30]
    B6 = xordItem[30:36]
    B7 = xordItem[36:42]
    B8 = xordItem[42:48]

    ByteList = [B1,B2,B3,B4,B5,B6,B7,B8]

    if (debug == 1): print(B1)
    if (debug == 1): print(B2)
    if (debug == 1): print(B3)
    if (debug == 1): print(B4)
    if (debug == 1): print(B5)
    if (debug == 1): print(B6)
    if (debug == 1): print(B7)
    if (debug == 1): print(B8)

    SBox1 = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
             0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
             4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
             15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]

    SBox2 = [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
             3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
             0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
             13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]

    SBox3 = [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,
             13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
             13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
             1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]

    SBox4 = [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,
             13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
             10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
             3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]

    SBox5 = [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,
             14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,
             4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
             11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]

    SBox6 = [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,
             10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,
             9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
             4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]

    SBox7 = [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,
             13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
             1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
             6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]

    SBox8 = [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,
             1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,
             7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
             2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]

    SBoxList = [SBox1, SBox2, SBox3, SBox4, SBox5, SBox6, SBox7, SBox8]


    WorkedOutSBox = SBoxFunction(ByteList, SBoxList)

    fPermutation = [16,7,20,21,
                    29,12,28,17,
                    1,15,23,26,
                    5,18,31,10,
                    2,8,24,14,
                    32,27,3,9,
                    19,13,30,6,
                    22,11,4,25]

    Completedf = permutateList(fPermutation, WorkedOutSBox)

    if (debug == 1): print(Completedf)

    return Completedf


def TrasformingABlockSixteenTimes(ListOfPermutatedLeftBlocks, ListOfPermutatedRightBlocks, ListOfSubkeys):
    
    MasterCipher = []

    LoopCounter = 0

    for i in range(0, len(ListOfPermutatedLeftBlocks)):
     
      LNaught = ListOfPermutatedLeftBlocks[i]
      if (debug == 5): print('LNaught: ' + str(LNaught))
      RNaught = ListOfPermutatedRightBlocks[i]
      if (debug == 5): print('RNaught: ' + str(RNaught))

      for j in range(0, 16): # Change the 1 back to a 16 when you're ready to do all 16

        L = RNaught
        if (debug == 5): print('L: ' + str(L))
        foo = f(RNaught, ListOfSubkeys[j])
        if (debug == 5): print('foo: ' + str(foo))
        R = XOR(LNaught, foo)
        if (debug == 5): print('R: ' + str(R))

        LNaught = L
        if (debug == 5): print('New LNaught: ' + str(LNaught))
        RNaught = R
        if (debug == 5): print('New RNaught: ' + str(RNaught))

        LoopCounter = LoopCounter + 1

        if (LoopCounter == 16):

          if (debug == 5): print('Loop 16 LNaught: ' + LNaught)
          if (debug == 5): print('Loop 16 RNaught: ' + RNaught)
          Final = RNaught + LNaught
          if (debug == 5): print('Final: ' + str(Final))

          FinalPermutationTable = [40,8,48,16,56,24,64,32,
                                  39,7,47,15,55,23,63,31,
                                  38,6,46,14,54,22,62,30,
                                  37,5,45,13,53,21,61,29,
                                  36,4,44,12,52,20,60,28,
                                  35,3,43,11,51,19,59,27,
                                  34,2,42,10,50,18,58,26,
                                  33,1,41,9,49,17,57,25]

          FinalList = permutateList(FinalPermutationTable, Final)
          if (debug == 5): print(type(FinalList))
          if (debug == 5): print('Final List: ' + str(FinalList))

          CipherText = hex(int(FinalList, 2))
          if (debug == 5): print('Inner CipherText: ' + str(CipherText))
          if (debug == 5): print(CipherText[2:])

          MasterCipher.append(CipherText[2:])
          if (debug == 5): print('Inner Master Cipher: ' + str(MasterCipher))

          LoopCounter = 0

    return MasterCipher       

def main(EorD, PassedMessage, SecretKey):

    # This returns as a tuple of (hexMessage, hex key, EorD) and must be unpacked 
    UserInput = takeUserInput(EorD, PassedMessage, SecretKey)

    # Begin Key Manipulation
    
    # This returns a list of Concatenated items that are 56 bits long

      
    ConcatList = formSixteenBlocks(UserInput)

    
    # This returns a list of SubKeys that are 48 bits long

    ListOfSubkeys = generateSubKeys(ConcatList)
    if (debug == 1): print('Number of Subkeys: ' + str(len(ListOfSubkeys)))

    #  ListOfSubkeys.reverse()

    if (debug == 1): print('EorD Subkeys: ')
    if (debug == 1): print(ListOfSubkeys)

    # Begin Plaintext manipulation

    # Initial Permutation of the Plaintext Message
    ListOfInitiallyPermutatedLeftAndRightBlocks = initialPermutationMessage(UserInput)
    ListOfPermutatedLeftBlocks = ListOfInitiallyPermutatedLeftAndRightBlocks[0]
    ListOfPermutatedRightBlocks = ListOfInitiallyPermutatedLeftAndRightBlocks[1]

    CipherText = TrasformingABlockSixteenTimes(ListOfPermutatedLeftBlocks, ListOfPermutatedRightBlocks, ListOfSubkeys)
    if (debug == 1): print(CipherText)
    if (EorD == 'E'):

      return CipherText

    elif (EorD == 'D'):

      byteObject = bytes.fromhex(CipherText[0])
      regString = byteObject.decode("utf-8")
      if (debug == 1): print(regString)
      return regString







