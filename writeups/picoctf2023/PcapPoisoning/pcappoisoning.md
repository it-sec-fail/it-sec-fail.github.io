---
layout: page
---

# <span style="color: cyan;">webuser</span>@<span style="color: darkorange;">security-client</span>:~$ <span style="color: white;">ls -la</span>  /home/w3ich3rt/writeups/picoctf2023/money-aware
total 78
drwxr-xr-x 10 w3ich3rt w3ich3rt  4096 Oct 14 22:15 .
drwxr-xr-x  3 root     root      4096 Dec 26  2021 ..
lrwxrwxrwx  1 w3ich3rt w3ich3rt    30 Mar 23 13:18 .home -> [/../../home](/)
lrwxrwxrwx  1 w3ich3rt w3ich3rt    30 Mar 23 13:18 .home -> [../writeups](/writeups.md)
lrwxrwxrwx  1 w3ich3rt w3ich3rt    30 Mar 23 14:53 .[back](/writeups/picoctf2023/picoctf_readme)
-rw-rw-rw-  1 Mr81u35ky Mr81u35ky  30 Mar 23 13:18 .solve.md

# <span style="color: cyan;">webuser</span>@<span style="color: darkorange;">security-client</span>:~$ <span style="color: white;">cat</span>  /home/w3ich3rt/writeups/picoctf2023/rules/solve.md

Writeup from: Mr81u35ky

## PcapPoisoning

Given was a pcap file.
Opened it with wireshark had just a first look and scrolled through the requests.

> picoCTF{P64P_4N4L7S1S_SU55355FUL_ba1a6097}
