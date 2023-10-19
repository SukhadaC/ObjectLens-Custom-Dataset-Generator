import cv2


cap=cv2.VideoCapture(2)
while cap.isOpened():
    _,frame=cap.read()
    cv2.imshow('Frame',frame)
    k=cv2.waitKey(10)
    if k==27:
     cv2.destroyAllWindows()
     break
