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

# <span style="color: cyan;">webuser</span>@<span style="color: darkorange;">security-client</span>:~$ <span style="color: white;">cat</span>  /home/w3ich3rt/writeups/picoctf2023/readmycert/solve.md

Writeup from: Mr81u35ky

## ReadMyCert

Open the downloaded file:

```text
-----BEGIN CERTIFICATE REQUEST-----
MIICpzCCAY8CAQAwPDEmMCQGA1UEAwwdcGljb0NURntyZWFkX215Y2VydF8xMmVi
YTdmMX0xEjAQBgNVBCkMCWN0ZlBsYXllcjCCASIwDQYJKoZIhvcNAQEBBQADggEP
ADCCAQoCggEBALpy6fpMuQHtDwrurMECVwArITyhZEWWOtGLTteR7QMx67dfVxm3
jEHlsrbVQtJBdMJDuMA3eRp14c3tD3GTf/BkLbvjuvfha/3yqmuRHg9QUoYb9129
+TQdefx9zF2Rfi3LRh/EBr63nOW30u/2grNCYloHJsECfl/yx6UxKgu64uEUbaMC
ds9CRgDj1dRT6OY9OR3VozOHBacX9VpdoCDxJZHEsEwF9qd09NinMqsqDl9DHTyq
rlwsAK5qpsoiKvHs0+Li5oHe8iVqtb9E55lMRZDG88yw9y6cbwDWFh0sgt2k6kz7
WcrUV9cignn6lsJ6sAbguYiPOXxQUdsP8fkCAwEAAaAmMCQGCSqGSIb3DQEJDjEX
MBUwEwYDVR0lBAwwCgYIKwYBBQUHAwIwDQYJKoZIhvcNAQELBQADggEBAESOpr8K
qI7FafXaK9fJslzdYXQpl/ByCM1J+ZYiSLzBh3XQKX6DED2glrAkizQmNRn7Td3v
TRRFGuxFF2rhyEyLiZG1YXFs0xlBTLKDFKYegwqj1L7UDOtA9mNJuJkuuFnfK/EI
eB0mEOldJJSdHobOvB7GApwKiVqmTiOEVUu2gD+ec9xAFg9duzdfluPQ+DAmZvnt
Jip/lE65xoqG6tIvf2Z9U9fo6zC3pBx+vtBHGYtXEjuTfzhc9M7S7puaC+Gz84gM
eZ96LXuAlFDXYYbSGuQxsIkYAobpbb8SkUxy+g7Z8YKLb85KT9UnHyKfvHbzw9Sn
uByIlA+gSIKNIJ0=
-----END CERTIFICATE REQUEST-----
```

Via [csr-decoder](https://ssl-trust.com/SSL-Zertifikate/csr-decoder)

```text
Certificate Request:
    Data:
        Version: 1 (0x0)
        Subject: CN=picoCTF{read_mycert_12eba7f1}/name=ctfPlayer
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    00:ba:72:e9:fa:4c:b9:01:ed:0f:0a:ee:ac:c1:02:
```

> picoCTF{read_mycert_12eba7f1}
