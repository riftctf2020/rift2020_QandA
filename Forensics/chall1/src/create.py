#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# create.py by X3eRo0
#

import pyminizip
import struct


# create flag.txt zip file
pyminizip.compress_multiple(
    [
        'flag.txt', # list of files to compress
    ],
    [],				# file path (current directory)
    "flag.zip",		# output file
    "", 			# empty password
    0x08,			# compression method
)

print "[+] Patching ZIP FILE"

# find Central Directory Header and
# change the External File attribute
# to 0x10 (not a file but a directory)

with open("flag.zip", "rb") as file:
    zipf = file.read()

for i in range(len(zipf)):
    if( zipf[i:i+4] == "\x50\x4B\x01\x02"):
        print "[+] CDH Offset:", hex(i)
        CDHO = i
        break

#         ZIP CDH STRUCTURE
# Central File Header Signature   --> 4  Bytes
# Version Made By                 --> 2  Bytes
# Version needed to Extract       --> 2  Bytes
# Genral Purpose Bit flag         --> 2  Bytes
# Compression Method              --> 2  Bytes
# Last Mod File Time              --> 2  Bytes
# Last Mod File Date              --> 2  Bytes
# CRC-32                          --> 4  Bytes
# Compressed Size                 --> 4  Bytes
# Uncompressed Size               --> 4  Bytes
# File Name Length                --> 2  Bytes
# Extra Field Length              --> 2  Bytes
# File Comment Length             --> 2  Bytes
# Disk Number Start               --> 2  Bytes
# Internal File Attributes        --> 4  Bytes
# External File Attributes        --> 4  Bytes
# Total                           --> 44 Bytes

EFAO = CDHO + 0x26 # External File Attributes
GPBF = CDHO + 0x08 # General Purpose Bit Flag

print "[+] EFAO:", hex(EFAO)
print "[+] GPBF:", hex(GPBF)

# change the External File Attribute
zipf = zipf[:GPBF] + struct.pack("<H", 0x01) + zipf[GPBF+2:]
zipf = zipf[:EFAO] + struct.pack("<H", 0x10) + zipf[EFAO+2:]

# save the file
with open("flag.zip", "wb") as file:
    file.write(zipf)
    file.close()

print "[+] Done"
exit()
