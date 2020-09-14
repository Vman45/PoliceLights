from gpiozero import LED
from time import sleep


def flash(led1, led2):
    led1.off()
    led2.off()
    sleep(0.1)
    led1.on()
    led2.on()
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

    for x in range(0, 10):
        flash(left_red, left_blue)
        flash(left_red, left_blue)
        
        flash(right_red, right_blue)
        flash(right_red, right_blue)
