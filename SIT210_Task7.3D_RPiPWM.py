# -- SIT210 Task 7.3D -- #
# -- Sean Corcoran -- #
# The following code, takes a reading from a distance sensor every 200ms 
# Then adjusts a LED to become brighter if a object comes closer
# the range is set to 0cm (highest LED output) to 50cm > no LED output

#libraries we need
import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
from time import sleep

# -- Hardware -- #

GPIO.setwarnings(False) # no warnings
GPIO.setmode(GPIO.BCM) 
GPIO.setup(13, GPIO.OUT) #LED

pwm = GPIO.PWM(13, 1000)
pwm.start(0)

# Initialize ultrasonic sensor
sensor = DistanceSensor(trigger=18, echo=24) 

# -- Functions -- #

def ledOutput(value):
    # double the reading from distance sensor, meaning the range is 50cm with the follow below code
    value = value * 2
    #default output level is 100 (high)
    outputValue = 100
    # if the value from the sensor is from 0 to 100 then use it to set the brightness of the LED
    if value < 101 and value > -1:
        # the output of the LED is 100 - the sensor distance meaning the closer something is the brighter the LED
        outputValue = outputValue - value
        print("LED Output: " + str(outputValue) + "%")
        pwm.ChangeDutyCycle(outputValue)
    else:
        # if anything else, turn the LED off 
        outputValue = 0
        pwm.ChangeDutyCycle(outputValue)

def main():
    while True:
	    # Wait 200ms between readings
	    sleep(0.2)

	    # get distance in centimetres with no decemcal places
	    distance = round(sensor.distance * 100)
	    # print to console
	    print("Distance: " + str(distance) + "cm")
	    ledOutput(distance)

# Executes the main function
if __name__ == '__main__': 
    main()