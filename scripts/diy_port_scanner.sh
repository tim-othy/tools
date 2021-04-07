#!/bin/bash

if [ -z "$1" ]; then
	echo "Usage : $0 <ip>"
	exit 0
fi

for port in {1..65535}; do
	timeout .1 bash -c "echo > /dev/tcp/$1/$port" && echo "port $port is open"
done
echo "Done"
