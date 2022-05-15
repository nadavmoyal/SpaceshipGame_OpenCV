import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import time

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Importing all images
imgBackground = cv2.imread("Background4.png")
imgBall = cv2.imread("meteor3.png", cv2.IMREAD_UNCHANGED)
imgBall2 = cv2.imread("meteor3.png", cv2.IMREAD_UNCHANGED)
imgBall3 = cv2.imread("meteor3.png", cv2.IMREAD_UNCHANGED)
imgBall4 = cv2.imread("meteor3.png", cv2.IMREAD_UNCHANGED)
spaceship = cv2.imread("ship2.png", cv2.IMREAD_UNCHANGED)
start = time.time()

# Variables
gameOver=False
ballPos = [100, 100]
speedX = 30
speedY = 30
ballPos2 = [700, 250]
speedX2 = 25
speedY2 = 25
ballPos3 = [1000, 500]
speedX3 = 15
speedY3 = 15
ballPos4 = [500, 500]
speedX4 = 25
speedY4 = 25

detector = HandDetector(detectionCon=0.8, maxHands=1)


while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img,flipType=False)  # with draw

    # Overlaying the background image
    img = cv2.addWeighted(img, 0.8, imgBackground, 0.2, 0)

    # Check for hands
    if hands:
        for hand in hands:
            # displaying the score:
            if gameOver:
                cvzone.putTextRect(img, "Game Over", [300, 350],
                                   scale=7, thickness=6, offset=20,colorR=(0, 0, 0))
                cvzone.putTextRect(img, f'Your Score: {total}', [200, 500],
                                   scale=7, thickness=6, offset=20,colorR=(0, 0, 0))
            else:
                x, y, w, h = hand['bbox']
                h1, w1, _ = spaceship.shape
                y1 = y - h1 // 2
                y1 = np.clip(y1, 20, 415)
                lmList = hands[0]['lmList']
                pointIndex = lmList[8][0:2]
                img = cvzone.overlayPNG(img, spaceship, (x, y1))
                #check if the spaceship destroyed
                if(abs(ballPos[0]-(x+80))<50 and abs(ballPos[1]-y1)<50) \
                        or (abs(ballPos2[0]-(x+80))<50 and abs(ballPos2[1]-y1)<50)\
                        or (abs(ballPos3[0]-(x+80))<50 and abs(ballPos3[1]-y1)<50)\
                        or (abs(ballPos4[0]-(x+80))<50 and abs(ballPos4[1]-y1)<50):
                    #astroids - stop moving.
                    speedX,speedY,speedX2,speedY2,speedX3,speedY3,speedX4,speedY4 = 0,0,0,0,0,0,0,0

                    # stop the time for the score calculation
                    end = time.time()
                    total = round(end - start, 2)
                    total=int(total*17.5)
                    gameOver=True

    # Overlaying the background image
    img = cv2.addWeighted(img, 0.8, imgBackground,0.4, 0)

    #move the ball (asteroid):
    if ballPos[1]>=650 or ballPos[1]<=10:
        speedY=-speedY
    if ballPos[0]>=1200 or ballPos[0]<=10:
        speedX=-speedX
    ballPos[0] += speedX
    ballPos[1] += speedY

   # Draw the ball (asteroid)
    img = cvzone.overlayPNG(img, imgBall, ballPos)

    #move the ball (asteroid):
    if ballPos2[1]>=600 or ballPos2[1]<=10:
        speedY2=-speedY2
    if ballPos2[0]>=1120 or ballPos2[0]<=70:
        speedX2=-speedX2
    ballPos2[0] += speedX2
    ballPos2[1] += speedY2

    # Draw the ball (asteroid)
    img = cvzone.overlayPNG(img, imgBall2, ballPos2)

    #move the ball (asteroid):
    if ballPos3[1]>=650 or ballPos3[1]<=10:
        speedY3=-speedY3
    if ballPos3[0]>=1200 or ballPos3[0]<=10:
        speedX3=-speedX3
    ballPos3[0] += speedX3
    ballPos3[1] += speedY3

    # Draw the ball (asteroid)
    img = cvzone.overlayPNG(img, imgBall3, ballPos3)

    #move the ball (asteroid):
    if ballPos4[1]>=650 or ballPos4[1]<=10:
        speedY4=-speedY4
    if ballPos4[0]>=1200 or ballPos4[0]<=10:
        speedX4=-speedX4
    ballPos4[0] += speedX4
    ballPos4[1] += speedY4

    # Draw the ball (asteroid)
    img = cvzone.overlayPNG(img, imgBall4, ballPos4)

    cv2.imshow("spaceship game", img)
    key = cv2.waitKey(1)
