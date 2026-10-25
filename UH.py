from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()


uh = UltrasonicSensor(Port.D)


while True:
    if uh.distance() < 200:
        hub.speaker.beep()
        wait(uh.distance())
    print(uh.distance())