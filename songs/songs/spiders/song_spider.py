# -*- coding: utf-8 -*-
import scrapy
class SongSpiderSpider(scrapy.Spider):
	name = 'song_spider'
	allowed_domains = ['www.hindigeetmala.net','https://www.ssyoutube.com']
	start_urls = ['http://www.hindigeetmala.net']

	def parse(self, response):
		for i in range(1,548):
			url='http://www.hindigeetmala.net/singer/lata_mangeshkar.php?page='+str(i)
			yield scrapy.Request(url,callback=self.parse_songs_page)
		
	def parse_songs_page(self,response):
		links=response.xpath('//td[@class="w185"]/a[@itemprop="url"]/@href').extract()
		print(links)
		for l in links:
			new_url= str(self.start_urls[0])+str(l)
			yield scrapy.Request(new_url,callback=self.parse_song)
			
	def parse_song(self,response):
		y_link=response.xpath('//td[@class="h300 w50p"]/iframe/@src').extract()
		ss_link=[]
		for i in y_link:
			f1=open('C:/Users/Harshit/Desktop/vasudev/songs/all_song_urls.txt','a')
			f1.write(i.replace('embed/','watch?v=')+'\n')
			f1.close()
			#ss_link.append(i.replace('embed/','watch?v='))
		#for s in ss_link:	
		#	print(s)
			
	
	