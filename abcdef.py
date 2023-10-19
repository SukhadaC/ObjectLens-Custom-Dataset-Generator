import cv2
from Samplexml import CreateXML

tracker=cv2.TrackerKCF_create()
video = cv2.VideoCapture(0)
while True:
    k,frame = video.read()
    cv2.imshow("Tracking",frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
bbox = cv2.selectROI(frame, False)
ok = tracker.init(frame, bbox)
cv2.destroyWindow("ROI selector")
i=0;
while True:
    imagename=r'D:\Data set\Dataset\Images\img_test{:>05}.jpg'.format(i)
    filename=r'D:\Data set\Dataset\XML\img_test{:>05}.xml'.format(i)
    ok, frame1 = video.read()
    ok, bbox = tracker.update(frame1)
    cv2.imwrite(imagename,frame1)

    if ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]),
              int(bbox[1] + bbox[3]))
        cv2.rectangle(frame1, p1, p2, (0,0,255), 2, 2)
    cv2.imshow("Tracking", frame1)
    CreateXML(str(p1[0]),str(p1[1]),str(p2[0]),str(p2[1]),filename,imagename)
    print('Saving %d'%i)
    i+=1
    k = cv2.waitKey(1) & 0xff
    if k == 27 :
        break
cv2.destroyAllWindows()
