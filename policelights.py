from gpiozero import LED
from time import sleep


def flashlights():
    led = LED(4)
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)


if __name__ == "__main__":
    left_red = LED(4)
    left_red.on()
    left_red.off()
    sleep(10)
    # for x in range(0, 50):
        # pass
