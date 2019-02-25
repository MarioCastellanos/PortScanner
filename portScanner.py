
#used to connect to server and ports

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.settimeout(2)

port = 1000

for port in range(1,100):
    try:
        s.connect(('ad.samsclass.info', port))
        r = s.recv(1024)
        if 'Congratulations' in r.decode('utf8'):
            print('[!]HIDDEN SERVICE FOUND: %s ~ %s' % (port, r.decode('utf8')))
            s.close()
            break
        else:
            print('%s ~ %s' % (port, r.decode('utf8')))
            s.close()
    except socket.error as err:
        print('%s ~ %s'% (port, err))
    port += 1000
