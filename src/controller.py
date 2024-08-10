import time
import pandas as pd
from M5MotorController import *
import numpy as np




#PARAMETERS
L = 0.15
W = 0.15
wheel_radius = 0.0485
wheel_dir_alignment = np.array([1,-1,-1,1]).reshape(4,1)
kinematic_model = np.array([[1, -1, -(L + W)],[1, 1, (L + W)],[1,1,-(L+W)],[1,-1,(L+W)]])

def calculateCarPWMs(cmd_vel):
    PWMs = (wheel_radius**-1*wheel_dir_alignment*kinematic_model@cmd_vel)
    return PWMs

cmd_vel = np.array([0.0667,0,0]).reshape(3,1)

print(cmd_vel)

PWMs = calculateCarPWMs(cmd_vel)
print(PWMs)