;for i in `objdump -d helloworld | tr '\t' ' ' | tr ' ' '\n' | egrep '^[0-9a-f]{2}$' ` ; do echo -n "\\x$i" ; done
;\xeb\x1e\xb8\x04\x00\x00\x00\xbb\x01\x00\x00\x00\x59\xba\x0f\x00\x00\x00\xcd\x80\xb8\x01\x00\x00\x00\xbb\x00\x00\x00\x00\xcd\x80\xe8\xdd\xff\xff\xff\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21\x0d\x0a

global _start		 ;Point de départ du programme, nécessaire pour le linker (ld)

section .text

_start:
    jmp MESSAGE      ;1)Jump vers MESSAGE

GOBACK:
    mov eax, 0x4
    mov ebx, 0x1
    pop ecx          ;3) Nous avons désormais l'adresse de "Hello, world!\r\n"
    mov edx, 0xF
    int 0x80
    mov eax, 0x1
    mov ebx, 0x0
    int 0x80

MESSAGE:
    call GOBACK       ;2) Nous revenons en arrière puisque nous avons utilisé `call`, cela signifie que l'adresse de retour, qui est dans ce cas l'adresse de "Hello, world!\r\n", est poussée dans la pile.
    db "Hello, world!", 0dh, 0ah ; 0ah = 10 en décimal = \n en ASCII. 0dh = 13 en décimal = \r en ASCII

section .data
