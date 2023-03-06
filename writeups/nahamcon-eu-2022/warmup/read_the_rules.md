---
layout: page
---

# Read the rules

The flag is in the sourcecode of the rules website.

- Inspect site or see sourcecode.
- Use the get_flag script.

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