import os
import sys
from optparse import OptionParser
#create and sort the passwords
def checkDuplicate(line, filename):
	check = False
	fsm = open(filename, 'r')
	for linesm in fsm:
		if(line == linesm):
			check = True
			break
	fsm.close()
	if (check == False):
		write2file(filename,'a',line)
	return check

def dividedPW(fileInput):
	filesm = 'passwordList/pwsm.txt'
	filemd = 'passwordList/pwmd.txt'
	filelg = 'passwordList/pwlg.txt'
	countsm = 0
	countmd = 0
	countlg = 0
	countTotal = countTotalLine(fileInput)
	i = 0
	print('Processing ... ' + str(i) + '/' + str(countTotal))
	f = open(fileInput, 'r')
	for line in f:
		i += 1
		percent = i / countTotal
		delete_last_line()
		print("{:00.0f}% downloaded".format(percent))
		print('Processing ... ' + str(i) + '/' + str(countTotal) 
			+ '               ' 
			+ '{:00.0f}%'.format(percent))
		if(len(line) < 8):
			if(checkDuplicate(line, filesm) == False):
				countsm += 1
		elif(len(line) > 16):
			if(checkDuplicate(line, filelg) == False):
				countlg += 1
		else:
			if(checkDuplicate(line, filemd) == False):
				countmd += 1
	f.close()
	print('sm = ' + str(countsm))
	print('md = ' + str(countmd))
	print('lg = ' + str(countlg))

def countTotalLine(filename):
	count = 0
	f = open(filename, 'r')
	for line in f:
		count += 1
	f.close()
	return count

def delete_last_line():
	CURSOR_UP_ONE = '\x1b[1A'
	ERASE_LINE = '\x1b[2K'
	sys.stdout.write(CURSOR_UP_ONE)
	sys.stdout.write(ERASE_LINE)

def write2file(filename, type, content):
	f = open(filename, type)
	f.write(content)
	f.close

def start():
	parser = OptionParser(usage="%prog [-y] [-o]", version="version 1.0")
	parser.add_option('-i', '--input', dest='inputFile', help='file password')
	
	(options, args) = parser.parse_args()

	if options.inputFile:
		dividedPW(options.inputFile)
	else:
		print''
		start()

if __name__ == "__main__":
	print('Password Manager Program')
	start()