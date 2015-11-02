# Python display 
import picamera from time
import sleep
camera = picamera.PiCamera()
## hold preview open
camera.start_preview()
camera.led = False
imageIndex = 0
## Keep bumping the brightness up
while True: 
	i = raw_input('input command')
	imageIndex += 1
	camera.capture('running' + str(imageIndex) + '.jpg')
	sleep(0.1)