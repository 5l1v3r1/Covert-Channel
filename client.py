#!/usr/bin/python
# -----------------------------------------------------------------------------
# FUNCTION:       Covert Channel
#
# DATE:           September 19, 2017
#
# DESIGNERS:      Paul Cabanez
#
# PROGRAMMERS:    Paul Cabanez
#
# NOTES: Using Scapy, creates a packet with a message embedded into the source
#		 source port, and sending to a desired IP using a random port.
#
#
# ----------------------------------------------------------------------------*/

import sys
import time
from scapy.all import *

pkt = None

# Converts a letter into unicode, using Scapy, embeds the message into the
# source port. Uses random destination port, and marks the packet with a C flag
#------------------------------------------------------------------------------
def make(character, dest):
	letter = ord(character)
	pkt = IP(dst=dest)/TCP(sport=letter, dport=RandNum(0, 8000), flags="C")
	return pkt

# Asks for IP and message to send
# for every letter in the message, create a packet and send it, then sleep to
# delay the sending of the messages
#------------------------------------------------------------------------------
def client():
	dest = raw_input("Enter the destination IP: ")
	while True:
		message = raw_input('Enter your message: ')
		message += "\n"
		for i in message:
			new_pkt = make(i, dest)
			send(new_pkt)
			time.sleep(RandNum(0, 10))


client()
