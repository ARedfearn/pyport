import socket

def portscan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', port))
        s.close()
    except Exception, e:
        if 'Address already in use' in e:
            print('port', port, 'already in use')
        else:
            print('exception message', e)


for i in range(8080, 8082):
    portscan(i)