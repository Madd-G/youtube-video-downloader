#make sure you have downloaded pytube3 
from pytube import YouTube

# enter the url you want to download
yt = YouTube("")

print(yt.title)

# to download the highest resolution
stream = yt.streams.get_highest_resolution().download()

print("Download Done")