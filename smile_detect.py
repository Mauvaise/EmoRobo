import cv2
import numpy as np
import sys
import time

class SMILE:
    def __init__(self):

        self.facePath = "haarcascade_frontalface_default.xml"
        self.smilePath = "haarcascade_smile.xml"
        self.faceCascade = cv2.CascadeClassifier(self.facePath)
        self.smileCascade = cv2.CascadeClassifier(self.smilePath)

        self.cap = cv2.VideoCapture(0)
        self.cap.set(3,640)
        self.cap.set(4,480)

        self.sF = 1.05
        self.smiles = 0

    def Start_Smile_Evaluation(self, evalTime):

        evalEnd= time.time() + evalTime / 100


        while time.time() < evalEnd:
            ret, frame = self.cap.read() # Capture frame-by-frame
            img = frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = self.faceCascade.detectMultiScale(
                gray,
                scaleFactor= self.sF,
                minNeighbors=8,
                minSize=(55, 55),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            # ---- Draw a rectangle around the faces

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]

                smile = self.smileCascade.detectMultiScale(
                    roi_gray,
                    scaleFactor= 1.7,
                    minNeighbors=22,
                    minSize=(25, 25),
                    flags=cv2.CASCADE_SCALE_IMAGE
                    )

                # Set region of interest for smiles
                for (x, y, w, h) in smile:
                    print "Found", len(smile), "smiles!"
                    self.smiles+= 1

                    cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 1)
                    #print "!!!!!!!!!!!!!!!!!"

            #cv2.cv.Flip(frame, None, 1)
            cv2.imshow('Smile Detector', frame)
            cv2.waitKey(1)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break

            # else:
            #     cv2.waitKey(evalTime)
            #     break

            # c = cv2.waitKey(7) % 0x100
            # if c == 27:
            #     break

        self.End_Smile_Evaluation()

    def End_Smile_Evaluation(self):
        self.cap.release()
        cv2.destroyAllWindows()
        print "total smiles", self.smiles


    def Send_Total_Smiles(self):
        return self.smiles