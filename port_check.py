import socket
targets = ["127.0.0.1", "10.0.0.5", "10.0.0.6"]
for ip in targets:# Create the socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a 1-second timeout so we don't wait forever
    s.settimeout(1)
    
    # The actual "knock" on Port 22 (SSH)
    result = s.connect_ex((ip, 22))
