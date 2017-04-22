import os

pid = os.fork()
if pid:
    for _ in range(10000):
        print('Parent process')
else:
    for _ in range(10000):
        print('Child process')
