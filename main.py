"""Main script to run LineFollower conected to the Raspberry 4."""
import RPi.GPIO as GPIO
import time
# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# TODO Insert here the GPIO Constants connected to the motors
GPIO.setmode(GPIO.BOARD)
engine_left_pin = 11
engine_right_pin = 13

# TODO Insert here the GPIO Constants connected to the sensors
left_sensor = 5
right_sensor = 6
middle_sensor =13

# TODO Insert here a function to run a motor with a specific speed
def engineLeftOn(speed):
    GPIO.output(engine_left_pin, GPIO.HIGH)


# TODO Insert here a function to stop a motor
def engineLeftOff():
    GPIO.output(engine_left_pin, GPIO.LOW)

def engineRightOff():
    GPIO.output(engine_right_pin, GPIO.LOW)

# TODO Insert here a function to read the sensors
def readSensors():
 left = GPIO.input(left_sensor)
 right = GPIO.input(right_sensor)
 middle = GPIO.input(right_sensor)
 return left,right,middle

# TODO Insert here a function to change the motor speed based on the sensors readings

# TODO Insert here a function to turn the robot based on the sensors readings
def turnSensorsRead():
    while true:
        left, right, middle = readSensors()
        if middle ==1:
            engineLeftOn
            
        elif left ==1:
            engineLeftOn
            
        elif right ==1:
            engineLeftOn
            
        else:
            engineLeftOff
            engineRightOff
            
            time.sleep(0.05)
            
# TODO Insert here a function to read the sensors and return the line position

# TODO Insert here a function to run the motors based on the sensors readings

# TODO Insert here the main loop to read the sensors and run the motors

# Clean up the GPIO settings
GPIO.cleanup()
