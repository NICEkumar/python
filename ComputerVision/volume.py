import cv2
import time
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activities(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
print(volume.GetVolumeRange())
volume.SetMasterVolumeLevel(-20.0, None)
while True:

    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 15, (242, 123, 100), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (242, 123, 100), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (242, 123, 100), 3)
        cv2.circle(img, (cx, cy), 15, (242, 123, 100), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        print(length)
        if length < 50:
            cv2.circle(img, (cx, cy), 15, (242, 0, 100), cv2.FILLED)



    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime

    cv2.putText(img, f"Fps: {int(fps)}", (30, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

    cv2.imshow('IMG', img)
    cv2.waitKey(1)
