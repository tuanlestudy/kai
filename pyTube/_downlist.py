from pytube import Playlist
pl = Playlist("https://www.youtube.com/watch?v=Edpy1szoG80&list=PL153hDY-y1E00uQtCVCVC8xJ25TYX8yPU")
pl.download_all()
# or if you want to download in a specific directory
pl.download_all('/path/to/directory/')