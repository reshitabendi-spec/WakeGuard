import cv2
import pygame
import math
import time
from cvzone.FaceMeshModule import FaceMeshDetector

pygame.mixer.init()

cap = cv2.VideoCapture(0)

detector = FaceMeshDetector(maxFaces=1)

alarm_on = False
closed_start = None

while True:
    success, img = cap.read()

    if not success:
        break

    img, faces = detector.findFaceMesh(img, draw=False)

    status = "AWAKE"
    color = (0, 255, 0)

    if faces:

        face = faces[0]

        left_up = face[159]
        left_down = face[23]

        eye_distance = math.hypot(
            left_up[0] - left_down[0],
            left_up[1] - left_down[1]
        )

        

        # Draw face box
        x_values = [p[0] for p in face]
        y_values = [p[1] for p in face]

        x = min(x_values)
        y = min(y_values)
        w = max(x_values) - x
        h = max(y_values) - y

        if eye_distance < 13:

            if closed_start is None:
                closed_start = time.time()

            elapsed = time.time() - closed_start

            if elapsed > 2:

                status = "SLEEPING! WAKE UP!"
                color = (0, 0, 255)

                if not alarm_on:
                    print("ALARM TRIGGERED")
                    pygame.mixer.music.load("alarm.wav")
                    pygame.mixer.music.play(-1)
                    alarm_on = True

        else:

            closed_start = None

            if alarm_on:
                pygame.mixer.music.stop()
                alarm_on = False

        cv2.rectangle(
            img,
            (x, y),
            (x + w, y + h),
            color,
            3
        )

    # Top banner
        cv2.rectangle(img, (10, 10), (550, 60), color, -1)

    cv2.putText(
        img,
        status,
        (20, 45),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.putText(
        img,
        "WakeGuard",
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.imshow("WakeGuard - Sleep Alarm Detector", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break