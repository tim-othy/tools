#!/bin/python

# Generate hex codes to check for bad-characters in shellcode.

import sys

for i in range(1, 256):
    sys.stdout.write("\\x" + "{:02x}".format(i))

