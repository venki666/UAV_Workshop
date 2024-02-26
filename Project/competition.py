'''
This is a simple script that will rotate the
drone in a counter clockwise fasion.There will be four mission pads
placed in four corners of an imaginary rectangle. 
The drone will start its journey from a mission pad. Then go to
other mission pads in counter clockwise direction and finally return to
the first one, it srated its journey.
@Author: MD Shariful Islam
@Date  : 22 February, 2024
'''

from djitellopy import Tello
import time

#configurations
DEFAULT_TELLO_SPEED = 25              #forward speed 
MAX_DISTANCE_BETWEEN_TWO_MPAD = 1000  #maximum distance between two mission pads
TOLERANCE_X_AXIS = 5                  #Absolute tolerance for positioning near mpad.
TOLERANCE_Y_AXIS = 5                  #Absolute tolerance for positioning near mpad.
POSITIONING_ITERATION_COUNT = 5       #Maxium retry to position the drone near missionpad
MINIMUM_HEIGHT_THRESHOLD = 80         #The drone hight while moving forward
DEFAULT_UPWARD_STEP = 20              #Upward step in cm in a shot
DEFAULT_FORWARD_STEP = 20             #Forward move in cm in a shot
DEFAULT_FORWARD_STEP_COUNT = (MAX_DISTANCE_BETWEEN_TWO_MPAD/DEFAULT_FORWARD_STEP) # Total count of forward move
DEFAULT_ROTATION_IN_DEGREE = 90       #Rotation angle is in degree

'''
This function tries to postion the drone near the current mission pad
@param tolerance_x    : This is absolute tolerance for mission pad X axis
@param tolerance_y    : This is absolute tolerance for mission pad Y axis
@param mpad_id        : This is the current mission pad id
@param iteration_count: This is number of iteration that the function will try to
                        position the drone near mission pad within tolerance
'''
tello = Tello()
def tello_position_near_mpad(tolerance_x, tolerance_y,mpad_id, iteration_count):

    y_min = 0-tolerance_y
    y_max = tolerance_y
    x_min = 0-tolerance_x
    x_max = tolerance_x
    loop_count = iteration_count

    x = tello.get_mission_pad_distance_x()
    y = tello.get_mission_pad_distance_y()
    z = tello.get_mission_pad_distance_z()

    for i in range(0,loop_count):
        if y >= y_min and y <= y_max:
            break
        else:
            tello.go_xyz_speed_mid(x,1,z,DEFAULT_TELLO_SPEED,mpad_id)
            time.sleep(1)
            x = tello.get_mission_pad_distance_x()
            y = tello.get_mission_pad_distance_y()
            z = tello.get_mission_pad_distance_z()

    for i in range(0,loop_count):
        if x >= x_min and x <= x_max:
            break
        else:
            tello.go_xyz_speed_mid(2,y,z,DEFAULT_TELLO_SPEED,mpad_id)
            time.sleep(1)
            x = tello.get_mission_pad_distance_x()
            y = tello.get_mission_pad_distance_y()
            z = tello.get_mission_pad_distance_z()


'''
This function moves the drone forward to find a new mission pad
@param step: This is the distance that the drone moves forward at a time
@param step_count: This determines how many times the drone should step forward
@param old_mpad_id: This is the previous mission pad id
'''
def tello_move_to_next_mpad(step, step_count, old_mpad_id):

    loop_count = step_count
    for i in range(0,step_count):

        tello.move_forward(step)
        new_mpad_id = tello.get_mission_pad_id()
        
        if new_mpad_id > 0 and new_mpad_id != old_mpad_id:
            print("new mission pad found")
            break

'''
This is the main loop that rotates the drone 
in counter clockwise direction
in a square shape for 4 mission pads
'''
def main():
    tello = Tello()
    tello.connect()
    #enable mission pad detectiond only in downward
    tello.enable_mission_pads()
    tello.set_mission_pad_detection_direction(0)
    tello.takeoff()
    #get the mission pad id
    mpad_id = tello.get_mission_pad_id()
    #print(mpad_id)

    #no mission pad is found during take off. So land the drone and exit
    if mpad_id < 0:
        tello.land()
        exit(-1)
    
    for i in range(0,4):
        #try to position the drone near the mission pad
        tello_position_near_mpad(TOLERANCE_X_AXIS, TOLERANCE_Y_AXIS, mpad_id, POSITIONING_ITERATION_COUNT)
        current_z = tello.get_mission_pad_distance_z()
        #print("debug1")

        #if the height is higher it is easy to detect the mission pad
        if current_z < MINIMUM_HEIGHT_THRESHOLD:
            tello.move_up(DEFAULT_UPWARD_STEP)
        
        #now go straight to find the next mission pad
        tello_move_to_next_mpad(DEFAULT_FORWARD_STEP, int(DEFAULT_FORWARD_STEP_COUNT),mpad_id)
        mpad_id = tello.get_mission_pad_id()

        #get the drone down a little bit for better positioning
        if current_z >= MINIMUM_HEIGHT_THRESHOLD:
            tello.move_down(DEFAULT_UPWARD_STEP)

        #rotate the drone head 
        tello.rotate_clockwise(DEFAULT_ROTATION_IN_DEGREE)

    #mission completed.now land    
    tello.land()


if __name__ == "__main__":
    main()