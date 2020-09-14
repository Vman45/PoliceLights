from gpiozero import LED
from time import sleep


def flash(led):
    led.off()
    sleep(0.1)
    led.on()
    sleep(0.1)





if __name__ == "__main__":
    left_red = LED(23)
    sleep(0.5)
    right_red = LED(24)
    sleep(0.5)
    left_blue = LED(4)
    sleep(0.5)
    right_blue = LED(25)
    sleep(0.5)
    left_red.on()
    right_red.on()
    left_blue.on()
    right_blue.on()

    for x in range(0, 50):
        flash(left_red)
        flash(right_red)
