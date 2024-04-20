# Learn raspberry pi 5
### Download Raspberry Pi OS using Raspberry Pi Imager for Raspberry Pi 5
[video](https://youtu.be/0u6iflSzwp0)

Follow the officail guide tutorial "Physical Computing with Python"
[Tutorial](https://projects.raspberrypi.org/en/projects/physical-computing/0)

### LED flashing on and off
[flashLED.py](./flashLED.py)

### Use buttons to get input
[gpio_button.py](./gpio_button.py)

### Use button to control the LED
[gpio_control](./gpio_control.py)

### Press or release button to control LED 

### Press the button to turn on the LED or release the button to turn off the LED
[gpio_control_toggle](./gpio_control_toggle.py)

### Create a beep() method for a buzzer
[gpio buzzer](./gpio_buzzer.py)

### Use button to control three LEDs and a buzzer
[traffic light](./gpio_trafficLight.py)

| Component | GPIO pin |
|-----------|----------|
| Button    |    26    |
| Red LED   |     6    |
| Amber LED |    13    |
| Green LED |    19    |
| Buzzer    |     5    |

### Control two potentiometers to adjust teh sensitivity of PIR sensor
[PIR sensor](./gpio_pirSensor.py)

### Use an ultrasonic distance sensor to calculate the distance from the object
[ultrasonic distance sensor](./gpio_ultrasonicDistanceSensor.py)

### ADC(MCP3008) 
[ADC(3008)](./gpio_ADC.py)
1. Adjusted the potentiometer and then my raspberry Pi5 read the voltage. but my potentiometer was broken and just show 0.0004885197850512668
2. Twist the dial when raspberry Pi5 read the voltage.
3. Connect LED to the potentiometer and turn the dial to change the LED brightness.
