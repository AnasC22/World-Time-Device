# LCD Imports
import time
import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# API Imports
from WorldTime_API import getTime

#LED Strip Imports
from neopixel import Neopixel
import utime

from machine import Pin

# LED dotlight
current_city = 1
led_tokyo = Pin(14, Pin.OUT)
led_nyc = Pin(13, Pin.OUT)
led_london = Pin(12, Pin.OUT)
led_SA = Pin(11, Pin.OUT)
led_moscow = Pin(10, Pin.OUT)
led_dubai = Pin(9, Pin.OUT)
led_dhaka = Pin(8, Pin.OUT)
led_edmonton = Pin(4, Pin.OUT)
led_sydney = Pin(6, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

#LCD VARS
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

print("Running main...")

sda = machine.Pin(18)
scl = machine.Pin(19) # NOTE: It is important you change this to match the SDA and SCL pins you are using.
i2c_controller = 1    # Also change this to match the controller you are using (Listed on the Raspberry Pi Pico W Pinout as "I2C0" or "I2C1")
                      # You will need to wire the LCD to your Pi Pico, ensuring that each pin goes to the correct header. The pinout should be written on the LCDs PCB.
                      # You can use either 5V power via VBUS or 3.3V power via either VSYS or 3V(OUT).

i2c = I2C(i2c_controller, sda=sda, scl=scl, freq=400000) 
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
    
currentString = "Tokyo 12:34 pm"
currentTime = []
#LED VARS
numpix = 30
pixels = Neopixel(numpix, 0, 28, "RGB")

pixels[29] = (128, 128, 128)
pixels[28] = (0, 0, 100)
pixels[27] = (8, 5, 94)
pixels[26] = (16, 10, 87)
pixels[25] = (24, 15, 81)
pixels[24] = (32, 20, 75)
pixels[23] = (40, 25, 69)
pixels[22] = (48, 30, 63)
pixels[21] = (56, 35, 57)
pixels[20] = (64, 40, 51)
pixels[19] = (30,60, 0)
pixels[18] = (45, 100,0)
pixels[17] = (50, 100, 0)
pixels[16] = (55, 60, 0)
pixels[15] = (104, 65, 22)
pixels[14] = (112, 70, 16)
pixels[13] = (104, 65, 22)
pixels[12] = (112, 75, 20)
pixels[11] = (112, 70, 16)
pixels[10] = (120, 75, 20)
pixels[9] = (120, 75, 10)
pixels[8] = (100, 160, 0)
pixels[7] = (95,155,0)
pixels[6] = (95,120,0)             
pixels[5] = (90, 150, 0)
pixels[4] = (85, 145, 0)
pixels[3] = (80, 140, 0)
pixels[2] = (75, 135, 0)
pixels[1] = (70, 120, 0)
pixels[0] = (95,1500,0)



pixels.show()
currentTime = getTime()
print(currentTime)
while True:
    if button.value():
        if(current_city == 1):
            led_edmonton.toggle()
            current_city += 1
            lcd.clear()
            lcd.putstr(f"Edmonton Time:  {currentTime[0]}")
            
        elif(current_city == 2):
            led_edmonton.toggle()
            led_nyc.toggle()
            current_city += 1
            lcd.clear()
            lcd.putstr(f"NYC Time {currentTime[1]}")
            
        elif(current_city == 3):
            led_nyc.toggle()
            led_london.toggle()
            current_city += 1
            lcd.clear()
            lcd.putstr(f"London Time     {currentTime[2]}")
            
        elif(current_city == 4):
            led_london.toggle()
            led_SA.toggle()
            current_city += 1
            lcd.clear()
            lcd.putstr(f"Johannesburg    Time {currentTime[3]}")
            
        elif(current_city == 5):
            led_SA.toggle()
            led_moscow.toggle()
            current_city += 1
            lcd.clear()
            lcd.putstr(f"Moscow Time     {currentTime[4]}")
            
        elif(current_city == 6):
            led_moscow.toggle()
            led_dubai.toggle()
            current_city += 1
            lcd.clear()
            lcd.putstr(f"Dubai Time {currentTime[5]}")
            
        elif(current_city == 7):
            led_dubai.toggle()
            led_dhaka.toggle()
            current_city += 1
            lcd.clear()
            lcd.putstr(f"Dhaka Time {currentTime[6]}")
            
        elif(current_city == 8):
            led_dhaka.toggle()
            led_tokyo.toggle()
            current_city += 1
            lcd.clear()
            lcd.putstr(f"Tokyo Time {currentTime[7]}")
            
        elif(current_city == 9):
            led_tokyo.toggle()
            led_sydney.toggle()
            current_city += 1
            lcd.clear()
            lcd.putstr(f"Sydney Time     {currentTime[8]}")
            
        elif(current_city >= 10):
            led_sydney.toggle()
            current_city = 1
            lcd.clear()
            lcd.putstr("Retrieving Data . . .")
            currentTime = getTime()
            print(currentTime)
            lcd.clear()
            lcd.putstr("Data received.  Click to cont.")
            
        time.sleep(0.5)
