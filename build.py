#!/usr/bin/env python
import struct

fout = open('pwned-passwords-2.0.bin', 'wb')

for line in open('pwned-passwords-2.0.sort'):
    passwd, count = line.rstrip('\n').split(':')
    fout.write(passwd.decode('hex'))
    fout.write(struct.pack('<i', int(count)))
