from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
hub.display.orientation(Side.LEFT)

# Portal - Still Alive (Intro / Fődallam)

Tetris = [
    # Első rész
    "E5/4", "B4/8", "C5/8", "D5/4", "C5/8", "B4/8",
    "A4/4", "A4/8", "C5/8", "E5/4", "D5/8", "C5/8",
    "B4/4", "B4/8", "C5/8", "D5/4", "E5/4",
    "C5/4", "A4/4", "A4/4",
    
    # Második rész
    "D5/4", "F5/8", "A5/8", "G5/4", "F5/8", "E5/8",
    "E5/4", "C5/8", "E5/4", "D5/8", "C5/8",
    "B4/4", "B4/8", "C5/8", "D5/4", "E5/4",
    "C5/4", "A4/4", "A4/4"
]


#hub.display.text("SZIASZTOK", 500, 50)

hub.speaker.volume(20)
hub.speaker.play_notes(Tetris, 120)


wait(1000)

print('valami')