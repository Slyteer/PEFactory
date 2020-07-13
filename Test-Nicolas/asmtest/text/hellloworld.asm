;for i in `objdump -d hellloworld | tr '\t' ' ' | tr ' ' '\n' | egrep '^[0-9a-f]{2}$' ` ; do echo -n "\\x$i" ; done
;\xba\x59\x00\x00\x00\xb9\x00\xa0\x04\x08\xbb\x01\x00\x00\x00\xb8\x04\x00\x00\x00\xcd\x80\xb8\x01\x00\x00\x00\xcd\x80

section     .text
global      _start                              ;Point de départ du programme, nécessaire pour le linker (ld)

_start:                                         ;Communique au linker le point d'entrée

    mov     edx,len                             ;Longueur du message
    mov     ecx,msg                             ;Message à écrire
    mov     ebx,1                               ;Description du fichier, ici "sortie standart" (stdout)
    mov     eax,4                               ;Numero syscall, toujours 4 pour du i386 (sys_write)
    int     0x80                                ;Call kernel

    mov     eax,1                               ;Numero syscall, toujours 1 pour du i386 (sys_exit)
    int     0x80                                ;Call kernel

section     .data

msg     db  'Coucou, je suis là! otjkreotkgoerktorektorektoerktoerktoperktporektoperktoprektoprketop',0xa          ;Le message que l'on souhaite afficher
len     equ $ - msg                             ;Calcul de la longueur du message qui va etre deplacer dans le registre edx
