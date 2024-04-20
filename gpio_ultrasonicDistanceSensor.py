from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=15, trigger=18)
while True:
    print(ultrasonic.distance)
