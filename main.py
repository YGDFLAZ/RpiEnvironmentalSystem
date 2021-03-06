#!/usr/bin/python
import init
import sensors
import display
import datetime
import time
import RPi.GPIO as GPIO
import os
import datetime


#global variables:
resetSwitch = 23
frequencySwitch = 24
stopSwitch = 27
displaySwitch = 22

#ADC PINS
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8

#global variables
delay = 0.5
state = True
start_time = time.time()
displayData= []

def main():
	global resetSwitch, frequencySwitch, stopSwitch, displaySwitch, SPICLK, SPIMISO, SPIMOSI, SPICS, state, displayData, start_time

	#run initialisation
	init.initPins(resetSwitch, frequencySwitch, stopSwitch, displaySwitch)
	GPIO.add_event_detect(frequencySwitch, GPIO.FALLING, callback=frequencyChange, bouncetime=200)
	GPIO.add_event_detect(stopSwitch, GPIO.FALLING, callback=stopButton, bouncetime=200)
	GPIO.add_event_detect(displaySwitch, GPIO.FALLING, callback=displayButton, bouncetime=400)
	GPIO.add_event_detect(resetSwitch, GPIO.FALLING, callback=resetButton, bouncetime=200)

	timer = 0
        display.display(["Time", "      Timer", "Pot", "Temp", "Light"])
    	while(True):
		while(state):#will run until reset button is bushed
			data = []
			data = sensors.getData()
			time.sleep(delay)
			end_time = time.time()
			timer = round(end_time-start_time,0)
			data[1] = datetime.timedelta(seconds=timer)
			displayData.append(data[:])
			display.display(displayData[len(displayData) -1])

def frequencyChange (channel):
	global delay

	if (delay == 0.5):
		delay = 1
	elif (delay == 1):
		delay = 2
	elif (delay == 2):
		delay = 0.5

def stopButton (channel):
	global state

	if (state == False):
		state = True
	else:
		state = False

def displayButton(channel):
	#enter stuff here to call display function
	#(sysTime, timer, Pot, Temp, Light)
	global displayData
	#tempData = displayData
	display.display(["Time", "	Timer", "Pot", "Temp", "Light"])
	if (len(displayData) >=5):
		#display.display([("Time", "Timer", "Pot", "Temp", "Light")])
		display.display(displayData[len(displayData) - 5])
		display.display(displayData[len(displayData) - 4])
		display.display(displayData[len(displayData) - 3])
		display.display(displayData[len(displayData) - 2])
		display.display(displayData[len(displayData) - 1])
	else:
		print("less than 5 items recorded")
	print("")

def resetButton (channel):
	global start_time
	start_time = time.time()
	os.system('clear')

if __name__ == '__main__':
	main()
