from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

hub.speaker.volume(30)


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


Boci_Boci = [
    # Boci, boci tarka, se füle, se farka,
    "C4/4", "E4/4", "C4/4", "E4/4", "G4/2",
    "C4/4", "E4/4", "C4/4", "E4/4", "G4/2",
    
    # Oda megyünk lakni, ahol tejet kapni.
    "F4/4", "F4/4", "E4/4", "E4/4", "D4/4", "D4/4", "C4/2",
    "F4/4", "F4/4", "E4/4", "E4/4", "D4/4", "D4/4", "C4/2"
]

Imperial_March = [
    # Főtéma - Első rész (A híres bevezető indítás)
    "G4/4", "G4/4", "G4/4", "E4/8", "A#4/8", 
    "G4/4", "E4/8", "A#4/8", "G4/2",
    
    # Második rész (Magasabb rekeszbe lépés)
    "D5/4", "D5/4", "D5/4", "D#5/8", "A#4/8", 
    "F#4/4", "E4/8", "A#4/8", "G4/2",
    
    # Harmadik rész (A drámai ugrálós dallamvezetés)
    "G5/4", "G4/8", "G4/8", "G5/4", "F#5/8", "F5/8",
    "E5/8", "D#5/8", "E5/4", "G#4/8", "C#5/4", "C5/8", "B4/8",
    "A#4/8", "A4/8", "A#4/4", "D#4/8", "F#4/4", "E4/8", "F#4/8",
    "A#4/4", "G4/8", "A#4/8", "D5/2"
]
FamilyFrost = [
    "Bb5/4",
    "D6/8",
    "C6/4",
    "Eb6/4",
    "D6/4",
    "F6/4",
    "Bb6/2"
]

#hub.display.text("SZIASZTOK", 500, 50)

hub.speaker.play_notes(FamilyFrost, 120)


hub.speaker.play_notes()

