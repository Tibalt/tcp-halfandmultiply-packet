# tcp-halfandmultiply-packet
a tcp client and a tcp server communicate with each other. What the server gets in one 'recv' can not be guaranteed to be the complete packet based on the protocol. Very likely, it could be multiply packets plus half packet.
