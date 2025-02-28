from machine import Pin

led = Pin(13, Pin.OUT)
led1 = Pin(12, Pin.OUT)
led2 = Pin(14, Pin.OUT)

led1.value (0)
led2.value (0)

estado = 0

while True:
    try:
        estado = int(input("1/0: "))
    except:
        print("Erro")
            
    if estado == 1:
        led.value(1)
    else:
        led.value(0)