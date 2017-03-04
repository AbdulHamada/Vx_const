#import RPi.GPIO  as GPIO
import time
import math
from math import pi


#GPIO.setmode(GPIO. BOARD)


# SpinMotorX:
X = raw_input (" X_Amplitude (mm) = ")
Vx = raw_input (" X_Velocity (mm/sec) = ")
Mx = raw_input (" mode of stepper X (Puls/Rev) = " )
Tn = raw_input(" Number of periodes (n * T ) = ")
Step_X =  (10) / float (Mx)
print (Step_X)
Num_StepsX = float (X )/ float (Step_X)
print(Num_StepsX)
Ste_DelayX = ((float (X)/ float (Vx)) / float(Num_StepsX))
print(Ste_DelayX)

def SpinMotorX (X_En, X_DIR, X_PUL, Num_StepsX, Ste_DelayX):
    ControlPinX = [X_En, X_DIR, X_PUL]
    for Pin in (ControlPinX):
        GPIO.setup(Pin,GPIO.OUT)
        GPIO.output(Pin, False)
        GPIO.output(X_En, True)
        time.sleep(0.000006)
        for n in range (0, Tn , +1):
            n += 1
            GPIO.output(X_DIR, True)
            time.sleep(0.000006)
            for sx in range (0,Num_StepsX):
                sx +=1
                print (sx)
                GPIO.output(X_PUL, True)
                time.sleep(Ste_DelayX)
                GPIO.output(X_PUL, False)
                time.sleep(Ste_DelayX)
if __name__=='__main__':
    SpinMotorX(36, 38, 40, Num_StepsX, Ste_DelayX)