import serial
import time

print ("hello world!")
 
ser = serial.Serial(
#	port = '/dev/ttyAMA0',
    port = '/dev/ttyUSB0',
	baudrate = 9600,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1
)
ser.reset_input_buffer()

print("Raspberry's sending : ")

try:
    while True:
        line = ser.readline().decode('utf-8').rstrip()
        read_msg = "Received Command: " + line
        print(read_msg)

        
        send_msg = f"Pi send: hehe {n}.\n"
        ser.write(b'hehe')
        ser.flush()
        print(send_msg)
        
        n = n + 1
        time.sleep(3)
except KeyboardInterrupt:
    print("Pi says Goodbye")
    ser.close()