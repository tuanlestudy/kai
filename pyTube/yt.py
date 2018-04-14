from pytube import YouTube
from pytube import Playlist
import os
import sys
from optparse import OptionParser

def progress_Check(stream = None, chunk = None, file_handle = None, remaining = None):
	#Gets the percentage of the file that has been downloaded.
	try:
		percent = (100*(file_size-remaining))/(file_size)
		print("{:00.0f}% downloaded".format(percent))
		delete_last_line()
	except ZeroDivisionError:
		print ('ZeroDivisionError')

def delete_last_line():
	CURSOR_UP_ONE = '\x1b[1A'
	ERASE_LINE = '\x1b[2K'
	sys.stdout.write(CURSOR_UP_ONE)
	sys.stdout.write(ERASE_LINE)

def singleDownload(ylink, output):
	print(ylink)
	print('Accessing Youtube URL...')
	try:
		video = YouTube(ylink, on_progress_callback=progress_Check)
		video_type = video.streams.filter(progressive=True, subtype='mp4').first()
 		title = video.title
 		print ("Fetching: {}...".format(title))
		global file_size
		file_size = video_type.filesize
		#Starts the download process
		if(output is None):
			video_type.download()
		else:
			print('Your file will save to:', output)
			video_type.download(output)
		#print(file_size)
		print ("100% downloaded")
	except:
		print("ERROR. Check your:\n  -connection\n  -url is a YouTube url\n\nTry again.")

def playlistDownload(llink, output):
	print()
	print(llink)
	print('Accessing Youtube URL...')
	try:
		pl = Playlist(llink)
		print('Downloading...')
		if(output is None):
			pl.download_all()
		else:
			print('Your file will save to:', output)
			pl.download_all(output)
		delete_last_line()
		print('Completed')
	except:
		print("ERROR. Check your:\n  -connection\n  -url is a YouTube url\n"
		+ "  -add '' to playlist link, example: python yt.py -l 'youtube playlist link'\n"
		+ "  -check your location if you add -o, sometime it's different between systems: Mac, Windows, Linux\n"
		+ "\nTry again.")
	

def fileSingleDownload(ysfile, output):
	f = open(ysfile, 'r')
	for line in f:
		#print line
		singleDownload(line, output)
	f.close()

def filePlaylistDownload(ysfile, output):
	f = open(ysfile, 'r')
	for line in f:
		#print line
		singleDownload(line, output)
	f.close()

if __name__ == "__main__":
	parser = OptionParser(usage="%prog [-y] [-o]", version="version 1.0")
	parser.add_option('-y', '--youtube', dest='ylink', help='link single Youtube')
	parser.add_option('-l', '--playlist', dest='llink', help='link playlist Youtube')
	parser.add_option('-o', '--output', dest='output', help='output location')
	parser.add_option('--ys', dest='ysfile', help='link single Youtube from file.txt')
	parser.add_option('--ls', dest='lsfile', help='link playlist Youtube from file.txt')
	
	(options, args) = parser.parse_args()

	if options.ylink:
		singleDownload(options.ylink, options.output)
	if options.llink:
		playlistDownload(str(options.llink), options.output)
	if options.ysfile:
		fileSingleDownload(options.ysfile, options.output)
	if options.lsfile:
		filePlaylistDownload(options.lsfile, options.output)
	