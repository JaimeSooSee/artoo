import webiopi
import datetime
import subprocess
import os
from threading import Thread

# init WebIOPi
GPIO = webiopi.GPIO

# Pins for the motors
LEFTMOTORPOS = 2 # GPIO pin for left leg positive
LEFTMOTORNEG = 3 # GPIO pin for left leg negative
RIGHTMOTORPOS = 4 # GPIO pin for left leg positive
RIGHTMOTORNEG = 17 # GPIO pin for left leg negative

MEDIA_PATH = "/usr/share/webiopi/htdocs/artoo/sounds"

# initialize all the pins to low output
def setup():
    # set the GPIO used by the motors to output
    GPIO.setFunction(LEFTMOTORPOS, GPIO.OUT)
    GPIO.setFunction(LEFTMOTORNEG, GPIO.OUT)
    GPIO.setFunction(RIGHTMOTORPOS, GPIO.OUT)
    GPIO.setFunction(RIGHTMOTORNEG, GPIO.OUT)

    # set all pins to high (motor stop)
    GPIO.digitalWrite(LEFTMOTORPOS, GPIO.HIGH)
    GPIO.digitalWrite(LEFTMOTORNEG, GPIO.HIGH)
    GPIO.digitalWrite(RIGHTMOTORPOS, GPIO.HIGH)
    GPIO.digitalWrite(RIGHTMOTORNEG, GPIO.HIGH)


# shutdown method set all pins to low
def destroy():
    # set all pins to low
    GPIO.digitalWrite(LEFTMOTORPOS, GPIO.LOW)
    GPIO.digitalWrite(LEFTMOTORNEG, GPIO.LOW)
    GPIO.digitalWrite(RIGHTMOTORPOS, GPIO.LOW)
    GPIO.digitalWrite(RIGHTMOTORNEG, GPIO.LOW)


# Begin -- JB -- the code below for the motor conrrol could be a bit cleaner and more extensible but I was going for low latency. I have some ideas about refactoring this to make it cleaner, but not sure about the performance impact at this point.

# motor control
@webiopi.macro
def moveForward():
    GPIO.digitalWrite(LEFTMOTORPOS, GPIO.HIGH)
    GPIO.digitalWrite(LEFTMOTORNEG, GPIO.LOW)
    GPIO.digitalWrite(RIGHTMOTORPOS, GPIO.HIGH)
    GPIO.digitalWrite(RIGHTMOTORNEG, GPIO.LOW)
  
@webiopi.macro
def moveBackward():
    GPIO.digitalWrite(LEFTMOTORPOS, GPIO.LOW)
    GPIO.digitalWrite(LEFTMOTORNEG, GPIO.HIGH)
    GPIO.digitalWrite(RIGHTMOTORPOS, GPIO.LOW)
    GPIO.digitalWrite(RIGHTMOTORNEG, GPIO.HIGH)

@webiopi.macro
def turnLeft():
    GPIO.digitalWrite(LEFTMOTORPOS, GPIO.HIGH)
    GPIO.digitalWrite(LEFTMOTORNEG, GPIO.LOW)
    GPIO.digitalWrite(RIGHTMOTORPOS, GPIO.LOW)
    GPIO.digitalWrite(RIGHTMOTORNEG, GPIO.HIGH)

@webiopi.macro
def turnRight():
    GPIO.digitalWrite(LEFTMOTORPOS, GPIO.LOW)
    GPIO.digitalWrite(LEFTMOTORNEG, GPIO.HIGH)
    GPIO.digitalWrite(RIGHTMOTORPOS, GPIO.HIGH)
    GPIO.digitalWrite(RIGHTMOTORNEG, GPIO.LOW)

@webiopi.macro
def motorStop():
    GPIO.digitalWrite(LEFTMOTORPOS, GPIO.HIGH)
    GPIO.digitalWrite(LEFTMOTORNEG, GPIO.HIGH)
    GPIO.digitalWrite(RIGHTMOTORPOS, GPIO.HIGH)
    GPIO.digitalWrite(RIGHTMOTORNEG, GPIO.HIGH)

@webiopi.macro
def motorShutdown():
    GPIO.digitalWrite(LEFTMOTORPOS, GPIO.LOW)
    GPIO.digitalWrite(LEFTMOTORNEG, GPIO.LOW)
    GPIO.digitalWrite(RIGHTMOTORPOS, GPIO.LOW)
    GPIO.digitalWrite(RIGHTMOTORNEG, GPIO.LOW)

# End -- JB


# play sound
@webiopi.macro
def playSound(file,extension):
    thread2 = Thread(target=playSoundHelper, args=(file,extension))
    thread2.start()

# play sound helper
def playSoundHelper(file,extension):
    file = MEDIA_PATH+"/"+file

    if extension == "mp3":
        os.system('sudo mpg321 ' + file + ' >/dev/null 2>&1')

# kill sounds
@webiopi.macro
def killSounds():
    os.system('sudo killall -9 mpg321 >/dev/null 2>&1')
