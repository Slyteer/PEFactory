import colorama
from colorama import Fore, Back, Style
colorama.init()

# Set the color semi-permanently
print(Fore.CYAN)
print("Text will continue to be cyan")
print("until it is reset or changed")
print(Style.RESET_ALL)

# Colorize a single line and then reset
print(Fore.RED + 'You can colorize a single line.' + Style.RESET_ALL)

# Colorize a single word in the output
print('Or a single ' + Back.GREEN + 'words' + Style.RESET_ALL + ' can be highlighted')

# Combine foreground and background color
print(Fore.BLUE + Back.WHITE)
print('Foreground, background, and styles can be combined')
print("==========            ")

print(Style.RESET_ALL)
print('If unsure, reset everything back to normal.')