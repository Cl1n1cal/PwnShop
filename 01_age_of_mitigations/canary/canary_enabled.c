#include <stdio.h>
#include <unistd.h>
#include <stdint.h>
// gcc -o  canary_enabled canary_enabled.c -no-pie

void win() {
    puts("Win!");
    execve("/bin/sh", NULL, NULL);
}

void leak_canary() {
    volatile uint64_t canary = 0;
    char buf[64];

    // Canary is typically right after the buffer and alignment padding
    uint64_t *canary_ptr = (uint64_t *)((char *)&buf + 72); // adjust if needed

    // Read it and store it
    canary = *canary_ptr;

    printf("Leaked Canary: 0x%lx\n", canary);
}

int main(void)
{
    char buf[32];

    puts("Canary enabled");
    leak_canary();
    printf(">>");
    fflush(stdout);

    read(0, buf, 200);

    return 0;
}