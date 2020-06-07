import serial
import syslog
import time
import struct

port = '/dev/ttyUSB0'

ard = serial.Serial(port, 9600,timeout=5)
time.sleep(2) # wait for Arduino

i = 0
double_val = 123.45678901

# TODO:
# - encapsulate this into a class
# - define opcodes (send X, send Y)
# - send buffered command stream

while (i < 4):
    ard.flush()

    # send opcode
    opcode = bytearray([65])
    ard.write(opcode)
    print("Python value sent: ")

    # NOTE: the Arduino Mega board has 32 bit doubles, same as floats
    # Send floats
    packed = struct.pack('f', double_val)
    print(struct.unpack('f', packed))
    ard.write(packed)
    time.sleep(1) # I shortened this to match the new value in your Arduino code

    # Serial read section
    msg = ard.read(ard.inWaiting()) # read all characters in buffer
    print ("Message from arduino: ")
    # print (msg.decode('utf-8'))
    print (msg.decode('ascii'))
    i = i + 1
    double_val += 1.0
