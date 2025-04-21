# How to deal with address leaks and logging
### Challenge prints an address to the terminal
The binary provides you with an address in this format: 0x7fffdeadbeef  



Solution:
io.recvuntil(b"format: 0x")  
leak = io.recvline().strip(b"\n")   
leak = int(16, leak)  
log.info("Leak: %s" % hex(leak))  

Result: "[*] Leak: 0x7fffdeadbeef"  

Detail: 
1. Using io.recvline().strip(b"\n") to remove trailing newline without removing potential space " " hex encoding (0x20) in the middle of the address. So if the address has 0x7fffdead20ab you will not accidentally remove the 0x20.

2. int(16, leak) is typecasting leak to a base 16 integer. Hex is base 16 and decimal is base 10. So if for some reason you get the result in decimal you can use int(10, leak).

IMO recvline is more reliable than recv.

### You do some ROP to get puts(some_addr)
This will print the address or canary ugly and in little endian like:  
"\xef\xbe\xad\xde\xff\x7f"  

If it was the canary you sometimes overwrite the lsb (the null byte) of the canary so it becomes writable by puts (since puts will terminate on a null byte).  
When looking at the stack in GDB it goes from:  
0xaf30deafbada4000 -> 0xaf30deafbada4041 (we overwrote the lsb with an 'A', 0x41)  

Then you will get printed something like this:  
"Your input: AAAAAAAAAAAAAAAAAAAA\x40\xda\xba\xaf\xde\x30\xaf"  


Solution (canary):  
io.recvuntil(b"Your input: AAAAAAAAAAAAAAAAAAAA")  
canary = io.recvline().strip(b"\n")  
canary = b"\x00" + canary  
canary = u64(canary.ljust(8, b"\x00"))  
log.info("Canary: %s" % hex(canary))  

Details:  
1. canary = b"\x00" + canary is to prepend the null byte that we could not print


### When the program uses 'read()'
use io.send()

### When the program uses 'fgets()'
use io.sendline() since fgets reads until newline
