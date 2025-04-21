#include <stdio.h>
#include <unistd.h>
// gcc -o nx_enabled nx_enabled.c -fno-stack-protector -no-pie
void win() {
    puts("Win!");
    execve("/bin/sh", NULL, NULL);
}

int main(void)
{
    char buf[32];

    puts("Nx-Enabled");
    printf("Stack leak: %p\n", __builtin_frame_address(0));
    printf(">>");
    fflush(stdout);

    read(0, buf, 200);

    return 0;
}