import cv2
from Samplexml import CreateXML
savexml=True
_capture=True
tracker=cv2.TrackerKCF_create()
cap = cv2.VideoCapture(0)

ok, frame1 = cap.read()
if ok:  
    cv2.imshow("Tracking", frame1)
else:
    print("No frames")
i=0
ok1=False
while True:
    ok, frame1 = cap.read()

    if(_capture==True and ok):
     tracker=cv2.TrackerKCF_create()
     bbox = cv2.selectROI("Tracking",frame1, False,False)
     ok1 = tracker.init(frame1, bbox)  
     print(bbox)
     _capture=False
     continue
    print(frame1.shape)
    
    ok1, bbox = tracker.update(frame1)

    if ok1:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]),
              int(bbox[1] + bbox[3]))
        cv2.rectangle(frame1, p1, p2, (0,0,255), 2, 2)
    cv2.imshow("Tracking", frame1)
    print('Saving %d'%i)
   
    k = cv2.waitKey(1) & 0xff
    if k==97:
        savexml=False
            
    elif k == 27 :
        break
    elif k==98:
        savexml=True
    elif(k==100):
        _capture=True
        
    if(savexml==True):
       ok, frame1 = cap.read()

       imagename=r'D:\Data set\Dataset\Images\img_test{:>05}.jpg'.format(i)
       filename=r'D:\Data set\Dataset\XML\img_test{:>05}.xml'.format(i)
       cv2.imwrite(imagename,frame1)
       size=frame1.shape
       CreateXML(str(p1[0]),str(p1[1]),str(p2[0]),str(p2[1]),filename,imagename,str(size))
       i+=1 

  
   

    
cv2.destroyAllWindows()
