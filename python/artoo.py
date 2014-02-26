import webiopi
import datetime
import subprocess
import os
from threading import Thread

GPIO = webiopi.GPIO

LIGHT = 17 # GPIO pin using BCM numbering

HOUR_ON = 8   # Turn Light ON at 08:00
HOUR_OFF = 18 # Turn Light OFF at 18:00

MEDIA_PATH = "/usr/share/webiopi/htdocs/artoo/sounds"

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    GPIO.setFunction(LIGHT, GPIO.OUT)

    # retrieve current datetime
    now = datetime.datetime.now()

    # test if we are between ON time and tun the light ON
    if ((now.hour >= HOUR_ON) and (now.hour < HOUR_OFF)):
        GPIO.digitalWrite(LIGHT, GPIO.HIGH)

# loop function is repeatedly called by WebIOPi 
def loop():
    # retrieve current datetime
    now = datetime.datetime.now()

    # toggle light ON all days at the correct time
    if ((now.hour == HOUR_ON) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT, GPIO.HIGH)

    # toggle light OFF
    if ((now.hour == HOUR_OFF) and (now.minute == 0) and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT, GPIO.LOW)

    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(LIGHT, GPIO.LOW)

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
