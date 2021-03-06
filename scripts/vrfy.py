#!/bin/python

import socket
import sys


if len(sys.argv) != 3:
    print("Usage: vrfy.py <ip> <username-file>")
    sys.exit(0)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((sys.argv[1], 25))
banner = s.recv(1024)

print(banner)

with open(sys.argv[2], 'r') as usernames:
    for username in usernames:
        s.send("VRFY " + sys.argv[2] + "\r\n")
        result = s.recv(1024)
        print(result)

s.close()

