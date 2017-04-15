# tcp-halfandmultiply-packet
a tcp client and a tcp server communicate with each other. What the server gets in one 'recv' can not be guaranteed to be the complete packet based on the protocol. Very likely, it could be multiply packets plus half packet.

There are many things you should aware of when you run the program:

1. multiply complet packets with two not complet packets are of the most cases after first recv
2. the send in client is blocked after short time
3. after block, the send will continue after many recv in server
4. if the client is stopped, the server will be aware of the disconnection immediately so that the data in buffer will be lost
