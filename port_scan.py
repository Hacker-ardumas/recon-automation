import socket

target = input("Enter IP: ")
port = 80

s = socket.socket()
result = s.connect_ex((target, port))

if result == 0:
    print("Port open")
else:
    print("Port closed")
