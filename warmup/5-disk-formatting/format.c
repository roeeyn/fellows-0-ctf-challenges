#include <stdio.h>
#include <unistd.h>

int main() {
    char secret_str[64] = "mlh{let_me_put_zeroooos_on_a_disk}";
    char name[64] = {0};
    printf("What's my secret?\n");
    read(0, name, 64);
    printf(name);
    return 0;
}
