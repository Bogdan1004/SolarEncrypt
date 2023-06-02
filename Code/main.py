from flask import Flask, render_template
import RPi.GPIO as GPIO
from time import sleep
app = Flask(__name__)

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

# Define servo control functions
def set_angle(pin, angle):
    pwm = GPIO.PWM(pin, 50)  # PWM frequency of 50Hz
    pwm.start(2.5)  # Starting duty cycle (2.5%)
    duty = angle / 18 + 2.5
    pwm.ChangeDutyCycle(duty)
    # Wait for the servo to reach the desired angle
    sleep(0.5)
    pwm.stop()

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/servo15')
def servo15():
    set_angle(17, 15)
    set_angle(18, 15)
    return 'Servo turned 15 degrees.'

@app.route('/servo30')
def servo30():
    set_angle(17, 30)
    set_angle(18, 30)
    return 'Servo turned 30 degrees.'

@app.route('/servo45')
def servo45():
    set_angle(17, 45)
    set_angle(18, 45)
    return 'Servo turned 45 degrees.'

@app.route('/servo60')
def servo60():
    set_angle(17, 60)
    set_angle(18, 60)
    return 'Servo turned 60 degrees.'

@app.route('/servo75')
def servo75():
    set_angle(17, 75)
    set_angle(18, 75)
    return 'Servo turned 75 degrees.'

@app.route('/servo90')
def servo90():
    set_angle(17, 90)
    set_angle(18, 90)
    return 'Servo turned 90 degrees.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')