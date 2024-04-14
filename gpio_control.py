from gpiozero import LED, Button
import time

led = LED(17)
button = Button(6)

button.wait_for_press()
led.on()
time.sleep(3)
led.off()
