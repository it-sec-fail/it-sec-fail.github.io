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

<span style="color: cyan; font-weight: bold;">webuser</span>@<span style="color: darkorange; font-weight: bold;">security-client</span>:~$ <span style="color: white; font-weight: bold;">cat</span> read_the_rules.txt

## Read the rules

The flag is in the sourcecode of the rules page on the CTF website.
To get this flag you can either

- Inspect site or see sourcecode.
- Use the get_flag script.

or you can use this python script.


```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re

url = "https://ctf.nahamcon.com/rules"
search_string = "Your flag is: .* flag{(.*)}"

## Get Website
print("I'll try to get the flag from the rules page...")
try:
    resp = requests.get(url)
except:
    print("something went wrong :-(")

print("Searching for flag in website content...")
m = re.findall(search_string, str(resp.content))

if m:
    print("Here is your flag: flag{" + str(m[0]) + "}")
else:
    print("Nothing found... sorry")
```
