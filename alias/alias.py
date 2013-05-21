#

# Alias program on windows - python 3.x
# Linux 12.04's python is 2.7.x currently. You may need to do port job if you want to use it on linux
# It is based on GPL license
# Let's go

import sys
import random

# 0 - 25 = A - Z, 26 - 51 = a - z, 52 - 61 = 0 - 9, 62 = ?
def getRandomChar():
        r = random.randint(0, 62)
        if r >= 0 and r <= 25:
                rChar = chr(ord('A') + r)
        elif r >= 26 and r <= 51:
                rChar = chr(ord('a') + r - 26)
        elif r >= 52 and r <= 61:
                rChar = chr(ord('0') + r - 52)
        else:
                rChar = '?'
        #print(rChar)
        return rChar

def FindAll(_f, _ba):
    found = []
    lastOffset = -1
    while True:
        lastOffset += 1
        lastOffset = _f.find(_ba, lastOffset)
        if lastOffset != -1:
            found.append(lastOffset)
        else:
            break
    return found

inputFileName = 'Ift.swf'
outputFileName = 'Ift_alias.swf'
inputTableFileName = 'inTable'
outputTableFileName = 'outRandomTable'

# Read commandline parameter as file input and output
# python alias.py InputFile InputTable OutputFile OutputTable

if len(sys.argv) < 2:
        print('Use default file names\n')
elif len(sys.argv) == 2:
        inputFileName = sys.argv[1]
elif len(sys.argv) == 3:
        inputFileName = sys.argv[1]
        inputTableFileName = sys.argv[2]
elif len(sys.argv) == 4:
        inputFileName = sys.argv[1]
        inputTableFileName = sys.argv[2]        
        OutputFile = sys.argv[3]
elif len(sys.argv) == 5:
        inputFileName = sys.argv[1]
        inputTableFileName = sys.argv[2]        
        OutputFile = sys.argv[3]
        outputTableFileName = sys.argv[4]

print("\n Parsing inputTable ", inputTableFileName + "...... \n")

fI = open(inputTableFileName, 'r')
fO = open(outputTableFileName, 'w')

while True:
        line = fI.readline()
        lg = len(line)

        if len(line) == 0:
                break
        i = 1
        abc = ''
        while True:
                if i > lg - 1:
                        break
                abc = abc + getRandomChar()
                i += 1
        abc += '\n'
        #print(abc)
        fO.write(abc)
print('Parsing done, will write random table to ', outputTableFileName + '\n')
fO.close()

# inputTableFileName -> outputTableFileName
fI = open(inputFileName, 'rb')
fO = open(outputFileName, 'wb')
fInTable = open(inputTableFileName, 'r')
fOutTable = open(outputTableFileName, 'r')

fC = fI.read()
fContent = bytearray(fC)
fI.close()

while True:
        findList = []
        findIndex = 0
        replaceLineBAIndex = 0
        fContentIndex = 0
        
        keyWordLineS = fInTable.readline()
        keyWordLineSLen = len(keyWordLineS)
        replaceLineS = fOutTable.readline()
        replaceLineSLen = len(replaceLineS)
        if keyWordLineSLen == 0:
                break
        keyWordLineBA = bytearray(keyWordLineS.encode())
        del keyWordLineBA[keyWordLineSLen - 1]
        replaceLineBA = bytearray(replaceLineS.encode())
        del replaceLineBA[replaceLineSLen - 1]
        findList = FindAll(fContent, keyWordLineBA)
        print(" ", findList, " ")
        if len(findList) == 0:
                continue
        while True:
                if replaceLineBAIndex ==  len(replaceLineBA) and findIndex == len(findList):
                        break
                fContentIndex = findList[findIndex]
                replaceLineBAIndex = 0
                while True:
                        if replaceLineBAIndex ==  len(replaceLineBA):
                                break
                        fContent[fContentIndex] = replaceLineBA[replaceLineBAIndex]
                        fContentIndex += 1
                        replaceLineBAIndex += 1

                findIndex += 1
                
fInTable.close()
fOutTable.close()
fO.write(fContent)
fO.close()
