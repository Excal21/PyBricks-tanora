from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

bal_motor  = Motor(Port.A, Direction.COUNTERCLOCKWISE)
jobb_motor = Motor(Port.C)

színérzékelő = ColorSensor(Port.B) 

mindket_motor = DriveBase(bal_motor, jobb_motor, 50, 10)

megallasok_szama = 0

kell_e_ismételni = True

while kell_e_ismételni:

    while színérzékelő.color() != Color.GREEN:
        print(színérzékelő.color())
        mindket_motor.drive(50, 0)
        if színérzékelő.color() == Color.WHITE:
            print('Itt meg kéne állni')
            kell_e_ismételni = False
            break


    mindket_motor.stop()

    hub.speaker.beep()
    megallasok_szama += 1

    #Ide is kell vajon a fehér ellenőrzés?
    while színérzékelő.color() == Color.GREEN:
        wait(10)


mindket_motor.stop()

hub.display.orientation(up=Side.LEFT)
hub.display.number(megallasok_szama)

wait(1000)