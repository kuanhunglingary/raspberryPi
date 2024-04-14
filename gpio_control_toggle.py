from gpiozero import LED, Button
import time

led = LED(17)
button = Button(6)

while True:
    button.wait_for_press()
    led.toggle()
    time.sleep(0.5)
