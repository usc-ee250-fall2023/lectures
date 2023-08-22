# https://pythontic.com/modules/socket/udp-client-server-example
import socket

serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.settimeout(5)

msgFromClient       = input("Message to send:")
bytesToSend         = str.encode(msgFromClient)

# Send to server using created UDP socket
while(msgFromClient != "quit"):
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server {}".format(msgFromServer[0])
    print(msg)
    msgFromClient       = input("Message to send:")
    bytesToSend         = str.encode(msgFromClient)
