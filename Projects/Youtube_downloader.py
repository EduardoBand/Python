#pip install pytube

from pytube import YouTube
from sys import argv

link = argv[1] #args always 1
yt = YouTube(link)

#To show the title and views 
print("Title: ", yt.title)
print("Views: ", yt.views)

#download the highest resolution of the video

yd = yt.streams.get_highest_resolution()

#You can change the folder at the end, otherwise it will create one. Don't forget to change the user as well.
yd.download('/Users/Eduardo/Desktop/Downloaded')