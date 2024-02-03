import time
import os
import re
uvival = 0
prevuvi = 0

def send(type):
    if type == "high":
        os.system(f'curl -u connor:!RyR106* -d "The UV is 8+, Please Put on A Hat And SunScreen" https://ntfy.moahub.org/weather')
    elif type == "med":
        os.system(f'curl -u connor:!RyR106* -d "The UV is 5+, Please Put on A Hat or SunScreen" https://ntfy.moahub.org/weather')
    elif type == "semi":
        os.system(f'curl -u connor:!RyR106* -d "The UV is 3+, Put on A Hat or SunScreen If You Want To" https://ntfy.moahub.org/weather')
    elif type == "low":
        os.system(f'curl -u connor:!RyR106* -d "The UV is Less Than 3, You Dont Need To Put On a Hat Or SunScreen" https://ntfy.moahub.org/weather')

while True:
    uvi = os.popen('curl -s "http://api.openweathermap.org/data/2.5/onecall?lat=-32.03738658217749&lon=115.78388761224882&appid=ada1f715672a438e9b9acaa7ea0e930b" | jq ".current.uvi"').read()
    if uvi == "null\n":
        uvi = 0
    if uvi:
        uvival = str(uvi)
        uvival = uvival.split('.')
        uvival = uvival[0]
        uvival = int(uvival)
        if uvival > 7:
            uvival = int(10)
        elif uvival > 4 and uvival < 8:
            uvival = int(6) 
        elif uvival > 2 and uvival < 5:
            uvival = int(4) 
        elif uvival < 3:
            uvival = int(1)
    if not uvival == prevuvi:
        if uvival == 10:
            send("high")
        elif uvival == 6:
            send("med")
        elif uvival == 4:
            send("semi")
        elif uvival == 1: 
            send("low")
    else:
        print("uvi not changed")
    print("slept")
    #time.sleep(600)
    print(uvival)
    print(prevuvi)
    prevuvi = uvival

