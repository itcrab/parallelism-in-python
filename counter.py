import threading
import time

counter = 0
lock = threading.Lock()


def inc():
    global counter

    with lock:
        value = counter
        time.sleep(0.001)
        counter = value + 1


pool = []
for _ in range(1000):
    th = threading.Thread(target=inc)
    th.start()

    pool.append(th)

for th in pool:
    th.join()

print(counter)
