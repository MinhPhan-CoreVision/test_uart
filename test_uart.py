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

n=0
print("Raspberry's sending : ")

try:
    while True:
        # line = ser.readline().decode('utf-8').rstrip()
        # read_msg = "Received Command: " + line
        # print(read_msg)

        # Receive uart message from Pi
        if ser.in_waiting > 0:           
        #   rcvMSG = str(ser.readline()) # <- using readline() but have no eof so timeout was actived
            rcvBytes = ser.read(5)        # <- using read() to read 5 bytes were send
            rcvMSG = str(rcvBytes) 

            read_msg = 'Get command: |->  ' + rcvMSG + '  <-|'
            print(read_msg)
        
        send_msg = f"Pi send: ping {n}.\n"
        ser.write(send_msg.encode('utf-8'))
        ser.flush()
        print(send_msg)
        
        n = n + 1
        time.sleep(3)
except KeyboardInterrupt:
    print("Pi says Goodbye")
    ser.close()