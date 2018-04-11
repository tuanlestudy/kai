from pytube import YouTube

#link = raw_input("Enter Link: ")
#YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download()
#yt = YouTube(link)
#yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

import os
import sys
 
# on_progress_callback takes 4 parameters.
def progress_Check(stream = None, chunk = None, file_handle = None, remaining = None):
	#Gets the percentage of the file that has been downloaded.
	try:
		preFile = file_size-remaining
		percent = (100*(file_size-remaining))/(file_size)
		speed = currFile - preFile
		print("{:00.0f}% downloaded".format(percent))
		delete_last_line()
	except ZeroDivisionError:
		print ('ZeroDivisionError')
		redo = start()
 
#Grabs the file path for Download
def file_path():
	home = os.path.expanduser('~')
	download_path = os.path.join(home, 'Downloads')
	return download_path
  
def finish():
 	os.system('exit()')
 	quit()

def start():
	print("Your video will be saved to: {}".format(file_path()))
	#Input 
	yt_url = raw_input("Copy and paste your YouTube URL here: ")
	yt_url = "https://www.youtube.com/watch?v=4Q46xYqUwZQ"

	if(yt_url == 'x'):
		end = finish()
	
	print(yt_url)
	print ("Accessing YouTube URL...")

	# Searches for the video and sets up the callback to run the progress indicator. 
	try:
		video = YouTube(yt_url, on_progress_callback=progress_Check)
	except:
	 	print("ERROR. Check your:\n  -connection\n  -url is a YouTube url\n\nTry again.")
	 	redo = start()
 
 	#print(video.streams.all())

	#Get the first video type - usually the best quality.
	#video_type = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
	video_type = video.streams.filter(progressive=True, file_extension='mp4').first()
 
	#Gets the title of the video
	title = video.title
 
	#Prepares the file for download
	print ("Fetching: {}...".format(title))
	global file_size
	file_size = video_type.filesize
	#Starts the download process
	video_type.download(file_path())
	print(file_size)
	print ("100% downloaded")
	print("\n")
	print ("Ready to download another video.")
	again = start()

def delete_last_line():
	CURSOR_UP_ONE = '\x1b[1A'
	ERASE_LINE = '\x1b[2K'
	sys.stdout.write(CURSOR_UP_ONE)
	sys.stdout.write(ERASE_LINE)
file_size = 0
global preFile
global currFile
currFile = 0
begin = start()