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

## rotation

given Text: `xqkwKBN{z0bib1wv_l3kzgxb3l_73l97nm4}`

Use [cyberchef](https://gchq.github.io/CyberChef/) and rot13 (but it was *18*)

> picoCTF{r0tat1on_d3crypt3d_73d97fe4}
