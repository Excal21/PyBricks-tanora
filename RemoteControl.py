from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, multitask, run_task

from usys import stdin
from uselect import poll

hub = PrimeHub()


keyboard = poll()
keyboard.register(stdin)

bal_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
jobb_motor = Motor(Port.C, Direction.CLOCKWISE)

mindket_motor = DriveBase(bal_motor, jobb_motor, 56, 96)



mindket_motor.settings(
    straight_speed = 500,
    straight_acceleration = 100,
    turn_rate = 1000,
    turn_acceleration = 1000)

mindket_motor.use_gyro(True)

# mindket_motor.turn(90)

#mindket_motor.drive(100, 0)



print('Kész')
#mindket_motor.arc(radius=100, angle=90, )

#Érdekesség, ha a drivebase és a sima motorok között váltogatunk, akkor bugos lesz a robot


uh = UltrasonicSensor(Port.D)
hub.speaker.volume(50)

async def tolatoradar():
    while True:
        if await uh.distance() < 200:
            await hub.speaker.beep()
            print(await uh.distance())
            await wait(await uh.distance())
        await wait(10)

async def taviranyito():
    while True:
        if keyboard.poll(0):
            key = stdin.read(1)
            print(key)
            if key == 'a':
                mindket_motor.stop()
                jobb_motor.run(100)
            elif key == 'd':
                mindket_motor.stop()
                bal_motor.run(100)
            elif key == 'w':
                mindket_motor.drive(100, 0)  
            elif key == 's':
                mindket_motor.drive(-100, 0)
            elif key == ' ':
                mindket_motor.stop()

        await wait(10)

async def main():
    await multitask(tolatoradar(), taviranyito())

run_task(main())