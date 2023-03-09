---
layout: page
---
# <span style="color: cyan;">webuser</span>@<span style="color: darkorange;">security-client</span>:~$ <span style="color: white;">ls -la</span> /home/w3ich3rt/writeups/nahamcon-eu-2022
total 78
drwxr-xr-x 10 w3ich3rt w3ich3rt  4096 Oct 14 22:15 .
drwxr-xr-x  3 root     root      4096 Dec 26  2021 ..
drwxr-xr-x  3 w3ich3rt w3ich3rt  4096 Oct 12 13:18 .[warmup](../nahamcon-eu-2022.md)
lrwxrwxrwx  1 w3ich3rt w3ich3rt    23 Oct 12 13:18 <span style="color: lightgreen;">.home</span> -> [/../../home](/)
-rw-rw-rw-  1 w3ich3rt w3ich3rt    23 Oct 12 13:18 .[desc-nahamcon-eu-2022.md](../readme.md)
-rw-rw-rw-  1 w3ich3rt w3ich3rt    23 Oct 12 13:18 .[read-the-rules.md](read_the_rules.md)
-rw-rw-rw-  1 w3ich3rt w3ich3rt    23 Oct 12 13:18 .[banjo.md](banjo.md)
-rw-rw-rw-  1 w3ich3rt w3ich3rt    23 Oct 12 13:18 .[hashstation.md](hashstation.md)

<span style="color: cyan; font-weight: bold;">webuser</span>@<span style="color: darkorange; font-weight: bold;">security-client</span>:~$ <span style="color: white; font-weight: bold;">cat</span> banjo.txt

## Banjo
475 points - Warmups - 73 Solves - easy
Author: @JohnHammond#6971

Oooh, that classic twang! The banjo is one of my favorite strings instruments!

Download the file below.
Attachments: [banjo.jpg](https://ctf.nahamcon.com/files/76af8b0a065b055ddabe2677f637bb19/banjo.jpg?token=eyJ1c2VyX2lkIjo3MjIsInRlYW1faWQiOjM4NywiZmlsZV9pZCI6MX0.Y5zQHg.94yw9mFvAsnuBoLybag2Y7PjBiQ)

### Solving
![](banjo.jpg)


run strings on banjo.jpg ... 
> Tip: use `| grep flag` to minimize output
