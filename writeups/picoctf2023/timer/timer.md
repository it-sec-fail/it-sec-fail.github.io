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

## timer

Download the apk-file.

Then use the online java [decompiler](http://www.javadecompilers.com/result?currentfile=sources/com/example/timer/BuildConfig.java) to decompile the apk-file.
In BuildConfig.java you find

```java
public static final String VERSION_NAME = "picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}";

```

> picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}
