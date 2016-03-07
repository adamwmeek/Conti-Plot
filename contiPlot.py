import matplotlib.pyplot as plt
import binascii
import sys


#subroutines to handle command line arguments

def setStartLine():
	argPos = argPos + 1
	startLine = sys.argv[argPos]

def setEndLine():
	argPos = argPos + 1
	#startLine = sys.argv[argPos]


## BEGIN MAIN PROGRAM ##
if len(sys.argv) > 1:
	file = open(sys.argv[1], "rb")
	startLine = 0

	#process remaining arguments
	switch = {
			'sl' : setStartLine,
			'el' : setEndLine,
		}

	numArgs = len(sys.argv)
	argPos = 2

	while(argPos < numArgs):
		arg = sys.argv[argPos]

		if(arg in switch):
			switch[arg]()

		argPos = argPos + 1
else:
	file = open("./contiPlot.py", "rb")
	startLine = 0

try:
	lineCount = 0

	while True:
		byte1 = file.read(1)
		byte2 = file.read(1)

		if byte2 is None: 
			break

		if byte1 == '\n':
			lineCount = lineCount + 1

		byte1 = int(binascii.hexlify(byte1), 16)
		byte2 = int(binascii.hexlify(byte2), 16)

		if(lineCount >= startLine):
			plt.scatter(byte1, byte2)
		file.seek(-1, 1)
	
finally:
	plt.axis([0,255,0,255])
	plt.show()
	file.close()


