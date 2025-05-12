import cv2

import threading
import time

import mediapipe as mp
import math
from cmu_graphics import *

class detectHand:

    #def init was pulled directly from the website (in citations.txt for opencv)
    #however some variables were removed as they were not needed in our code
    def __init__(self, maxNumHands = 1, detectionCon = 0.5, trackCon = 0.5):
        self.maxNumHands = maxNumHands = 1
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(max_num_hands=self.maxNumHands,
                min_detection_confidence=self.detectionCon,
                min_tracking_confidence=self.trackCon)
        self.mpDrawing = mp.solutions.drawing_utils
        self.cap = cv2.VideoCapture(0) #open camera here so its only called once
        self.running = False


    #new function
    def getAngle(pointer1, pointer2):
        dx = pointer2.x - pointer1.x
        dy = pointer2.y - pointer1.y
        # converts math.atan2(dy,dx) from radians into degrees
        angleDegrees = math.degrees(math.atan2(dy, dx))
        return angleDegrees
    #end of new function

    #findHandPour and findHandStir was written on my own after learning about
    #opencv from the website (cited in citations.txt for opencv)
    #read handTracking.py for understanding of the progress

    def findHandPour(self, frame, draw = True):
        convertRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #this is becasue
        #the cv actually looks at it in BGR and so it needs to convert to RGB
        self.results = self.hands.process(convertRGB)   #adding into frame

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks: 
                #handlandmarks are finger positions
                # new code
                thumbPointer = hand_landmarks.landmark[4]
                indexPointer = hand_landmarks.landmark[8]
                turnAngle = detectHand.getAngle(thumbPointer, indexPointer)

                if -74 <= turnAngle <= -34:
                    print('hello')
                    app.flagMilk = True

        # return frame    #return frame by frame from camera
    
    def findHandStir(self, frame, draw = True):
        convertRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(convertRGB)

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks: 
                #handlandmarks are finger positions
                #code from handTracking
                handNumbers = self.results.multi_hand_landmarks[0]
                thumbPoint = handNumbers.landmark[4]
                pointerPoint = handNumbers.landmark[20]
                # print(thumbPoint, pointerPoint)
                dis = math.sqrt((thumbPoint.x - pointerPoint.x)**2 + 
                                (thumbPoint.y - pointerPoint.y)**2)
                if dis < 0.1:
                    print("working")
                    app.flagSyrup = True 
                    # app.flagMilk = False
                
        # return frame

    #visited professor Mike's OH and recommended thread detection
    #professor sent python material on thread detection 
    # used Sihab Sahariar's article on Medium for 
    # thread detection function adaption 
    # https://tinyurl.com/multithreadinghelpfor15112tp
    def detectGestures(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                continue
            self.findHandStir(frame)
            self.findHandPour(frame)

            time.sleep(0.03)
        
        self.cap.release()
    
    # def detectStir(self):
    #     self.running = True
    #     cap = cv2.VideoCapture(0)
    #     while self.running:
    #         ret, frame = cap.read()
    #         if not ret:
    #             continue
    #         self.findHandStir(frame)
    #         time.sleep(0.03)
    #     cap.release()

    # def detectPour(self):
    #     self.running = True
    #     cap = cv2.VideoCapture(0)
    #     while self.running:
    #         ret, frame = cap.read()
    #         if not ret:
    #             continue
    #         self.findHandPour(frame)
    #         time.sleep(0.03)
    #     cap.release()

    def startThreadDetection(self):
        #daemon is used to keep the program running in the background
        #taken from Sihab Sahariar's article on Medium for thread detection
        self.running = True
        self.t = threading.Thread(target = self.detectGestures)
        self.t.daemon = True
        self.t.start()

    def stopThreadDetection(self):
        self.running = False

    #didnt end up using findPosition but was pulled directly from the website
    #(cited in citations.txt for opencv)

    # def findPosition(self, frame, numHand = 0, draw = True):
    #     landmark = []   #list of where the fingers are
    #     if self.results.multi_hand_landmarks:
    #         myHand = self.results.multi_hand_landmarks[numHand]
    #         #might be useful, didnt use in handtracking.py
    #         for id, lm in enumerate(myHand.landmark):   
    #             h, w, c = frame.shape
    #             cx, cy = int(lm.x * w), int(lm.y * h)
    #             landmark.append([id, cx, cy])
    #             if draw:
    #                 cv2.circle(frame, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
    #     return landmark

    # code underneath written on our own
    # commented out main1(), main2(), main1Helper(), main2Helper()
    # due to difficulties implementing opencv in 
    # correspondence with cmu graphics
    # main1 and main1helper designed to unlock milk screen in game
    # main2 and main2helper designed to unlock syrup screen in game
    # wrote these functions prior to implementing threading
     
    # def main1():
    #     cap = cv2.VideoCapture(0)
    #     detect = detectHand()
    #     working, frame = cap.read() #reads the frame
    #     # frame = detect.findHandPour(frame)
    #     # print('pour: ', detect.findHandPour(frame))
    #     return detectHand.main1Helper(cap, detect)
    #         # landmark = detect.findPosition(frame) 
    #         # if len(landmark) != 0: #takes position from init
    #         #     print(landmark[3])
    #         # cv2.imshow("image", frame)  #label of the camera
    #         # cv2.waitKey(1)  #this is to quit

    # def main1Helper(cap, detect):
    #     working, frame = cap.read() #reads the frame
    #     frame = detect.findHandPour(frame)

    # def main2():
    #     cap = cv2.VideoCapture(0)
    #     # while True:
    #     detect = detectHand()
    #     working, frame = cap.read() #reads the frame
    #     frame = detect.findHandStir(frame)
    #     return detectHand.main2Helper(cap, detect)

    # def main2Helper(cap, detect):
    #     working, frame = cap.read() #reads the frame
    #     frame = detect.findHandStir(frame)

# detectHand.main1()
# detectHand.main2()

