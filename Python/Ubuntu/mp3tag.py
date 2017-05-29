# This uses midv32 so, you should install mutagen
# sudo pip install mutagen

import os
from subprocess import call
from time import sleep

def Replace(files):
    files=files.replace('(','\(')
    files=files.replace(')','\)')
    files=files.replace(' ','\ ')
    return files

# Find Music Tag list
P = os.listdir(os.getcwd())

for files in P:
	if files.endswith('.txt'):
		print "Is it music tag list file? \n %s" % files
		a = raw_input('y/n? ')
		if a == 'y':
			templist = open(files,'r')
			break
		elif a =='n':
			continue
			
templist2 = [line.strip() for line in templist]
n = len(templist2)
print templist2

# Split Tag
for i in range(0,n):
	locals()["Taglist"+str(i)] = templist2[i].split('/')

# Find Music file and Tagging
for i in range(0,n):
	title, artist, album, genre, pic = locals()["Taglist"+str(i)][:]
	temp = title.split(' ')
	retitle = temp[0]
	for files in P:
		if files.endswith('.mp3'):
			if files.find(retitle) == -1:
				pass
			else:
				title = Replace(title)
				artist = Replace(artist)
				album = Replace(album)
				genre = Replace(genre)
				pic = Replace(pic)
				files = Replace(files)
				print title
				print "Finish"
				call("mid3v2 -t "+title+" -a "+artist+" -A "+album+" -g "+genre+" -p "+pic+' '+files, shell = True)
	
