#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
# ev3.speaker.beep()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
front_ultra = InfraredSensor(Port.S4)
# front_ultra = UltrasonicSensor(Port.S4)
# back_touch = TouchSensor(Port.S1)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

action_timer = StopWatch()
action_timer.reset()

# while action_timer.time() < 30000:
while True:
    # Drive forward at 200 millimeters per second
    robot.drive(200, 0)
    
    while front_ultra.distance() > 5:
        wait(10)
        
    robot.straight(-300)
    while front_ultra.distance() < 5:
        wait(10)

    robot.turn(120)
    ev3.speaker.beep()