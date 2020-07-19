# ASLR Check
    dynamicBase = 0x40
    aslrcheck = pe.OPTIONAL_HEADER.DllCharacteristics & 0x0040

    # If ASLR is enabled, then disable it and save to new file
    if aslrcheck:
        if (args.info == False):
            print (PrintRed("[!]") + " ASLR: \t\t\tEnabled - Disabling ASLR to " + newFile + "\n")
            pe.OPTIONAL_HEADER.DllCharacteristics &= ~dynamicBase
            pe.write(newFile)
            return True
        else:
            print(PrintRed("[!]") + " ASLR: \t\t\tEnabled\n")
        #sys.exit(1)

    # Continue without ASLR
    else:
        print (PrintGreen("[+]") + " ASLR: \t\t\tDisabled\n")
        return False
