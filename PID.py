from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

bal_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
jobb_motor = Motor(Port.A)

mindketto_motor = DriveBase(bal_motor, jobb_motor, 56, 80)

mindketto_motor.use_gyro(True)

mindketto_motor.settings(
    100,
    100,
    100,
    100
)

mindketto_motor.straight(100)