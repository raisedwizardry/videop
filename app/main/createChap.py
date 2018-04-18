import xml.dom
import datetime


class createChap:

	def __init__(self, duration, episode):
		chaplist= self.getChaptimes(duration)
		chapfile=open(str(episode)+".txt", 'w')
		chapfile.write('CHAPTER01=00:00:00.00\n')
		chapfile.write('CHAPTER01NAME=Chapter 1\n')
		for i in range (0, len(chaplist), 1):
			chapnum=i+2

			chapfile.write('CHAPTER'+str(format((chapnum), '02'))+'='+ str(chaplist[i]) + '\n')
			chapfile.write('CHAPTER'+str(format((chapnum), '02'))+'NAME=Chapter '+ str(chapnum) +'\n')
		chapfile.close()

	def getMark(self, hour, minute): #turns seconds into an ffmpeg compatible HHMMSS string
		if int(hour)>0:#if longer than 59mins 18m chap
			mark=18
		elif int(minute)>46:#if 45-59mins 13 min chap
			mark=13
		elif int(minute)>35:#if 35-45mins 9 min chap
			mark=8
		elif int(minute)>17:#if 17-35mins 6 min chap
			mark=5
		elif int(minute)>10:#if 10-17mins 4 min
			mark=4
		else:
			mark=None
		return mark

	def getChaptimes(self, duration):
		chaplist=list()
		full=str(duration).split(".")[0]
		hour=str(full).split(":")[0]
		minute=str(full).split(":")[1]
		mark=self.getMark(hour, minute)
		if int(hour)>0:
			iteration=int((int(minute)+(int(hour)*60))/int(mark))
		elif int(hour)==0:
			iteration=int(int(minute)/int(mark))
		else:
			iteration=None
		count=mark
		hours=0
		for i in range(0, iteration, 1):
			if count >=60:
				hours=hours+1
				count=count-60
			chapter= ''+str(format((hours), '02'))+":"+str(format((count), '02'))+":00.00"
			chaplist.append(chapter)
			count=count+mark
		return chaplist



createChap("/mnt/d/Stuff/videop-dev-folder/Video/DVR/processing/plex-dvr/archived/20180415 212908 A.P. BIO s01e05 Dating Toledoans/A.P. BIO s01e05 Dating Toledoans.ts","A.P. BIO s01e05 Dating Toledoans","/mnt/d/Stuff/videop-dev-folder/Video/DVR/processing/plex-dvr/archived/20180415 212908 A.P. BIO s01e05 Dating Toledoans/")
print("till")