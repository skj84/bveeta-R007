#Tutorial 2: Control bveeta motion with python program
#functions involved
#arguments:    --->   ser.write(b"m Rspeed Lspeed \r\n")
#Rspeed & Lspeed Maximum 200, minimum 10 --> test on your own to get better result
#Author: Bizbot Technology

import time
import serial


#Define functions on TOP

def forward():
	ser.write(b"m -50 -50  \r\n")
	time.sleep(2)

def reverse():	
	ser.write(b"m 50 50  \r\n")
	time.sleep(2)

def right():
	ser.write(b"m -50 50  \r\n")
	time.sleep(2)

def left():
	ser.write(b"m 50 -50  \r\n")
	time.sleep(2)

#=========================================================

#setup Serial communications with bveeta motor driver
ser = serial.Serial('/dev/ttyUSB1', 57600, timeout=0.050)
time.sleep(2) #must wait for 2 seconds for connections established


while True:
	forward()
	reverse()
	right()
	left()
