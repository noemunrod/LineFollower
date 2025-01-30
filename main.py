"""Main script to run LineFollower conected to the Raspberry 4."""
import RPi.GPIO as GPIO

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# TODO Insert here the GPIO Constants connected to the motors
GPIO.setmode(GPIO.BOARD)
engine_left_pin = 11
engine_right_rightpin = 13


def engineLeftOff():
    GPIO.output(engine_left_pin, GPIO.LOW)


def engineRightOff():
    GPIO.output(engine_right_pin, GPIO.LOW)
# TODO Insert here the GPIO Constants connected to the sensors

# TODO Insert here a function to run a motor with a specific speed


def engineLeftOn(speed):
    GPIO.output(engine_left_pin, GPIO.HIGH)


# TODO Insert here a function to stop a motor

# TODO Insert here a function to read the sensors

# TODO Insert here a function to change the motor speed based on the sensors readings

# TODO Insert here a function to turn the robot based on the sensors readings

# TODO Insert here a function to read the sensors and return the line position

# TODO Insert here a function to run the motors based on the sensors readings

# TODO Insert here the main loop to read the sensors and run the motors

# Clean up the GPIO settings
GPIO.cleanup()
