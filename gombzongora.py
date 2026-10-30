from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from usys import stdin
from uselect import poll


keyboard = poll()
keyboard.register(stdin)

hub = PrimeHub()
hub.speaker.volume(20)

while True:
    if keyboard.poll(0):
        karakter = stdin.read(1)
        if karakter == 'a':
            hub.speaker.beep(500)
        elif karakter == 's':
            hub.speaker.beep(1000)
        elif karakter == 'd':
            hub.speaker.beep(1500)
        elif karakter == 'f':
            hub.speaker.beep(2000)
        elif karakter == 'g':
            hub.speaker.beep(2500)
        elif karakter == 'h':
            hub.speaker.beep(3000)
        elif karakter == 'j':
            hub.speaker.beep(3500)
        elif karakter == 'k':
            hub.speaker.beep(4000)
        elif karakter == 'l':
            hub.speaker.beep(4500)
        elif karakter == 'é':
            hub.speaker.beep(5000)