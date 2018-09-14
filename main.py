#!/usr/bin/python

import init.py
import sensors.py
import display.py
import datetime
import time
#global variables:
tempSensorChannel = 22 #examples, i dont know if these pins are correct
potChannel = 23
ldrChannel =24
resetPin = 25
#bla bla more pins
#might be better to make the pins an array/linkedList

def main():
    global tempSensorPin, potPin, ldrPin, resetPin
    #run initialisation
    init.initADC()
    init.initPins(resetPin)
    #bla bla just example code on how to call functions from another file
    timer = 0
    state = False #if state is false program is not running
    while(True):
        #check if reset button is pushed to start program
        #bla bla bla bla
        #timer

        while(state):#will run until reset button is bushed
        #if reset button pressed: state = False and break

            ## TODO: write function to choose between 500ms, 1s, 2s delay
            #if 500 ms chosen then let delay = 500ms etc etc

            sysTime = datetime.datetime.now().time() #gets the current system time
            display.display(sysTime, timer, sensors.getPot(potChannel), sensors.getTempreture(tempSensorChannel), sensors.getLDR(ldrChannel))
            timer += delay
            time.sleep(delay)



if __name__ == "__main__":
    main()
