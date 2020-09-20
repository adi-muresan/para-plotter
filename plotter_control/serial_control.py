import serial
import syslog
import time
import struct


def run_serial_example():
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


# Communication protocol opcodes
class Protocol:
    Error = 0
    Ready = 1
    ResendLast = 2
    Waiting = 3
    Busy = 4
    Debug = 5


class Ops:
    Nop = 0
    MoveXY = 1
    MoveUD = 2
    Delay = 3
    SetDebug = 4
    ProgramEnd = 5


class State:
    Error = 0
    WaitingStart = 1
    SendingOps = 2
    WaitingReady = 3
    Ended = 4


test_ops = [
    struct.pack('B', Ops.MoveUD) + struct.pack('h', 90),
    struct.pack('B', Ops.Delay) + struct.pack('h', 250),
    struct.pack('B', Ops.MoveUD) + struct.pack('h', 0),
    struct.pack('B', Ops.Delay) + struct.pack('h', 250),
    struct.pack('B', Ops.MoveUD) + struct.pack('h', 90),
    struct.pack('B', Ops.Delay) + struct.pack('h', 250),
    struct.pack('B', Ops.MoveUD) + struct.pack('h', 0),
    struct.pack('B', Ops.Delay) + struct.pack('h', 250),

    struct.pack('B', Ops.ProgramEnd),
]


def run_serial_ops(port):
    ard = serial.Serial(port, 9600, timeout=5)
    time.sleep(2)  # wait for Arduino
    opidx = 0
    state = State.WaitingStart

    while True:
        ard.flush()
        msg = ard.read(ard.inWaiting()) # read all characters in buffer

        while msg:
            # opcode is 1 byte
            protocol_opcode = msg[0]
            msg = msg[1:]

            if protocol_opcode == Protocol.Error:
                print("Error")
            elif protocol_opcode == Protocol.Ready:
                print("Ready")
                if state == State.WaitingReady:
                    state = State.SendingOps
            elif protocol_opcode == Protocol.ResendLast:
                print("Resend last operation")
                opidx -= 1
                if state == State.WaitingReady:
                    state = State.SendingOps

            elif protocol_opcode == Protocol.Waiting:
                # unpack short ints on 2 bytes
                opcount, = struct.unpack('h', msg[:2])
                msg = msg[2:]
                print(f"Waiting: {opcount}")
                if state != State.Ended:
                    state = State.SendingOps
            elif protocol_opcode == Protocol.Busy:
                print("Busy")
            elif protocol_opcode == Protocol.Debug:
                # unpack short ints on 2 bytes
                length, = struct.unpack('h', msg[:2])
                msg = msg[2:]
                dbg = msg[:length].decode('ascii')
                msg = msg[length:]
                print("Debug msg:", dbg)
            else:
                print("Unknown protocol opcode:", int(protocol_opcode))

        if state == State.SendingOps:
            state = State.WaitingReady
            ard.write(test_ops[opidx])
            ard.flush()
            opidx += 1

            if opidx >= len(test_ops):
                state = State.Ended

        # TODO: solve for these delays
        time.sleep(1)


run_serial_ops('/dev/ttyUSB0')

