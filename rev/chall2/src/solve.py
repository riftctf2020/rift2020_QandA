enc = "\x27\x3c\x33\x21\x16\x01\x13\x2e\x21\x27\x61\x36\x3c\x3b\x32\x0a\x31\x65\x66\x26\x3b\x21\x0a\x22\x65\x27\x3e\x0a\x34\x3b\x2c\x18\x65\x27\x66\x66\x28"
flag = ""
key = 0x55
for i in range(len(enc)):
	flag += chr( ord(enc[i]) ^ key )

print flag