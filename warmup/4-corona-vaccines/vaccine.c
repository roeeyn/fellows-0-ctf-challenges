#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


int main() {
    char command[64], input[64];

    printf("Who do you wanna shoot? Name: ");
    fgets(input, 64, stdin);

    strcpy(command, "echo ");
    strcat(command, input);

    printf("Command: %s\n", command);
    system(command);
    return 0;
}
