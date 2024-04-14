from gpiozero import LED, Button
import signal

led = LED(17)
button = Button(6)

button.when_pressed = led.on
button.when_released = led.off

signal.pause()
