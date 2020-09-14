from gpiozero import LED
from time import sleep


def flashlights():
    led = LED(4)
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)


if __name__ == "__main__":
    left_red = LED(23)
    sleep(1)
    right_red = LED(24)
    sleep(1)
    left_blue = LED(4)
    sleep(1)
    right_blue = LED(25)
    sleep(1)
    

    sleep(10)
    # for x in range(0, 50):
        # pass
