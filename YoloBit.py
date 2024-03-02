from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1

while True:
  pin14.write_analog(round(translate(70, 0, 100, 0, 1023)))
