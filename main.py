from machine import Pin
from time import sleep

bot1=Pin(28, Pin.IN)
bot2=Pin(27, Pin.IN)
led1=Pin(1, Pin.OUT)
led2=Pin(2, Pin.OUT)


while 1:
  if bot1.value() == 1:
    led1.on()
  else:
    led1.off()
  
  if bot2.value() == 1:

    if led2.value() == 0:
      led2.on()
  
    elif led2.value() == 1:
      led2.off()

    sleep(.5)

