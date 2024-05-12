import time
import network
import urequests
ssid = 'WIFI Network Name'
password = 'PASSWORD'


def connect():
    # Connect to WLAN
    # Connect function from https://projects.raspberrypi.org/en/projects/get-started-pico-w/2
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid,password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(1)
try:
    connect()
    

except KeyboardInterrupt:
    machine.reset()


last_call = 0
def checkCall():
    global last_call
    if time.time() - last_call >= 60:
        getTime()

times = []
def getTime():
    Edmonton = urequests.get("http://worldtimeapi.org/api/timezone/America/Edmonton")
    Edmonton_data = Edmonton.json()
    Edmonton_date = Edmonton_data['datetime'][:10]
    Edmonton_time = Edmonton_data['datetime'][11:16]
    Edmonton.close()

    NYC = urequests.get("http://worldtimeapi.org/api/timezone/America/New_York")
    NYC_data = NYC.json()
    NYC_date = NYC_data['datetime'][:10]
    NYC_time = NYC_data['datetime'][11:16]
       
    NYC.close()
    
    London = urequests.get("http://worldtimeapi.org/api/timezone/Europe/London")
    London_data = London.json()
    London_date = London_data['datetime'][:10]
    London_time = London_data['datetime'][11:16]  
    London.close()
    
    SA = urequests.get("https://worldtimeapi.org/api/timezone/Africa/Johannesburg")
    SA_data = SA.json()
    SA_date = SA_data['datetime'][:10]
    SA_time = SA_data['datetime'][11:16]  
    SA.close()
    
    Moscow = urequests.get("http://worldtimeapi.org/api/timezone/Europe/Moscow")
    Moscow_data = Moscow.json()
    Moscow_date = Moscow_data['datetime'][:10]
    Moscow_time = Moscow_data['datetime'][11:16]  
    Moscow.close()
     
    Dubai = urequests.get("http://worldtimeapi.org/api/timezone/Asia/Dubai")
    Dubai_data = Dubai.json()
    Dubai_date = Dubai_data['datetime'][:10]
    Dubai_time = Dubai_data['datetime'][11:16]  
    Dubai.close()
    
    Dhaka = urequests.get("http://worldtimeapi.org/api/timezone/Asia/Dhaka")
    Dhaka_data = Dhaka.json()
    Dhaka_date = Dhaka_data['datetime'][:10]
    Dhaka_time = Dhaka_data['datetime'][11:16]  
    Dhaka.close()
     
    Tokyo = urequests.get("http://worldtimeapi.org/api/timezone/Asia/Tokyo")
    Tokyo_data = Tokyo.json()
    Tokyo_date = Tokyo_data['datetime'][:10]
    Tokyo_time = Tokyo_data['datetime'][11:16]  
    Tokyo.close()

    Sydney = urequests.get("http://worldtimeapi.org/api/timezone/Australia/Sydney")
    Sydney_data = Sydney.json()
    Sydney_date = Sydney_data['datetime'][:10]
    Sydney_time = Sydney_data['datetime'][11:16]  
    Sydney.close()

    global times
    print(f"{[Edmonton_time, NYC_time, London_time, SA_time, Moscow_time, Dubai_time, Dhaka_time, Tokyo_time, Sydney_time]}")
    return [Edmonton_time, NYC_time, London_time, SA_time, Moscow_time, Dubai_time, Dhaka_time, Tokyo_time, Sydney_time]

getTime()