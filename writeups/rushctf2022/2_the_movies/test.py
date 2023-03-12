#!/usr/bin/env python
# coding: utf8

def decodehist(_in, out):
    change = False
    for _c in _in.read():
        c = ord(_c)
        if c != 0x83:
            d = c^32 if change else c
            out.write(chr(d))
            change = False
        else:
            change = True

if __name__ == "__main__":
    import sys
    decodehist(sys.stdin, sys.stdout)
