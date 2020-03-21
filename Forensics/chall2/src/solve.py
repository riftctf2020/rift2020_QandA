#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Solve.py by X3eRo0
#
import struct

with open("flag.zip", "rb") as file:
    zipf = file.read()

for i in range(len(zipf)):
    if( zipf[i:i+4] == "\x50\x4B\x01\x02"):
        print "[+] CDH Offset:", hex(i)
        CDHO = i
        break

GPBF = CDHO + 0x08 # General Purpose Bit Flag
zipf = zipf[:GPBF] + struct.pack("<H", 0x9) + zipf[GPBF+2:]

with open("flag_fixed.zip", "wb") as file:

	file.write(zipf)
	file.close()

print "[!] Ok..."