### Setting a breakpoint (bp) on a function
b main

### Setting a breakpoint on an instruction within a function
b *main+403

### Setting a breakpint on an address
b *0x404030

### List breakpoints (info breakpoints)
i b

### Disable a breakpoint until you enable it again. Below command will disable bp number 3
disable b 3

### Enable a breakpoint again. Below command will enable bp number 3
enable b 3

### Delete a breakpoint. Below command will delete bp number 3
delete b 3

### Print the value of a register (in Hex)
p/x $rdi

### Print the value of a register (in Decimal)
p $rdi

### Print the 8-byte value at the memory address contained in a register (reg needs to hold readable mem addr)
x/gx $rdi

### Print 16 8-byte values of multiple addresses starting from the memory address conatined in rdi 
x/16gx $rdi

### Print the value at the memory address in a register (word size)
x/wx $rdi

### Print the 8-byte value at an address
x/gx 0x7fffffffdc50

### Print the 8-byte value at [rdi+1]
x/gx $rdi+1

### Calculate an offset of a stack address (in hex)
p/x 0x7fffffffdc50 - 0x7fffffffdc30

### Calculate an offset of a stack address (in decimal)
p 0x7fffffffdc50 - 0x7fffffffdc30

### Print 40 stack addresses
stack 40

### Show virtual memory map
vmmap

### Show the heap (with all flag to show everything possible)
vis -a

### Show heap bins
bins

### Info fram (can show you rbp and ret addr on the stack)
i f


