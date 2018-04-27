import os
import sys

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

#if __name__ == "__main__":

def getHTML(link, filename):
	output = 'index.txt'
	#print('wget ' + link + ' -O ' + output)
	os.system('wget ' + link + ' -O ' + output)

def printProcessing(count, countTotal):
	print('Processing ... ' + str(i) + '/' + str(countTotal) 
			+ '               ' 
			+ '{:00.0f}%'.format(count/countTotal))

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

def write2file(filename, type, content):
	f = open(filename, type)
	f.write(content)
	f.close

def mkdir(text):
    if not os.path.exists(text):
		os.makedirs(text)
