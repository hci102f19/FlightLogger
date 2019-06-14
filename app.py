import json
from time import time, sleep

from gpio.Sensors import Sensors

s = Sensors()
s.start()

start_time = time()
points = []

while True:
    data = s.emit()
    sleep(0.1)
    frame_time = time() - start_time

    points.append({
        'data': data,
        'time': frame_time
    })

    with open('data.json', 'w') as f:
        json.dump(points, f, indent=4)
