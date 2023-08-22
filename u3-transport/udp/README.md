UDP Broadcast example
=====================

This examle is based on pont.net
change to support UDP broadcast client/server

gcc udpClient.c -o udpClient

gcc udpServer.c -o udpServer

ARM static compile
==================

arm-none-linux-gnueabi-gcc -static udpServer.c -o udpServer-arm

Server side:
============

./udpServer

Client side:
============

./udpClient 255.255.255.255 TEST

Send a broadcast message via UDP

 