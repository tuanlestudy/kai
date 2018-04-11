from pytube import Playlist
import os
 
#Grabs the file path for Download
def file_path():
	home = os.path.expanduser('~')
	download_path = os.path.join(home, 'Downloads')
	return download_path

link_list = raw_input('Enter Link List: ')
pl = Playlist(link_list)
#pl.download_all()
# or if you want to download in a specific directory
#pl.download_all(file_path())
location = raw_input("Where save file: ")
location = '/Volumes/Lexar64G/'
pl.download_all(location)
print ('')