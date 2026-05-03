import socket
targets = ["127.0.0.1", "10.0.0.5", "10.0.0.6"]
for ip in targets:
    print(f"--- Checking Server: {ip} ---")


    # Create the socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # Set a 1-second timeout so we don't wait forever
    s.settimeout(1)


    # Knock on Port 22 (SSH)
    result = s.connect_ex((ip, 22))

    # 0 means Open, anthing else means Closed
   	if result == 0:
            print(f"SUCCESS: Port 22 is OPEN on {ip}")
	else:
	    print(f"FAILED: Port 22 is CLOSED on {ip}")

	# Close the connection
	s.close()
