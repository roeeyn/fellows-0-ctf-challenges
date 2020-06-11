#include <stdio.h>
#include <string.h>
#include <unistd.h>


void print_super_secret_flag_muahaha() {
    /* uses kind of ROT3 to "hide" the flag */
    char rot_str[] = "jiexc00i.kd\\pi00mv\\e-k0vz";

    for ( int i = 0; i < strlen(rot_str); i++ ) {
        rot_str[i] = rot_str[i] + 3;
    }

    printf("%s\n", rot_str);
}


int main() {
    sleep(1);
    printf("yaaaawn\n");
    sleep(3);
    printf("goina bed now\n");
    sleep(10);
    printf("get out and let me sleep!\n");
    sleep(12);
    printf("cmon the sooner I sleep the sooner you get your flag\n");
    sleep(30);
    printf("you're a hero just by getting this far\n");
    sleep(360000);
    printf("thanks for letting me sleep! here's your flag\n");
    print_super_secret_flag_muahaha();

    return 0;
}
