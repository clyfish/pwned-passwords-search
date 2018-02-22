#!/usr/bin/env python
import sys, os, mmap, struct, getpass, hashlib

f = open(os.path.dirname(sys.argv[0]) + '/pwned-passwords-2.0.bin')
mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
size = len(mm) / 24

def item(i):
    return mm[i * 24 : i * 24 + 20]

def count(i):
    return struct.unpack('<i', mm[i * 24 + 20 : i * 24 + 24])[0]

def search(x):
    left = 0
    right = size

    while left < right:
        mid = (left + right) // 2

        if item(mid) < x:
            left = mid + 1
        else:
            right = mid

    if left < size and item(left) == x:
        return count(left)
    else:
        return 0

while True:
    try:
        passwd = getpass.getpass()
    except (EOFError, KeyboardInterrupt):
        print
        break
    print search(hashlib.sha1(passwd).digest())
