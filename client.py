import sys
import time 
from scapy.all import *

pkt = None


def make(character, dest):
	letter = ord(character)
	pkt = IP(dst=dest)/TCP(sport=letter, dport=RandNum(0, 8000), flags="C")
	return pkt


def client():
	dest = raw_input("Enter the destination IP: ")
	while True:
		message = raw_input('Enter your message: ')
		message += "\n"
		print "Sending data: " + message
		for i in message:
			new_pkt = make(i, dest)
			send(new_pkt)
			time.sleep(RandNum(0, 10))


client()
