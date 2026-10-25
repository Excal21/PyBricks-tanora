from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# hub.display.icon([[30, 24, 50, 59, 29], [31, 52, 76, 110, 39], [43, 90, 108, 110, 48], [39, 51, 103, 103, 41], [24, 25, 88, 74, 32]])
# wait(1000)

# hub.display.off()
# hub.display.pixel(3, 2, 100)
# wait(1000)

hub.display.orientation(Side.LEFT)

ultra = UltrasonicSensor(Port.F)

beeped = False

hub.speaker.volume(30)

while True:
    input()
    print(ultra.distance())

    if ultra.distance() < 300:
        hub.speaker.beep(1000, 100)
        wait(ultra.distance()-100)
