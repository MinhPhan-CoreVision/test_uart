import serial
import time

print ("hello world!")

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
    ser.reset_input_buffer()

    while True:
        ser.write ("DietPi hello.\n")
        time.sleep(1)