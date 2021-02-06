import RPi.GPIO as GPIO
import time
import cv2
import os

print("start")
while True:
    try:
        echo = 17 #BCM 17端口
        trig = 22 #BCM 22端口

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(trig,GPIO.OUT)
        GPIO.setup(echo,GPIO.IN)

        #send 
        GPIO.output(trig,True)
        time.sleep(0.00001)
        GPIO.output(trig,False)

        #start
        while GPIO.input(echo) == 0:
            pass
        start_time = time.time()
        #stop
        while GPIO.input(echo) == 1:
            pass 
        stop_time = time.time()

        end_time = stop_time - start_time
        data = (end_time * 34300) / 2
        print(data)
        if int(data) <= 10: #距离物体小于等于10cm就熄灭指示灯，并传输视频
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(24,GPIO.OUT)
            print("low")
            GPIO.output(24,GPIO.LOW)
            time.sleep(0.05)
            # os.system("raspistill -o new.jpg")
            # time.sleep(0.5)
            # os.system("xdg-open new.jpg")
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                cv2.imshow("cap",frame)
                if cv2.waitKey(100) & 0xff == ord("q"):
                    break
            cap.release()
            cv2.destroyAllWindows()

        else:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(24,GPIO.OUT)
            print("high")
            GPIO.output(24,GPIO.HIGH)
        time.sleep(0.1)
    except KeyboardInterrupt:
        print("exit!")
        GPIO.cleanup()
        quit()
