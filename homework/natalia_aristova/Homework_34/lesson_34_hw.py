from datetime import datetime
from time import sleep
import requests

while True:
    requests.get('https://www.cms.org.cy/')
    print(datetime.now())
    sleep(2)
