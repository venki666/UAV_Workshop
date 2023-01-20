import socket
import threading
import cv2
import time
import numpy as np

# function for receiving data
def udp_receiver():
    while True:
        try:
            response, _ = sock.recvfrom(1024)
        except Exception as e:
            print(e)
            break

# local IP address on Tello side (default), destination port number (for command mode)
TELLO_IP = '192.168.10.1'
TELLO_PORT = 8889
TELLO_ADDRESS = (TELLO_IP, TELLO_PORT)

# Local IP address and destination port number for video reception from Tello
TELLO_CAMERA_ADDRESS = 'udp://@0.0.0.0:11111'

# object for capturing
cap = None

# Prepare objects for receiving data
response = None

# create a socket for communication
# * Address family: AF_INET (IPv4), Socket type: SOCK_DGRAM (UDP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# set IP address and port number used by own host
sock.bind(('', TELLO_PORT))

# create thread for receiving
thread = threading.Thread(target=udp_receiver, args=())
thread.daemon = True
thread.start()

# command mode
sock.sendto('command'.encode('utf-8'), TELLO_ADDRESS)

time.sleep(1)

# Start streaming camera video
sock.sendto('streamon'.encode('utf-8'), TELLO_ADDRESS)

time.sleep(5)

if cap is None:
    cap = cv2.VideoCapture(TELLO_CAMERA_ADDRESS)

if not cap.isOpened():
    cap.open(TELLO_CAMERA_ADDRESS)

time.sleep(1)

while True:
    ret, frame = cap.read()

    # skip if video frame is empty
    if frame is None or frame.size == 0:
        continue

    # Reduce the size of the camera image to half and display it in the window
    frame_height, frame_width = frame.shape[:2]
    frame = cv2.resize(frame, (int(frame_width/2), int(frame_height/2)))

    cv2.imshow('Tello Camera View', frame)

    # quit with q key
    if cv2.waitKey(1) & 0xFF == ord('q'):

        break
release()
cv2.destroyAllWindows()

# stop video streaming
sock.sendto('streamoff'.encode('utf-8'), TELLO_ADDRESS)
