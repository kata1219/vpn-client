import subprocess
import socket

def connect_to_vpn(config_file):
    process = subprocess.Popen(['openvpn', '--config', config_file])

    while True:
        try:
            sock = socket.create_connection(('140.113.169.90', 1194), timeout=10)
            break
        except socket.error:
            continue

    print('CONNECT SUCCESS!')
    process.terminate()

connect_to_vpn('./config/client1.ovpn')
