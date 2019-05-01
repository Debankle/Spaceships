import sys
import socket
from enum import Enum
from threading import Thread


class State(Enum):
    LOBBY = 1
    INGAME = 2


class Room(object):
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = socket.gethostname()
        self.host = socket.gethostbyname(self.name)
        self.port = 38493
        self.socket.bind((self.host, self.port))

        self.gameData = dict()

    def lobby(self):
        self.socket.listen(4)

        while True:
            conn, addr = self.socket.accept()