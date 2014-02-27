import webiopi
import datetime
import subprocess
import os
from threading import Thread

GPIO = webiopi.GPIO

#LIGHT = 17 # GPIO pin using BCM numbering

# Pins for the motors
LEFTMOTORPOS = 2 # GPIO pin for left leg positive
LEFTMOTORNEG = 3 # GPIO pin for left leg negative
RIGHTMOTORPOS = 4 # GPIO pin for left leg positive
RIGHTMOTORNEG = 17 # GPIO pin for left leg negative


#HOUR_ON = 8   # Turn Light ON at 08:00
#HOUR_OFF = 18 # Turn Light OFF at 18:00

MEDIA_PATH = "/usr/share/webiopi/htdocs/artoo/sounds"

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    #GPIO.setFunction(LIGHT, GPIO.OUT)

    # set the GPIO used by the motors to output
    GPIO.setFunction(LEFTMOTORPOS, GPIO.OUT)
    GPIO.setFunction(LEFTMOTORNEG, GPIO.OUT)
    GPIO.setFunction(RIGHTMOTORPOS, GPIO.OUT)
    GPIO.setFunction(RIGHTMOTORNEG, GPIO.OUT)


    # retrieve current datetime
    #now = datetime.datetime.now()

    # test if we are between ON time and tun the light ON
    #if ((now.hour >= HOUR_ON) and (now.hour < HOUR_OFF)):
    #    GPIO.digitalWrite(LIGHT, GPIO.HIGH)

# loop function is repeatedly called by WebIOPi 
#def loop():
    # retrieve current datetime
    #now = datetime.datetime.now()

    # toggle light ON all days at the correct time
    #if ((now.hour == HOUR_ON) and (now.minute == 0) and (now.second == 0)):
    #    if (GPIO.digitalRead(LIGHT) == GPIO.LOW):
    #        GPIO.digitalWrite(LIGHT, GPIO.HIGH)

    # toggle light OFF
    #if ((now.hour == HOUR_OFF) and (now.minute == 0) and (now.second == 0)):
    #    if (GPIO.digitalRead(LIGHT) == GPIO.HIGH):
    #        GPIO.digitalWrite(LIGHT, GPIO.LOW)

    # gives CPU some time before looping again
    #webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    #GPIO.digitalWrite(LIGHT, GPIO.LOW)
    GPIO.digitalWrite(LEFTMOTORPOS, GPIO.LOW)
    GPIO.digitalWrite(LEFTMOTORNEG, GPIO.LOW)
    GPIO.digitalWrite(RIGHTMOTORPOS, GPIO.LOW)
    GPIO.digitalWrite(RIGHTMOTORNEG, GPIO.LOW)


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
