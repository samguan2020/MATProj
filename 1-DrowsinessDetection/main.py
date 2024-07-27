import cv2
import dlib
import pyttsx3
from scipy.spatial import distance

# INITIALIZING THE pyttsx3 SO THAT 
# ALERT AUDIO MESSAGE CAN BE DELIVERED
engine = pyttsx3.init()

# SETTING UP OF CAMERA TO 0 (DEFAULT CAMERA)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video device.")
    exit()

# MAIN LOOP IT WILL RUN UNLESS 
# AND UNTIL THE PROGRAM IS BEING KILLED 
# BY THE USER
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image")
        break
    
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Drowsiness DETECTOR IN OPENCV2", frame)
    
    key = cv2.waitKey(9)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
