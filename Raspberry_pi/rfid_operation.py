# RFID Read

import RPi.GPIO as gpio
from mfrc522 import SimpleMFRC522
cardRead = SimpleMFRC522()

print("Scanning...")
print("to cancel press ctrl+c")
try:
    id, text = cardRead.read()
    print("ID: %s\nText: %s" % (id,text))
finally:
    gpio.cleanup()


# RFID Write

import RPi.GPIO as gpio
from mfrc522 import SimpleMFRC522
cardWrite = SimpleMFRC522()

try:
    text = input("Enter Reg Number for writing: ")
    print("Place the Tag...")
    cardWrite.write(text)
    print("Done...")
finally:
    gpio.cleanup()
