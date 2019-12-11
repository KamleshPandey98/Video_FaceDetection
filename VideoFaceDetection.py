import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    eyes = eye_cascade.detectMultiScale(frame, 1.3, 4)
    # nose_cascade = cv2.CascadeClassifier("haarcascade_nose.xml")
    # nose = nose_cascade.detectMultiScale(frame, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 245, 0), 3)

    # For Eyes

        for (ex, ey, ew, eh) in eyes:
            # cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 245, 0), 2)
            cv2.circle(frame, (int(ex + ew *0.5), int(ey + eh *0.5)), int(0.5 * ew), (255, 255 ,0),2)

    # For nose
        # for (nx, ny, nw, nh) in nose:
        #     cv2.rectangle(frame, (nx, ny), (nx + nw, ny + nh), (0, 255, 0), 2)

    c = cv2.waitKey(1)

    if c == 27:
        break
    cv2.imshow("FACE", frame)

cap.release()
cv2.destroyAllWindows()
