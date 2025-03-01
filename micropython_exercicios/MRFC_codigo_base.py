#Codigo base do mrfc

#PINAGEM: RST-4    SDA-5    SCK-18    MISO-19    MOSI-23

from mfrc522 import MFRC522
from machine import Pin
from machine import SPI
import time


spi = SPI(2, baudrate=2500000, polarity=0, phase=0)
spi.init()
rdr = MFRC522(spi=spi, gpioRst=4, gpioCs=5)

while True:
    (stat, tag_type) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            card_id = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
   
            print(card_id)
sleep(0.1)
