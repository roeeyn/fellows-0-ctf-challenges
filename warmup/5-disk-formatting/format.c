#include <stdio.h>
#include <unistd.h>

int main() {
    char secret_str[64] = "not my secret, obviously";
    char name[64] = {0};
    printf("What's my secret?\n");
    read(0, name, 64);
    printf(name);
    return 0;
}
