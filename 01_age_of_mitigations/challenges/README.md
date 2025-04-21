# Getting started with challenge binaries
The next couple of challenges will become increasingly more difficult.  
Start by understanding how the value is leaked in chall_00  

### Format string vulnerabilites
When a C program prints a buffer like this: printf(buffer);  
It means that there is a format string vulnerability.  

Usually, a binary will read user input into a buffer and then print that buffer, something like the following:  

```code
char buffer[32];
puts("Enter your name:");
read(0, buffer, 64);
puts("You entered:");
printf(buffer);
```

You can leak things from the stack using for example: %p  

You can leak a specific stack value by using for example: %11$p  
This will leak value number 11 on the stack. But what does value number 11 mean?  

The numbers 0-5 are some of the values in registers and the first value from the stack is number 6.  

So to leak the first value (8 bytes on 64-bit) you need to do %6$p  

Let's say you count the addresses on the stack and figure out that the canary is at position 13 (remember to start counting from 6).  
Then you need to do: %13$p  

### Resources
Read if you want to learn more (not necessary to solve the challenges)
https://owasp.org/www-community/attacks/Format_string_attack  
