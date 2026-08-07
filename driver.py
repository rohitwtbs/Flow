import time
import random
class MyApiDriver:
    def __init__(self):
        pass
    def setup(self):
        pass
    def do_poll(self):
        occupancy_values = [0,1,2]
        fake_data = random.choice(occupancy_values)
        print('fake_data', fake_data)
        pass

interval = 5
driver = MyApiDriver()
while True:
    driver.do_poll()
    time.sleep(interval)

