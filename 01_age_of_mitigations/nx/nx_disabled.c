#include <stdio.h>
#include <unistd.h>
// gcc -o nx_disabled nx_disabled.c -fno-stack-protector -z execstack -no-pie

int main(void)
{
    char buf[32];

    puts("Nx-Disabled");
    printf("Stack leak: %p\n", __builtin_frame_address(0));
    printf(">>");
    fflush(stdout);

    read(0, buf, 200);

    return 0;
}