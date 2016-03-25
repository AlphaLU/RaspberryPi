import time
import picamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

camera = picamera.PiCamera()
camera.hflip = True
camera.vflip = True

def BlinkPhoto(num, speed):
	for i in range(0, num):
		try:
			print "[*] Taking photo number: " + str(i)
			camera.start_preview()
			GPIO.output(12, 1)
			camera.capture('image'+str(i)+'.jpg')
			time.sleep(speed)
			camera.stop_preview()
			GPIO.output(12, 0)
			time.sleep(speed)
		
		except (KeyboardInterrupt, SystemExit):
			GPIO.output(12, 0)
			GPIO.cleanup()
			camera.stop_preview()
			raise
	
	GPIO.output(12, 1)
	print "[+] -"+str(num)+"- Pictures were taken successfully."
	time.sleep(0.8)
	GPIO.output(12, 0)
	time.sleep(0.8)
	GPIO.output(12, 1)
	time.sleep(0.8)
	GPIO.output(12, 0)
	GPIO.cleanup()

iterations = raw_input("Enter number of photos to take:\n")
speed = raw_iput("Enter time between each photo (sec) :\n")

print "[*] Taking a total of "+str(iterations)+" pictures at a speed of "+str(speed)+" second(s)."

BlinkPhoto(int(iterations), float(speed))