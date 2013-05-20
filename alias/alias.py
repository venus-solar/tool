#

# Alias program on windows - python 3.x
# Linux 12.04's python is 2.7.x currently. You may need to do port job if you want to use it on linux
# It is based on GPL license
# Let's go

import sys
import random
import binascii

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

inputFileName = ''
outputFileName = 'result'

# Read commandline parameter as file input and output
if len(sys.argv) < 2:
        print('Need input file name!\n')
        sys.exit()
elif len(sys.argv) == 3:
        outputFileName = sys.argv[2]

inputFileName = sys.argv[1]

print("\n Parsing file ", inputFileName + "...... \n")

fI = open(inputFileName, 'r')
fO = open(outputFileName, 'w')

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
print('Parsing done, will write to file ', outputFileName + '\n')

fO.close()
