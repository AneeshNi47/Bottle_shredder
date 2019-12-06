import serial
import time

phone = serial.Serial("/dev/ttyUSB0", baudrate=115200, timeout=1.0)  # setting connect to module with serial port

local_contact_no = input("Enter Contact No.: ")  # local variables created to debug this code 
local_message = input("Enter message(less than 50 words):")  # local variables created to debug this code


def send_sms(contact_no, message):
    phone.write('AT+CMGF=1' + '\r\n')  # setting SIM900 Module to Text Mode
    result = phone.read(10)
    print(result)
    time.sleep(1)

    phone.write('AT+CMGS="{0}"'.format(contact_no) + '\r\n')  # setting phone no. to SIM900 Module
    result = phone.read(10)
    print(result)
    time.sleep(1)

    phone.write(message + '\r\n')  # sending message from function
    result = phone.read(10)
    print(result)

    phone.write("\x1A")  # closing message function
    for i in range(10):
        result = phone.read(10)
        print(result)


send_sms(local_contact_no, local_message)
