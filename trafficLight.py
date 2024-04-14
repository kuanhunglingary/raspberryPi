from gpiozero import Button, TrafficLights, Buzzer

button = Button(26)
lights = TrafficLights(6, 13, 19)
buzzer = Buzzer(5)

while True:
    lights.on()
    buzzer.beep()
    button.wait_for_press()
    lights.off()
    buzzer.on()
    button.wait_for_press()
