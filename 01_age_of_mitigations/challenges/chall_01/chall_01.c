#include <stdio.h>
#include <unistd.h>
// gcc -o chall_01 chall_01.c

// You probably want to leak pie and canary in one go

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