import json
import threading
from time import time, sleep

from gpio.Sensors import Sensors


class Logger(threading.Thread):
    def __init__(self):
        super().__init__()
        self.s = Sensors()
        self.s.start()

        self.start_time = time()
        self.points = []

        self.running = True

    def run(self):
        while self.running:
            data = self.s.emit()
            frame_time = time() - self.start_time

            self.points.append({
                'data': data,
                'time': frame_time
            })

            with open('data.json', 'w') as f:
                json.dump(self.points, f)

            sleep(0.075)

    def stop(self):
        self.running = False
        self.s.stop()
