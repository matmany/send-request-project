import requests
import time
from datetime import datetime

message = "Hey Joe, your PC is on"
url = "https://receive-logs.fly.dev/api/log"
#url = "http://localhost:8000/api/log"
sleepSeconds = 10

currentDateTimeBody = {"date": "", "message": message}


while 1:

    print("Seending...")

    try:
        currentDateTimeBody["date"] = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        requests.post(url, json=currentDateTimeBody)
    except:
        print("Request Failed, verify your connection ")
    else:
        print("Request Succeed, now waiting...")

    time.sleep(sleepSeconds)
