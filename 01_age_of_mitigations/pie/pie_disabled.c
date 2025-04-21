#include <stdio.h>
#include <unistd.h>
// gcc -o pie_disabled pie_disabled.c -fno-stack-protector -no-pie
void win() {
    puts("Win!");
    execve("/bin/sh", NULL, NULL);
}

int main(void)
{
    char buf[32];

    puts("PIE disabled");
    printf(">>");
    fflush(stdout);

    read(0, buf, 200);

    return 0;
}