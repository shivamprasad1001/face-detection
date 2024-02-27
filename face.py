import cv2
import numpy as np 
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_de(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    faces = face_classifier.detectMultiScale(gray,1.3,5, minSize=(50, 50))

  
    
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x -10 ,y-10),(x+w,y+h),(0,0,255),2)
        cv2.rectangle(img,(x+h, y),(x, y+50), (0, 255, 0), -1)
        # return img
        cv2.putText(img,"Human", (x+20,y+30), cv2.FONT_HERSHEY_TRIPLEX,1, (255,255,255),2 )
        # cv2.put
        return img

cap=  cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    result = face_de(frame)
    # print(result)/
    cv2.imshow("Video Frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows() 


