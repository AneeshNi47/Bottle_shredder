import RPi.GPIO as GPIO
import keyboard
from gsm_module import send_sms

GPIO.setmode(GPIO.BCM)
IR_in = 4
LED_out = 14
GPIO.setup(IR_in, GPIO.IN)
GPIO.setup(LED_out, GPIO.OUT)
run_status = True


def count_bottle():
    status = 0
    count = 0
    while run_status:
        try:
            if GPIO.input(IR_in):
                if GPIO.input(IR_in) != status:
                    count = count + 1
                    print("Added 1 bottle")
                GPIO.output(LED_out, 1)
                status = GPIO.input(IR_in)
            else:
                if GPIO.input(IR_in) != status:
                    print("Waiting")
                GPIO.output(LED_out, 0)
                status = GPIO.input(IR_in)
        except:
            print("error")

        question = input("Do you want to Add more:?")
        if question == 'Y' or question == 'y':
            run_status = True
        else:
            run_status = False
        if run_status == False:
            contact_no = input("Enter Mobile NO.: ")
            message = "You Have Added {0} bottle".format(count)
            send_sms(contact_no, message)
        if keyboard.is_pressed('esc'):
            exit()


count_bottle()
