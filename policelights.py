from gpiozero import LED
from time import sleep


def flash(led1, led2):
    led1.off()
    led2.off()
    sleep(0.07)
    led1.on()
    led2.on()
    sleep(0.07)





if __name__ == "__main__":
    for x in range(0, 50)
    xmas = LED(22)
    xmas.off()
    sleep(0.1)