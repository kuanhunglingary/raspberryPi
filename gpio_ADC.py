# 1. Adjusted the potentiometer and then my raspberry Pi5 read the voltage. 
# from gpiozero import MCP3008
# pot = MCP3008(0)
# print(pot.value)

# 2. Twist the dial when raspberry Pi5 read the voltage.
# from gpiozero import MCP3008
# pot = MCP3008(0)
# while True:
#     print(pot.value)

# 3. Connect LED to the potentiometer and turn the dial to change the LED brightness.
from gpiozero import MCP3008
pot = MCP3008(0)
from gpiozero import PWMLED
# Create a PWMLED object on pin 26:
led = PWMLED(26)
led.on()
led.off()
led.value = 0.0004885197850512668
led.source = pot.values
while True:
    led.value = pot.value