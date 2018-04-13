import os
import sys

#https://www.vulnhub.com/?page=1

import urllib

def readURL(link):
	f = urllib.urlopen(link)
	html = f.read()
	return html

def getLink(html):
	f = open(html, 'r')
	for line in f:
		print line
		for i in range (0, len(line)-1):
			if(html[i]=='"'):
				j = i+1
				while True:
					if (html[j] == '"'): 
						print (html[i:j])
						break
					if (j==len(line)-5):
						break
					j+=1

str = 'html.txt'
getLink(str)