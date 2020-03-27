import socket
import threading
from multiprocessing import JoinableQueue

lock = threading.Lock()

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', port))
        s.close()
    except Exception, e:
        if 'Address already in use' in e:
            with lock:
                print('port', port, 'already in use')
        else:
            with lock:
                print('exception message', e)

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = JoinableQueue()

for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(8000, 65535):
    q.put(worker)