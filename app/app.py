import time
import random
import os
import requests
# allow for HBM to start
time.sleep(5)
# Register app with the HBM
r = requests.post('http://172.18.0.1:5000/apps', data = {'name':os.environ['APP_NAME']})
id = r.json()['id']
while True:
    if random.random() > 0.9:
        time.sleep(15)
    requests.put('http://172.18.0.1:5000/app/'+str(id), data = {'status':'ok'})
    time.sleep(5)
