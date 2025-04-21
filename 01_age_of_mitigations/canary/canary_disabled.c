#include <stdio.h>
#include <unistd.h>
// gcc -o canary_disabled canary_disabled.c -fno-stack-protector -no-pie
void win() {
    puts("Win!");
    execve("/bin/sh", NULL, NULL);
}

int main(void)
{
    char buf[32];

    puts("Canary disabled");
    printf(">>");
    fflush(stdout);

    read(0, buf, 200);

    return 0;
}