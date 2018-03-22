from pytube import YouTube
import sys
f1=open('C:/Users/Harshit/Desktop/vasudev/songs/all_song_urls.txt','r')
for url in f1:
	try:
		yt = YouTube(str(url))
		videos = yt.get_videos()
		vid = videos[0]
		destination = str('C:/Users/Harshit/Desktop/vasudev/songs/Videos/')
		vid.download(destination)
		print(yt.filename+"\nHas been successfully downloaded")
	except:
		try:
			print(sys.exc_info[0])
			print(url)
		except:
			print("err")