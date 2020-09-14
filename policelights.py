from gpiozero import LED
from time import sleep


def flashlights():
    led = LED(4)
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)

def setupled():
    left_red = LED(23)
    sleep(.5)
    right_red = LED(24)
    sleep(.5)
    left_blue = LED(4)
    sleep(.5)
    right_blue = LED(25)
    sleep(.5)
    left_red.on()
    right_red.on()
    left_blue.on()
    right_blue.on()

if __name__ == "__main__":
    setupled()
    # for x in range(0, 50):
        # pass
