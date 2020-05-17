import pefile

exe_path = "../putty.exe"
pe = pefile.PE(exe_path)

print("[*] e_magic value: %s" % hex(pe.DOS_HEADER.e_magic))
print("[*] Signature value: %s" % hex(pe.NT_HEADERS.Signature))


for field in pe.DOS_HEADER.dump():
    print(field)


for section in pe.sections:
    print(section.Name.decode('utf-8'))
    print("\tVirtual Address: " + hex(section.VirtualAddress))
    print("\tVirtual Size: " + hex(section.Misc_VirtualSize))
    print("\tRaw Size: " + hex(section.SizeOfRawData))
pe = pefile.PE(exe_path)


