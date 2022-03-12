from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

sense.clear()

w = (255, 255, 255)
g = (0, 255, 0)
e = (0, 100, 0)
b = (0, 0, 0)

icon = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    e, g, g, g, b, b, w, w,
    e, g, g, g, b, w, b, b,
    b, e, g, b, b, w, b, w,
    b, e, g, b, b, w, b, w,
    e, g, b, g, b, b, w, b,
]

sense.set_pixels(icon)


sense.set_pixel(1, 1, (255, 255, 255))
sleep(1)
sense.set_pixel(2, 1, (255, 255, 255))
sleep(1)
sense.set_pixel(3, 1, (255, 255, 255))
sleep(1)
sense.set_pixel(4, 1, (255, 255, 255))
sleep(0.7)
sense.set_pixel(5, 1, (255, 255, 255))
sleep(0.7)
sense.set_pixel(6, 1, (255, 255, 255))
sleep(2)

sense.show_message("Tundra Campsite 2.1.3", text_colour=(255, 255, 255), scroll_speed=(0.04))

sense.clear(255, 255, 255)

#1
sense.set_pixel(2, 1, (100, 10, 0))
sense.set_pixel(3, 1, (100, 10, 0))
sense.set_pixel(4, 1, (100, 10, 0))
sense.set_pixel(5, 1, (100, 10, 0))
sense.set_pixel(6, 1, (100, 10, 0))
#2
sense.set_pixel(7, 2, (100, 10, 0))
sense.set_pixel(7, 3, (100, 10, 0))
sense.set_pixel(7, 4, (100, 10, 0))
sense.set_pixel(7, 5, (100, 10, 0))
sense.set_pixel(7, 6, (100, 10, 0))
#3
sense.set_pixel(6, 7, (100, 10, 0))
sense.set_pixel(5, 7, (100, 10, 0))
sense.set_pixel(4, 7, (100, 10, 0))
sense.set_pixel(3, 7, (100, 10, 0))
sense.set_pixel(2, 7, (100, 10, 0))
#4
sense.set_pixel(1, 2, (100, 10, 0))
sense.set_pixel(1, 3, (100, 10, 0))
sense.set_pixel(1, 4, (100, 10, 0))
sense.set_pixel(1, 5, (100, 10, 0))
sense.set_pixel(1, 6, (100, 10, 0))


while True:
    x = randint(3, 5)
    y = randint(3, 5)
    r = randint(0, 255)
    g = randint(0, 0)
    b = randint(0, 0)
    sense.set_pixel(x, y, r, g, b)
    sleep(0.01)
    
