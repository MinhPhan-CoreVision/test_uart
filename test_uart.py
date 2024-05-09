import serial
import time

print ("hello world!")
 
ser = serial.Serial(
	port = '/dev/ttyAMA0',
	baudrate = 9600,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1
)
ser.reset_input_buffer()

print("Raspberry's sending : ")

n = 0

try:
    while True:
		send_msg = f"Pi send {n}:"
    	ser.write(b'hehe')
    	ser.flush()
    	print("hehe")
    	time.sleep(3)
except KeyboardInterrupt:
	ser.close()