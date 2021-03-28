#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



ev3 = EV3Brick()

ev3.speaker.beep()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

color_sensor = ColorSensor(Port.S3)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# calculate light threshold
BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2

#set drive_speed to 100 millimeters per second
DRIVE_SPEED = 80

PROPORTIONAL_GAIN = 1.2

while True:
    deviation = color_sensor.reflection() - threshold
    turn_rate = PROPORTIONAL_GAIN * deviation
    robot.drive(DRIVE_SPEED, turn_rate)
    wait(10)
