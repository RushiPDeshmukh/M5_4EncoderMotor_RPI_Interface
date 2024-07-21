from numpy import pi as PI
from numpy import sin as sin
from numpy import cos as cos

MOTOR_PPR = 2880 # pulses per rotation
WHEEL_DIAMETER = 0.097 # meters
ENCODER_HZ = 50 # Max = 50 since motor driver module can read at max 20ms

# Robot Dimensions 
L_X = 100
L_Y = 100

def getEncoder():
    # get encoder value for all motors with the timestamp
    # needs to be always >20ms time difference
    # encoder_readings = [ts,M0_val,M1_val,M2_val,M3_val]
    encoder_readings = []

    return encoder_readings

def calculateOdometry(now_enc_reading, prev_enc_reading=None, prev_pos=None):
    # use encoder values to calculate position,velocity
    # given encoder readings for Ts (t) and (t-1), get odometry
    if prev_enc_reading is None or prev_pos is None:
        prev_pos = [0,0,0] # x,y,z
        prev_enc_reading = [0,0,0,0,0] # ts, M0_val, M1_val, M2_val, M3_val
    time_delta = now_enc_reading[0]-prev_enc_reading[0]
    motor_angles = [calculate_angle(now_enc_reading[1]-prev_enc_reading[1]),calculate_angle(now_enc_reading[2]-prev_enc_reading[2]),calculate_angle(now_enc_reading[3]-prev_enc_reading[3]),calculate_angle(now_enc_reading[4]-prev_enc_reading[4])]
    motor_angular_speeds = motor_angles/time_delta # [w_0,w_1,w_2,w_3]
    
    # Use Kinematic equations to get robot speeds (linear_x,linear_y and angular_z)
    v_x = (WHEEL_DIAMETER/2)/4 * (motor_angular_speeds[0]+motor_angular_speeds[1]+motor_angular_speeds[2]+motor_angular_speeds[3])
    v_y = (WHEEL_DIAMETER/2)/4 * (-motor_angular_speeds[0]+motor_angular_speeds[1]+motor_angular_speeds[2]-motor_angular_speeds[3])
    w_z = (WHEEL_DIAMETER/2)/(4*(L_X+L_Y)) * (-motor_angular_speeds[0]+motor_angular_speeds[1]-motor_angular_speeds[2]+motor_angular_speeds[3])
    
    pose_x = prev_pos[0] + v_x*time_delta
    pose_y = prev_pos[1] + v_y*time_delta
    pose_z = prev_pos[2]

    pass

def calculate_angle(del_encoder):
    angle = (del_encoder/MOTOR_PPR)*(2*PI) # radians 
    return angle

def euler_to_quaternion(roll,pitch,yaw):
    qx = sin(roll/2) * cos(pitch/2) * cos(yaw/2) - cos(roll/2) * sin(pitch/2) * sin(yaw/2)
    qy = cos(roll/2) * sin(pitch/2) * cos(yaw/2) + sin(roll/2) * cos(pitch/2) * sin(yaw/2)
    qz = cos(roll/2) * cos(pitch/2) * sin(yaw/2) - sin(roll/2) * sin(pitch/2) * cos(yaw/2)
    qw = cos(roll/2) * cos(pitch/2) * cos(yaw/2)

    return [qx,qy,qz,qw]

