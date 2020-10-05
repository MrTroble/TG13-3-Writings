import threading


def test():
    print(threading.current_thread().getName())


for x in range(10000):
    threading.Thread(None, test).start()