#!/usr/bin/python3
from pwn import *

elf = context.binary = ELF("../nx-disabled")

gs = '''
b main
'''
def start():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript=gs)
    if args.REMOTE:
        return remote("address", 12345)
    else:
        return process(elf.path)

# Addresses
win = 

# Functions

io = start()

io.recvline()


io.interactive()
