import os,random,time

#How often do you want the wallpaper to change, random number between these two values

minimumTime = 1    #in minutes
maximumTime = 2    #in minutes

#picks a random time between minimum and maximum value
switchBackgroundTimer = random.randrange(60*minimumTime, 60*maximumTime) 

#directory of your pictures
dir = "/home/USERNAME/Pictures/randomBackgrounds/"

while True:
	backgroundChosen = random.choice(os.listdir(dir))

	if backgroundChosen.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')): #only image extensions
		#set the background, then sleep until it's time to switch the background again
		os.system("gsettings set org.mate.background picture-filename " + dir + backgroundChosen)
		time.sleep(switchBackgroundTimer)
	
	
