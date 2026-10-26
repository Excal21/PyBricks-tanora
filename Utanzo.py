from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

sebessegek = []

bal_motor  = Motor(Port.A, Direction.COUNTERCLOCKWISE)
jobb_motor = Motor(Port.C)

színérzékelő = ColorSensor(Port.B) 

mindketmotor = DriveBase(bal_motor, jobb_motor, 50, 10)

jobb_motor_sebességei = []
bal_motor_sebességei  = []


while Button.RIGHT not in hub.buttons.pressed():
    jobb_motor_sebességei.append(jobb_motor.speed())
    bal_motor_sebességei.append(bal_motor.speed())
    
    wait(100)

print(jobb_motor_sebességei)
print(bal_motor_sebességei)


print('Megnyomva')

#Kérdés: ugyanakkora a két lista? Igen/Nem Miért?
for i in range(len(jobb_motor_sebességei)):
    jobb_motor.run(jobb_motor_sebességei[i])
    bal_motor.run(bal_motor_sebességei[i])
    wait(100)

mindketmotor.stop()

print('Vége')