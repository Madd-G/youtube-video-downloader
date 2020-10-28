from pytube import YouTube


yt = YouTube("https://www.youtube.com/watch?v=fi2WkznwWbc")

print(yt.title)

stream = yt.streams.get_highest_resolution().download()

print("Download Done")
