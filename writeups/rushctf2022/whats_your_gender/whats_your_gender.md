# What's your gender?
Easy
Category: Forensics

## Challenge description

I identify as Binary Packetsexual!

Can you look at this pcap file and help me find the flag?

Flag: RUSH{ALLCAPSMESSAGE}

[PCAP-File](Whats_your_gender.pcap)

![Challenge Picture](whats-your-gender.png) 

## Solving

Looking at the `pcap`-File with `Wireshark` and the python lib `scapy`.
But nothing pops up... :-D

Checked without result:
 [x] `strings`
 [x] `wireshark`
 [x] `tshark`
 [x] `scapy`

### Scapy script

Here is the current version of the python script:

```python
#!/usr/bin/env python3

from scapy.all import *

packets = rdpcap('Whats_your_gender.pcap')

for packet in packets:
    print(packet.load)
```