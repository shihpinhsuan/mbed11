import serial

import time


# XBee setting

serdev = '/dev/ttyUSB0'

s = serial.Serial(serdev, 9600)


s.write("+++".encode())

char = s.read(2)

print("Enter AT mode.")

print(char)


s.write("ATMY 0x112\r\n".encode())

char = s.read(3)

print("Set MY 0x112.")

print(char)


s.write("ATDL 0x212\r\n".encode())

char = s.read(3)

print("Set DL 0x212.")

print(char)


s.write("ATID 0x1\r\n".encode())

char = s.read(3)

print("Set PAN ID 0x1.")

print(char)


s.write("ATWR\r\n".encode())

char = s.read(3)

print("Write config.")

print(char)


s.write("ATMY\r\n".encode())

char = s.read(4)

print("MY :")

print(char)


s.write("ATDL\r\n".encode())

char = s.read(4)

print("DL : ")

print(char)


s.write("ATCN\r\n".encode())

char = s.read(3)

print("Exit AT mode.")

print(char)


print("start sending RPC")

while True:

    # send RPC to remote

    s.write("/getAcc/run\n\r".encode())

    char = s.read(40)
    print(char)
    time.sleep(2)

s.close()