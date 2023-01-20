import threading
import socket
import time
import cv2
class MyTello:
 def __init__(self):
     self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
     self.socket.bind(("0.0.0.0", 8889))

     self.tello_address = ("192.168.10.1", 8889)
     self.receive_thread = threading.Thread(target=self.receive_thread)
     self.receive_thread.daemon = True
     self.receive_thread.start()

     self.socket.sendto('command'.encode('utf-8'), self.tello_address)
     print('sent: command')
     time.sleep(1)
     self.socket.sendto('streamon'.encode('utf-8'), self.tello_address)
     print('sent: streamon\r\n')
     self._running = True

 def terminate(self):
     self._running = False
     self.video.release()
     cv2.destroyAllWindows()

 def receive_thread(self):
     while True:
         try:
             self.response, ip = self.socket.recvfrom(3000)
             print(self.response)
         except socket.error as exc:
             print("Caught exception socket.error : %s" % exc)

 def recv(self):
     self.video = cv2.VideoCapture("udp://@0.0.0.0:11111")
     while self._running:
         try:
             ret, frame = self.video.read()
             if ret:
                 cv2.imshow('Tello', frame)
             cv2.waitKey(1)
         except Exception as err:
             print(err)

 def mystart(self):
     self.recv_videoThread = threading.Thread(target=self.recv)
     self.recv_videoThread.daemon = True
     self.recv_videoThread.start()
     pass

 def myStop(self):
     print('myStop')
     self.recvThread.terminate()
     pass

if __name__ == "__main__":
 print("Start program....")
 myTello= MyTello()
 myTello.mystart()
 x = input('Enter Any key to stop')
 myTello.myStop()
 print("\n\nEnd of Program\n")
