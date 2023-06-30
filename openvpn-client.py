import subprocess
import time

def connect_to_vpn():
    config_file = './config/client1.ovpn'
    connect_proc = subprocess.Popen(['sudo', 'openvpn', '--config', config_file], stdout=subprocess.PIPE)
    
    while True:
        output = connect_proc.stdout.readline()
        if output:
            print(output)
            if 'Initialization Sequence Completed' in str(output):
                time.sleep(0.5)
                ping_test()
                connect_proc.send_signal(4)
                break
    
    return connect_proc

def ping_test():
    subprocess.run(['ping', '8.8.8.8', '-c 3', '-I', '10.8.0.2'])
    
if __name__ == "__main__":
    connect_to_vpn() 
    