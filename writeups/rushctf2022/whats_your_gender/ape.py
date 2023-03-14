#!/usr/bin/env python3

from scapy.all import rdpcap


def decode_binary_string(s):
    """Converting the byts to string"""
    byte_string = ''.join(chr(int(s[i*8:i*8+8], 2)) for i in range(len(s)//8))
    return byte_string


packets = rdpcap('Whats_your_gender.pcap')
count = 0
flag = ""

for pck in packets:
    if pck[IP].src != "1.2.3.4":
        flag += pck[IP].dst[-3]+pck[IP].dst[-1]
        count += 1
        if count % 4 == 0:
            flag += ""

print(decode_binary_string(flag))
