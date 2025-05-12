import cv2
import mediapipe as mp
import math

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 900)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

mpDrawing = mp.solutions.drawing_utils
mpHands = mp.solutions.hands
hand = mpHands.Hands() #NEED TO MAKE NUMBER OF HANDS

####
#all of this code was written with the intent to understand how opencv could be
#used in the game, some code like the if statements had to be understood
#by reading the website (cited in citations.txt for opencv) however the hand
#landmarks and math were written without any code help from the website 
#and written only after reading about the hand landmarks from the text
#this would also be the basis of our code in classHands
####

while True:
    working, frame = cap.read()
    if working:
        convertRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hand.process(convertRGB)
        if result.multi_hand_landmarks:
            handNumbers = result.multi_hand_landmarks[0]
            thumbPoint = handNumbers.landmark[4]
            pointerPoint = handNumbers.landmark[20]
            print(thumbPoint, pointerPoint)
            dis = math.sqrt((thumbPoint.x - pointerPoint.x)**2 + 
                            (thumbPoint.y - pointerPoint.y)**2)
            print(dis)
            for handLandmarks in result.multi_hand_landmarks:
                mpDrawing.draw_landmarks(frame, handLandmarks, 
                                         mpHands.HAND_CONNECTIONS)
        cv2.imshow("image", frame)
    
    if cv2.waitKey(1) == ord("q"): 
        break
cv2.destroyAllWindows()

