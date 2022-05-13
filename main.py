import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
# Importing all images

imgBackground = cv2.imread("Background4.png")
# imgGameOver = cv2.imread("gameOver.png")
imgBall = cv2.imread("meteor3.png", cv2.IMREAD_UNCHANGED)
imgBall2 = cv2.imread("meteor3.png", cv2.IMREAD_UNCHANGED)
imgBall3 = cv2.imread("meteor3.png", cv2.IMREAD_UNCHANGED)
imgBall4 = cv2.imread("meteor3.png", cv2.IMREAD_UNCHANGED)
bat1 = cv2.imread("ship2.png", cv2.IMREAD_UNCHANGED)
start = time.time()

# Variables
gameOver=False
ballPos = [100, 100]
speedX = 50
speedY = 50
ballPos2 = [700, 50]
speedX2 = 45
speedY2 = 45
ballPos3 = [1000, 500]
speedX3 = 15
speedY3 = 15
ballPos4 = [500, 500]
speedX4 = 25
speedY4 = 25

detector = HandDetector(detectionCon=0.8, maxHands=1)

# class Worm:
#     def __init__(self):
#         self.points = []
#         self.lengths = []
#         self.currentLength = 0
#         self.allowedLength = 455
#         self.previousHead = 0, 0
#
#     def update(self, imgMain,currentHead):
#         px, py = self.previousHead
#         cx, cy = currentHead
#
#         self.points.append([cx, cy])
#         distance = math.hypot(cx - px, cy - py)
#         self.lengths.append(distance)
#         self.currentLength += distance
#         self.previousHead = cx, cy
#
#         # Length Reduction
#         if self.currentLength > self.allowedLength:
#             for i, length in enumerate(self.lengths):
#                 self.currentLength -= length
#                 self.lengths.pop(i)
#                 self.points.pop(i)
#                 if self.currentLength < self.allowedLength:
#                     break
#         # Draw Snake
#         if self.points:
#             for i, point in enumerate(self.points):
#                 if i != 0:
#                     cv2.line(imgMain, self.points[i - 1], self.points[i], (0, 0, 0), 20)
#             cv2.circle(imgMain, self.points[-1], 20, (0, 0, 0), cv2.FILLED)
#             return imgMain


# game = Worm()

while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img,flipType=False)  # with draw

    # Overlaying the background image
    img = cv2.addWeighted(img, 0.8, imgBackground, 0.2, 0)

    # Check for hands
    if hands:
        for hand in hands:
            if gameOver:
                cvzone.putTextRect(img, "Game Over", [300, 350],
                                   scale=7, thickness=6, offset=20,colorR=(0, 0, 0))
                cvzone.putTextRect(img, f'Your Score: {total}', [200, 500],
                                   scale=7, thickness=6, offset=20,colorR=(0, 0, 0))
            else:
                print("Stopwatch started..")

                x, y, w, h = hand['bbox']
                h1, w1, _ = bat1.shape
                y1 = y - h1 // 2
                y1 = np.clip(y1, 20, 415)
                lmList = hands[0]['lmList']
                pointIndex = lmList[8][0:2]
                # img = game.update(img, pointIndex)
                # cv2.circle(img, pointIndex, 25, (0, 0, 0), cv2.FILLED)
                # _, img = cap.read()
                # img = cv2.flip(img, 1)
                img = cvzone.overlayPNG(img, bat1, (x+80, y1))

                if(abs(ballPos[0]-(x+80))<45 and abs(ballPos[1]-y1)<45) \
                        or (abs(ballPos2[0]-(x+80))<43 and abs(ballPos2[1]-y1)<43)\
                        or (abs(ballPos3[0]-(x+80))<43 and abs(ballPos3[1]-y1)<43)\
                        or (abs(ballPos4[0]-(x+80))<43 and abs(ballPos4[1]-y1)<43):
                    speedX=0
                    speedY=0
                    speedX2= 0
                    speedY2= 0
                    speedX3= 0
                    speedY3= 0
                    speedX4 = 0
                    speedY4 = 0
                    # time when you stop
                    end = time.time()
                    total = round(end - start, 2)
                    total=int(total)
                    gameOver=True

    # Overlaying the background image
    img = cv2.addWeighted(img, 0.5, imgBackground,0.3, 0)

    #move the ball
    if ballPos[1]>=650 or ballPos[1]<=10:
        speedY=-speedY
    if ballPos[0]>=1200 or ballPos[0]<=10:
        speedX=-speedX
    ballPos[0] += speedX
    ballPos[1] += speedY

    #     # Draw the ball
    img = cvzone.overlayPNG(img, imgBall, ballPos)

    if ballPos2[1]>=600 or ballPos2[1]<=10:
        speedY2=-speedY2
    if ballPos2[0]>=1100 or ballPos2[0]<=70:
        speedX2=-speedX2
    ballPos2[0] += speedX2
    ballPos2[1] += speedY2

    img = cvzone.overlayPNG(img, imgBall2, ballPos2)

    if ballPos3[1]>=650 or ballPos3[1]<=10:
        speedY3=-speedY3
    if ballPos3[0]>=1200 or ballPos3[0]<=10:
        speedX3=-speedX3
    ballPos3[0] += speedX3
    ballPos3[1] += speedY3

    img = cvzone.overlayPNG(img, imgBall3, ballPos3)

    if ballPos4[1]>=650 or ballPos4[1]<=10:
        speedY4=-speedY4
    if ballPos4[0]>=1200 or ballPos4[0]<=10:
        speedX4=-speedX4
    ballPos4[0] += speedX4
    ballPos4[1] += speedY4

    img = cvzone.overlayPNG(img, imgBall4, ballPos4)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
