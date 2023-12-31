# https://pythontic.com/modules/socket/udp-client-server-example
import socket
import os
import signal

localIP     = "127.0.0.1"
localPort   = 20001

bufferSize  = 1024
msgFromServer       = "Server acknowledges receipt"
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.settimeout(10)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "\tClient IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)

   

    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)