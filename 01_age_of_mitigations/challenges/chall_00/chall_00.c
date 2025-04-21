#include <stdio.h>
#include <unistd.h>
// gcc -o chall_00 chall_00.c -no-pie

// This challenge is only to demontrate how to leak a value with %p and using
// u64() in pwntools instead of int(leak, 16)
// When you have leaked the canary you can overwrite the return address

// Remember that when canary is enabled you want you exploit to be:

// padding values
// canary
// rbp
// ret addr

void win() {
    puts("Win!");
    execve("/bin/sh", NULL, NULL);
}

int main(void)
{
    char buf[64];
    char buf2[64];

    puts("Chall_00");
    puts("Enter your input:");
    printf(">>");
    fflush(stdout);

    read(0, buf, sizeof(buf));

    puts("You entered:");
    printf(buf);

    puts("Enter your input again:");
    printf(">>");
    fflush(stdout);

    read(0, buf, 200);

    return 0;
}