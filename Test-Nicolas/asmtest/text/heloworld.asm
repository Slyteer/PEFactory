;for i in `objdump -d heloworld | tr '\t' ' ' | tr ' ' '\n' | egrep '^[0-9a-f]{2}$' ` ; do echo -n "\\x$i" ; done
;\xeb\x19\x31\xc0\xb0\x04\x31\xdb\xb3\x01\x59\x31\xd2\xb2\x16\xcd\x80\x31\xc0\xb0\x01\x31\xdb\xb3\x01\xcd\x80\xe8\xe2\xff\xff\xff\x20\x79\x30\x75\x20\x73\x70\x33\x34\x6b\x20\x31\x33\x33\x37\x20\x3f\x20


global _start		  ;Point de départ du programme, nécessaire pour le linker (ld)

section .text

_start:
	jmp message

proc:
    xor eax, eax
    mov al, 0x04	  ;Ici pour retirer les NULL BYTES, on peut stocker les valeurs de eax, ebx, edx dans leurs équivalents plus petits (al, bl, dl = registers 8 bits)
    xor ebx, ebx
    mov bl, 0x01
    pop ecx
    xor edx, edx
    mov dl, 0x16
    int 0x80

    xor eax, eax
    mov al, 0x01
    xor ebx, ebx
    mov bl, 0x01   ; return 1
    int 0x80

message:
    call proc
    msg db "Hello, world!"

section .data

