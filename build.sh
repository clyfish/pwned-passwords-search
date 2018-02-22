#!/bin/bash

cd `dirname $0` || exit

rtorrent https://downloads.pwnedpasswords.com/passwords/pwned-passwords-2.0.txt.7z.torrent
7za e pwned-passwords-2.0.txt.7z
TMPDIR=~/tmp LC_ALL=C sort pwned-passwords-2.0.txt -o pwned-passwords-2.0.sort -S 50%
./build.py
