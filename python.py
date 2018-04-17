import os
import sys

if __name__ == "__main__":

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

def getHTML(link, filename):
	output = 'index.txt'
	#print('wget ' + link + ' -O ' + output)
	os.system('wget ' + link + ' -O ' + output)