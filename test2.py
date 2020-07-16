import numpy as np 
import cv2 

cap = cv2.VideoCapture(0)
while(True):
# Capture frame-by-frame 15 
    ret, frame = cap.read() 
# Our operations on the frame come here 18 
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
# Display the resulting frame 21 
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('test2.jpg',frame)
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


############################################
# cap = cv2.VideoCapture(0)
# while(True):
# # Capture frame-by-frame 15 
#     ret, frame = cap.read() 
# # Our operations on the frame come here 18 
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
# # Display the resulting frame 21 
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('s'):
#         cv2.imwrite('test2.jpg',frame)
#         break
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break 
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()
