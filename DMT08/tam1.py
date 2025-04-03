import cv2
import serial
import time

def initialize_arduino(port='COM3', baudrate=9600):
    try:
        arduino = serial.Serial(port, baudrate)
        time.sleep(2)  # Chờ Arduino khởi động
        return arduino
    except serial.SerialException as e:
        print(f"Error initializing Arduino: {e}")
        return None

def initialize_camera():
    videoCam = cv2.VideoCapture(0)
    if not videoCam.isOpened():
        print("The camera is not accessible")
        return None
    return videoCam

def main():
    arduino = initialize_arduino()
    if arduino is None:
        return

    videoCam = initialize_camera()
    if videoCam is None:
        return

    classifierFace = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    buttonispressed = False

    try:
        while not buttonispressed:
            ret, framework = videoCam.read()
            if not ret:
                print("Failed to capture frame")
                break

            gray = cv2.cvtColor(framework, cv2.COLOR_BGR2GRAY)
            dafFace = classifierFace.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=2)

            for (x, y, w, h) in dafFace:
                tamX = x + w // 2  # Tọa độ X của tâm
                tamY = y + h // 2  # Tọa độ Y của tâm
                print(f"Tọa độ tâm: {tamX}, {tamY}")
                if w>130 and w <160 :   # Gửi tọa độ tamX sang Arduino
                    arduino.write(f"{tamX} , {tamY}\n".encode())
                print(f"Đã gửi tọa độ tamX: {tamX} ,{tamY}")

                # Vẽ hình tròn tại tọa độ tâm

                cv2.circle(framework, (tamX, tamY), 5, (0, 0, 255), -1)
                cv2.putText(framework, f"({tamX}, {tamY})", (tamX, tamY), cv2.FONT_HERSHEY_SIMPLEX, 1, (180, 0, 255), 2)
                cv2.rectangle(framework, (x, y), (x + w, y + h), (0, 255, 0), 2)

            teks = f"so luong khon mat {len(dafFace)}"
            cv2.putText(framework, teks, (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (250, 250, 255), 2)

            cv2.imshow("tam", framework)

            # Thoát bằng phím 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                buttonispressed = True
                break
    finally:
        # Giải phóng camera và đóng kết nối
        videoCam.release()
        cv2.destroyAllWindows()
        if arduino:
            arduino.close()

if __name__ == "__main__":
    main()
