
from machine import Pin, I2C
import time
import dht 
import ssd1306
sensor=dht.DHT11(Pin(16,Pin.In, Pin PULL_UP))
oled=ssd1306.SSD1306_12C(128,64,i2c)
i2c = I2C(0, scl=Pin(22), sda=Pin (21))
last_valid_temp = "--"
last_valid_hum= "--"
temp_str = "Waiting..."
hum_str = "Waiting..."
from machine import Pin, I2C
    i2c=I2C(0, scl=Pin(22), sda=Pin(21))
    print("Scanning digital I2C bus...")
    devices=i2c.scan()
    if len(devices) == 0
    print("Error no I2C devices found")
    else:
    print("Success! Found devices at addresses")
last_sensor_read = time.ticks.ms()
SENSOR_INTERVAL = 3000
while True:
 try:
 current_time = time.ticks_ms(_)
 sensor.measure()
 last_valid_temp=str(sensor.temperature()) +" C"
 last_valid_hum = str(sensor.humidity())+ "%"
 print("glitch bypassed.keeping last data")
 temp = sensor.temperature
 hum = sensor.humidity
#Display on OLED
 oled.fill(0) 
 oled.text("EP32 MONITOR", 10,0)    
 oled.text("Temp:"+last_valid_temp, 10, 24)
 oled.text("Hum: "+;last_valid_hum,10,44)
 oled.show()

except OSError as e:
     print ("Failed to read sensor Retrying...")
     oled.fill(0)
     oled.text("Reading Sensor",0,20)
     oled.show()
time.sleep(2)
 error_78_count=0
 successful_reads=0
 while True: 
    try:
        current_time = time.ticks_ms()
    if time.ticks_diff(current_time, last_sensor_read)
    try:
        sensor.measure()
        temp = sensor.temperature
        hum = sensor.humidity
      temp_str = "Temp: {} C".format(temp)
      hum_str = "Hum: {} %".format(hum)
        print(f"Success #{succesful_reads}) - T: {sensor.temperature()}")
        except OSError as e:
            error_78_count += 1
            print(f"Data corruption caught ({error_78_count} drops). Retrying..")
    last_sensor_read = current_time
    
oled.fill(0)
    oled.text(temp_str,0,20)
    oled.text(hum_str,0,40)
    oled.show()