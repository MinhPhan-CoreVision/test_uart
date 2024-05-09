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

n = 1

try:
    while True:
        ser.write(b'hehe')
        ser.flush()
        send_msg = "Pi send: " + str(n)
        print(send_msg)
        n = n + 1
        time.sleep(3)
except KeyboardInterrupt:
	ser.close()