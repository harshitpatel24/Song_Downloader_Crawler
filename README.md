# Song_Downloader_Crawler
it requests http://www.hindigeetmala.net/singer/lata_mangeshkar.php song and create one text file containing all youtube links. 
After that I have created a module which read one by one url from file and download videos from youtube with given quality.

Pre-requisites: 

python3 

pip3 install Scrapy 

pip3 install pytube

Scrapy startproject song 

cd song 

Scrapy genspider song_spider

It will store YouTube urls in one text file

now, python3 download_song.py

It will download ans store videos under song/Video/ folder.
