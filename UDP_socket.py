import socket


class UdpSocket:
    def __init__(self, prt, dle_s='1002', dle_e='1003'):
        self.sock = None
        self.dle_s = dle_s
        self.dle_e = dle_e
        self.prt = prt
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', self.prt))  # open socket

    def datarcv(self):
        data = self.sock.recv(4096) # get 4096 bytes from socket
        return data
