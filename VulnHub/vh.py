import os
import sys

#https://www.vulnhub.com/?page=1

def getHTML(link, filename):
	output = 'index.txt'
	cmd = 'wget ' + link + ' -O' + output
	print (cmd)
	os.system(cmd)

def delete_last_line():
	CURSOR_UP_ONE = '\x1b[1A'
	ERASE_LINE = '\x1b[2K'
	sys.stdout.write(CURSOR_UP_ONE)
	sys.stdout.write(ERASE_LINE)

def countTotalLine(filename):
	count = 0
	f = open(filename, 'r')
	for line in f:
		count += 1
	f.close()
	return count

def getLinkFromFile(filename):
	beg = 0
	end = 0
	check = False
	f = open(filename, 'r')
	for line in f:
		for i in range(0, len(line)):
			if (line[i:i+7]=='/entry/'):
				beg = i
				i = i + 7
				end = i 
				while True:
					if (line[i] == '"'):
						if (line[i-1] == '/'):
							end = i
							check = checkLinkInFile('link.txt', line[beg:end])
							if (check == False):
								print line[beg:end]
								writeLink2File('link.txt', line[beg:end])

						break
					else:
						i += 1
	f.close()

def checkAllPages():
	olink = "https://www.vulnhub.com/?page="
	page = 1
	totalpages = 22
	for i in range(page, totalpages+1):
		link = olink + str(i)
		print('Check page: ' + link)
		getHTML(link, 'index.txt')
		print('Checking...')
		getLinkFromFile('index.txt')
		percent = i / totalpages
		print("{:00.0f}% checked".format(percent))
	print('Completed')

def checkFirstPage():
	link = "https://www.vulnhub.com"
	print('Check page: ' + link)
	getHTML(link, 'index.txt')
	print('Checking...')
	getLinkFromFile('index.txt')
	print('Completed')
				
def writeLink2File(filename, link):
	f = open(filename, 'a')
	f.write(link+'\n')
	f.close()

def checkLinkInFile(filename, link):
	check = False
	f = open(filename, 'r')
	for line in f:
		if (line[0:len(line)-1] == link):
			check = True
			break
	f.close()
	return check					

def compFileWalkthrough():
	#create a new file link_raw.txt
	a = open('link_raw.txt', 'w')
	a.close()
	#Create processing function
	b = open('link.txt', 'r')
	countTotal = 0
	for lineb in b:
		countTotal += 1
	b.close()
	f1 = open('link.txt', 'r')
	check = False
	count = 0
	i = 0
	print('Processing... ' + str(i) + '/' + str(countTotal))
	for line1 in f1:
		delete_last_line()
		i += 1
		print('Processing... ' + str(i) + '/' + str(countTotal))
		f2 = open('link_walkthrough.txt', 'r')
		for line2 in f2:
			if(line1 == line2):
				check = True
				break
		f2.close()
		if(check == False):
			f3 = open('link_raw.txt', 'a')
			f3.write(line1)
			f3.close()
			#print line1
			count += 1
		else:
			check = False
	print('We have ' + str(count) + ' links without walkthoughs and ' + str(countTotal - count) + ' links solved.\nCompleted.')


def checkWalkthough():
	sourceLink = 'https://www.vulnhub.com'
	newlist = []
	f = open('link_raw.txt', 'r')
	for line in f:
		link = sourceLink + line[0:len(line)-1]
		getHTML(link, 'index.txt')
		f2 = open('index.txt', 'r')
		check = False
		for line2 in f2:
			for i in range(0, len(line2)):
				if(line2[i:i+14] == 'Walkthrough(s)'):
					check = True
					newlist.append(line)
					break
			if (check == True):
				check = False
				break

	countnewlink = 0
	for newlink in newlist:
		print (sourceLink + newlink[0:len(newlink)-1])
		countnewlink += 1
	print ('Found: ' + str(countnewlink) + ' links with Walkthrough(s)')
	if(countnewlink != 0):
		answer = raw_input("Do you want to save them to link_walkthrough.txt ( y/n) ")
		if(answer == 'y' or answer == 'Y'):
			fw = open('link_walkthrough.txt', 'a')
			for newlink in newlist:
				fw.write(newlink)
			fw.close()
			print('Saved ' + str(countnewlink) + ' links')

def mkdir(text):
    if not os.path.exists(text):
		os.makedirs(text)

def downloading():
	olink = "https://www.vulnhub.com"
	link = ''
	countTotal = countTotalLine('link_walkthrough_download.txt')
	f = open('link_walkthrough_download.txt','r')
	temp = 0
	count = 0
	listlink = []
	for line in f:
		link = olink + line;
		print ('\nTesting ' + link + '\n')
		getHTML(link[0:len(link)-1], 'index.txt')
		print('Finding donwload links ... ')
		f2 = open('index.txt', 'r')
		for line2 in f2:
			for i2 in range(0, len(line2)):
				if(line2[i2:i2+29] == 'https://download.vulnhub.com/'):
					count += 1
					temp = i2+30
					while True:
						if(line2[temp] == '"'):
							#print (str(count) + '  ' + line2[i2:temp])
							listlink.append(line2[i2:temp])
							i2 = temp
							break
						else:
							if (temp >= (len(line2)-10)):
								break
							else:
								temp+=1
		count = 0 
		for l in listlink:
			print (str(count) + ' ' + l)
			count += 1
		choice = input('\nChoose the link to download or 99 to exit: ')
		if (choice != 99):
			print listlink[choice]

			print 'Create folder and download'
			for i in range (0,len(line)):
				if(line[i] == ','):
					print (line[i+1:len(line)-2] + ' ' +line[7:i])

		else:
			w = open('not_download.txt', 'a')
			w.write(line)
			w.close()
			w.close()
		listlink = []
		break




	f.close()


def testing():
	print 'Testing Function'

def start():
	choice = raw_input("\nChoice: \n" 
		+ "1. Check the first page to find new post\n"
		+ "2. Check all pages to find new posts\n"
		+ "3. Check posts have walkthoughs\n"
		+ "4. Check remain links without walkthoughs\n"
		+ "5. Downloading\n"
		#+ "0. Testing\n"
		+ "99.Exit\n\n"
		+ "   Your choice:  ")
	print ''
	if (choice == '1'):
		checkFirstPage()
		start()
	elif (choice == '2'):
		checkAllPages()
		start()
	elif (choice == '3'):
		checkWalkthough()
		start()
	elif (choice == '4'):
		compFileWalkthrough()
		start()
	elif (choice == '5'):
		downloading()
		start()
	elif (choice == '99'):
		print('Exited')
	elif (choice == '0'):
		testing()
	else:
		print('')
		start()

if __name__ == "__main__":
	link = "https://www.vulnhub.com/?page=1"
	start()
