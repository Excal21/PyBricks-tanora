from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

bal_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
jobb_motor = Motor(Port.A)


jobb_kerek_sebessegek = []
bal_kerek_sebessegek  = []

felvetel_aktiv = True

while felvetel_aktiv:
    #Ebben a whileban fogjuk feljegyezni, hogy a kerekek mennyit mentek
    jobb_kerek_sebessegek.append(jobb_motor.speed(10))
    bal_kerek_sebessegek.append(bal_motor.speed(10))

    wait(10)

    lenyomott_gombok = hub.buttons.pressed() #Az éppen lenyomott gombok halmaza
    if Button.LEFT in lenyomott_gombok and Button.RIGHT in lenyomott_gombok:
        felvetel_aktiv = False

print(jobb_kerek_sebessegek)

#Ide meg a whileon kívül írunk majd valamit, ami visszaolvassa
for hanyadik in range(len(jobb_kerek_sebessegek)):
    bal_motor.run(bal_kerek_sebessegek[hanyadik])

    jobb_motor.run(     jobb_kerek_sebessegek[hanyadik]      )
    wait(10)