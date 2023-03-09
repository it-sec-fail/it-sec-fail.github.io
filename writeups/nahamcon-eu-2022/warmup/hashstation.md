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

<span style="color: cyan; font-weight: bold;">webuser</span>@<span style="color: darkorange; font-weight: bold;">security-client</span>:~$ <span style="color: white; font-weight: bold;">cat</span> hashstation.txt

## Hashstation
485 points - Warmups - 57 Solves - easy
Author: @JohnHammond#6971

Below is a SHA256 hash! Can you determine what the original data was, before it was hashes?

`705db0603fd5431451dab1171b964b4bd575e2230f40f4c300d70df6e65f5f1c`

Please wrap the original value within the `flag{` prefix and `}` suffix to match the standard flag format.

### Solving.

1. [crackstation](https://crackstation.net/)
2. Copy Hash there...
3. `awesome`

> Flag: `flag{awesome}`