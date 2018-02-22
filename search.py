#!/usr/bin/env python
import sys, os, mmap, struct, bisect, getpass, hashlib

class SortedPasswd:
    def __init__(self):
        f = open(os.path.dirname(sys.argv[0]) + '/pwned-passwords-2.0.bin')
        self.mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    def __len__(self):
        return len(self.mm) / 24
    def __getitem__(self, i):
        return self.mm[i * 24 : i * 24 + 20]
    def count(self, i):
        return struct.unpack('<i', self.mm[i * 24 + 20 : i * 24 + 24])[0]

sortedPasswd = SortedPasswd()

def search(x):
    index = bisect.bisect_left(sortedPasswd, x)

    if index < len(sortedPasswd) and sortedPasswd[index] == x:
        return sortedPasswd.count(index)
    else:
        return 0

while True:
    try:
        passwd = getpass.getpass()
    except (EOFError, KeyboardInterrupt):
        print
        break
    print search(hashlib.sha1(passwd).digest())
