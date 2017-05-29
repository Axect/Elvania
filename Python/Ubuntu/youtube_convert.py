# This program uses youtube-dl, ffmpeg.

# Import
import os
from subprocess import call
from time import sleep

def slugify(files):
    import string
    valid_chars = "-_.()%s%s" % (string.ascii_letters, string.digits)
    files = ''.join(c for c in files if c in valid_chars)
    return files

def Replace(files):
    files=files.replace('(','\(')
    files=files.replace(')','\)')
    return files

# Find Music List 
Q = os.listdir(os.getcwd())

for files in Q:
	if files.endswith('.txt'):
		print "Is it music link list file? \n %s" % files
		a = raw_input('y/n? ')
		if a == 'y':
			templist = open(files,'r')
			break
		elif a =='n':
			continue

musiclinklist = [line.strip() for line in templist]

print 'Start downloding...'
sleep(0.5)

# Download youtube
for link in musiclinklist:
	call('youtube-dl --embed-thumbnail --format mp4 '+link, shell=True)
	
print 'Checking downloded files..'
n = len(musiclinklist)
sleep(5*n)

t = raw_input("Press return to continue")

# Slugify
P = os.listdir(os.getcwd())

for files in P:
    if files.endswith('.mp4'):
        os.rename(files, slugify(files))
    elif files.endswith('.jpg'):
        os.rename(files, slugify(files))

print "Wait Slugifying.."
sleep(1)

# Convert mp4 to mp3
P = os.listdir(os.getcwd())

for files in P:
    if files.endswith('.mp4'):
        f=Replace(files)
        call("ffmpeg -i "+f+" -b:a 320K -vn "+os.path.splitext(f)[0]+'.mp3', shell=True)
