import os,random,time

#Defines how often you want the background to cycle
minimumTime = 1    #in minutes
maximumTime = 2    #in minutes

#picks a random time between minimum and maximum value
cycleBackgroundTimer = random.randrange(60*minimumTime, 60*maximumTime) 

#directory of your pictures
dir = "/home/..."

#repeat while the program is running - program set to startup when system boots in the Linux startup program list.
while True:
	#picks a random file in the directory chosen above
	backgroundChosen = random.choice(os.listdir(dir))
	
	#checks to see if the file chosen ends with common image extensions
	if backgroundChosen.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')): #image extensions
		#set the background, then sleep until it's time to switch the background again
		os.system("gsettings set org.mate.background picture-filename " + dir + backgroundChosen)
		time.sleep(cycleBackgroundTimer)
	
	
