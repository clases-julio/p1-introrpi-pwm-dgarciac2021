import RPi.GPIO as GPIO;
import time
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
pwm = GPIO.PWM(2, 100)
pwm.start(0)
print ('Press CTRL+C to kill the program')
while True:
	try:
		for i in range(25, 100):
			pwm.ChangeDutyCycle(i)
			time.sleep(0.01)
		for i in range(100, 25, -1):
			pwm.ChangeDutyCycle(i)
			time.sleep(0.01)
	except KeyboardInterrupt:
		print ('\nC ya!')
		break
pwm.stop()
GPIO.cleanup()
