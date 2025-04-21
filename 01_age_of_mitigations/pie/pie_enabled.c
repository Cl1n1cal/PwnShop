#include <stdio.h>
#include <unistd.h>
// gcc -o pie_enabled pie_enabled.c -fno-stack-protector
void win() {
    puts("Win!");
    execve("/bin/sh", NULL, NULL);
}

int main(void)
{
    char buf[32];

    puts("PIE enabled");
    printf("Leaking Pie address of main(): %p\n", main);
    printf(">>");
    fflush(stdout);

    int fd = 0;
    read(fd, buf, 200);

    return 0;
}