import socket

# Function to scan a port
def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)  # Set timeout to 1 second
    result = s.connect_ex((ip, port))
    s.close()
    
    if result == 0:
        return True
    return False

# Get user input
target = input("Enter the target IP or website: ")

# Common ports to scan
ports = [21, 22, 23, 25, 53, 80, 443, 8080]

print(f"\nScanning {target}...\n")

# Scan each port
for port in ports:
    if scan_port(target, port):
        print(f"Port {port} is OPEN")
    else:
        print(f"Port {port} is CLOSED")

print("\nScanning Completed!")