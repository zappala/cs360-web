#!/usr/bin/env python

"""
A simple echo server and client that uses UDP broadcast
"""

import optparse
import socket
import sys
import threading
import time

class Broadcast(threading.Thread):
    def __init__(self,port):
        threading.Thread.__init__(self)
        threading.Thread.daemon = True
        self.host = ''
        self.port = port
        self.open_socket()

    def open_socket(self):
        # create socket
        self.sock = None
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            self.sock.bind((self.host,self.port))
            print "Broadcast: ", self.sock.getsockname()
        except socket.error, (code,message):
            print "Could not open socket: " + message
            sys.exit(1)

    def run(self):
        size = 1024
        while True:
            data,address = self.sock.recvfrom(size)
            print "Responding to: ", address
            self.sock.sendto(data,address)


class Input(threading.Thread):
    def __init__(self,port):
        threading.Thread.__init__(self)
        threading.Thread.daemon = True
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        print "Input: ", self.sock.getsockname()

    def run(self):
        size = 1024
        while True:
            data,address = self.sock.recvfrom(size)
            print data

class Output:
    def __init__(self,port,sock):
        self.sock = sock
        self.host = '<broadcast>'
        self.port = port

    def run(self):
        size = 1024
        while True:
            line = raw_input("> ")
            if line == "quit":
                break
            self.sock.sendto(line,(self.host,self.port))
            print "Output: ", self.sock.getsockname()
            time.sleep(0.5)


if __name__ == "__main__":
    # parse options
    parser = optparse.OptionParser(usage = "%prog [options]",
                                   version = "%prog 0.1")
    parser.add_option("-p", "--port", type="int",dest="port",
                      metavar="PORT",default=3000,
                      help="port number for the server")

    (options, args) = parser.parse_args()

    b = Broadcast(options.port)
    b.start()
    i = Input(options.port)
    i.start()
    o = Output(options.port,i.sock)
    o.run()

