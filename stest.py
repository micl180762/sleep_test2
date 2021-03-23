import time
starttime = time.time()


def get_all():
    print('all_us')

while True:
    get_all()
    time.sleep(10.0 - ((time.time() - starttime) % 10.0))