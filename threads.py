import threading


def action():
    for _ in range(1000):
        print('Current thread name (function): {}'.format(threading.current_thread().name))


for _ in range(100):
    thread = threading.Thread(target=action)
    thread.start()


class Worker(threading.Thread):
    def run(self):
        for _ in range(1000):
            print('Current thread name (class): {}'.format(threading.current_thread().name))


for _ in range(100):
    thread = Worker()
    thread.start()
