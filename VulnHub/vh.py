import os
import sys

#https://www.vulnhub.com/?page=1

import urllib

def readURL(link):
	f = urllib.urlopen(link)
	html = f.read()
	return html

def getLink(html):
	print html
	line = readURL(html)
	i = 0
	while True:
		#print len(line)
		#print html[40:50]
		try:
			if (html[i]=='W'): 
				print -1
				break
		except IndexError:
			break
		if(html[i:i+11]=="Walkthrough"):
			print 0
			break
		if (i == (len(line)-1)): 
			break
		print i
		i+=1

str = 'https://www.vulnhub.com/entry/mr-robot-1,151/'
getLink(str)