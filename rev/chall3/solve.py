#!/usr/bin/python

from z3 import *

inp = [BitVec("inp[%d]" % i,32)for i in range(0,0x25)]

z3_solver = Solver()
flag = ""

# inp
for i in range(0,len(inp)):
	z3_solver.add(inp[14] == 95)
	z3_solver.add(inp[0x24] - inp[0x7] == 2)
	z3_solver.add(inp[0x24] == 125)
	z3_solver.add(inp[0x8] == inp[0x23])
	z3_solver.add(inp[0x9] == inp[0x22])
	z3_solver.add(inp[0x9] == 45)
	z3_solver.add(inp[0x22] == inp[0x23])

	# z3_solver.add(inp[0x22]%0x9 == 0)
	# z3_solver.add(inp[0x22]%0x5 == 0)
	# z3_solver.add(inp[0x22]%0x28 == 5)
	# z3_solver.add(inp[0x22] == 45)
	z3_solver.add(inp[0xa] - inp[0x8]*3 + 0xe == 0)

	z3_solver.add(inp[0xb] == 0x30)

	z3_solver.add(inp[0xc] == 117) 
	z3_solver.add(inp[0x15] == 119) 
	# # or inp[0x15] == 'w'

	z3_solver.add(inp[0xd]%0x6 == 0)

	z3_solver.add(inp[0xd] == 114)

	z3_solver.add(inp[0xe] ^ inp[0x14] ^ inp[0x18] ^ inp[0x1f] == 0)

	z3_solver.add(inp[0xf] == 102)
	z3_solver.add(inp[0x10] == 0x31)
	z3_solver.add(inp[0x11] == 114)

	z3_solver.add(inp[0x11] + 0x1 == inp[0x12])
	z3_solver.add(inp[0x11] + 0x2 == inp[0x13])

	z3_solver.add(inp[0x15] == 119)
	z3_solver.add(inp[0x16] == 0x33)
	z3_solver.add(inp[24] == (inp[26] - 19))
	z3_solver.add(inp[20] == inp[24])
	z3_solver.add(inp[0x17] == 98)
	z3_solver.add(inp[0x19] == 99)

	z3_solver.add(inp[0x1a] == 114)

	z3_solver.add(inp[0x1b] == 0x34)

	z3_solver.add(inp[0x1c] ^ 0x20 == 75)

	z3_solver.add(inp[0x1d] == 109)
	z3_solver.add(inp[0x1e] == 101)
	z3_solver.add(inp[0x20] == 88)
	z3_solver.add(inp[0x21] == 79)
	z3_solver.add(inp[0x0] == 114)
	z3_solver.add(inp[0x1] == 105)
	z3_solver.add(inp[0x2] == 102)
	z3_solver.add(inp[0x3] == 116)
	z3_solver.add(inp[0x4] == 67)
	z3_solver.add(inp[0x5] == 84)
	z3_solver.add(inp[0x6] == 70)

	if z3_solver.check() == sat:
		sol = z3_solver.model()
		for i in range(0x25):
			try:
				#print(str(hex(i)) + ": " + str(sol[inp[i]]))
				flag += chr(int(str(sol[inp[i]])))
			except:
				pass
				#print(str(hex(i)) + ": " + str(sol[inp[i]]))
		break

print(flag)