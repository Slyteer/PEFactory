#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv) {
    if(argc < 2) {
        printf("Usage: %s <shellcode>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    printf("Size: %d bytes.\n", strlen(argv[1]));
    void (*shellcode)() = (void((*)())) (argv[1]);

    shellcode();

    return EXIT_SUCCESS;
}
