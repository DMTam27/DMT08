import cv2
import numpy as np
import time

classifierFace = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

videoCam = cv2.VideoCapture(0)

if not videoCam.isOpened():
    print("The camera is not accessible")
    exit()

buttonispressed = False
try:
    while not buttonispressed:
        ret, framework = videoCam.read()

        if ret:
            gray = cv2.cvtColor(framework, cv2.COLOR_BGR2GRAY)
            dafFace = classifierFace.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=2)

            if len(dafFace) > 0:
                for (x, y, w, h) in dafFace:
                    print(x, y, w, h)

                    tamX = x + w // 2  # Tọa độ X của tâm
                    tamY = y + h // 2  # Tọa độ Y của tâm
                    print(tamX, tamY)

                    tam = f'({tamX},{tamY})'

                    cv2.circle(framework, (tamX, tamY), 5, (0, 0, 255), -1)  # Chấm đỏ ở tâm
                    cv2.putText(framework, tam, (tamX, tamY), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                    cv2.rectangle(framework, (x, y), (x + w, y + h), (0, 255, 0), 2)

                teks = f"so luong khuon mat = {len(dafFace)}"
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(framework, teks, (0, 30), font, 1, (250, 250, 255), 2)

            cv2.imshow("tam", framework)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                buttonispressed = True
                break
finally:
    # Giải phóng camera và đóng cửa sổ
    videoCam.release()
    cv2.destroyAllWindows()

