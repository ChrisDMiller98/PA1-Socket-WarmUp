
import socket
import sys  
import platform 
import subprocess

# Leftover ping function
def ping(host):

    param = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0
  
try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print ("Socket successfully created")
except socket.error as err: 
    print ("socket creation failed with error %s" %(err)) 
# Enter port here
port = 44713
  
try: 
    # Enter IP here
    host_ip = socket.gethostbyname('10.30.1.102') 
except socket.gaierror: 
  
    print ("there was an error resolving the host")
    sys.exit() 
  
# connecting to the server 
s.connect((host_ip, port)) 

# message sent to server
s.send('chrdmill\n'.encode()) 
data = ''
data = s.recv(1024).decode()
print (data)
  
print ("the socket has successfully connected to site \ on port == %s" %(host_ip)) 
