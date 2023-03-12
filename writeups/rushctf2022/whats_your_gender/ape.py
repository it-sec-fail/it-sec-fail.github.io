#!/usr/bin/env python3

from scapy.all import *

packets = rdpcap('Whats_your_gender.pcap')

for packet in packets:
    print(packet.load)