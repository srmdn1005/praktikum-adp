import os
import time
from termcolor import colored

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pertamina_logo():

    print(colored("\n                                pertamina   \n", "white", attrs=["bold"]))

    print(colored("                           ██████████████████", "red"))
    print(colored("                             ██████████████████", "red"))
    print(colored("                               ██████████████████", "red"))
    print(colored("                                 ██████████████████", "red"))
    print(colored("                                   ██████████████████", "red"))
    print()

    print(colored("              ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "   " + colored("███████  ██████  ██████   ██████   █████   ███     ███  ██  ███   ██   █████", "white"))
    print(colored("            ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "     " + colored("██   ██  ██      ██   ██    ██    ██   ██  ████   ████  ██  ████  ██  ██   ██", "white"))
    print(colored("          ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "       " + colored("███████  █████   ██████     ██    ███████  ██ ██ ██ ██  ██  ██ ██ ██  ███████", "white"))
    print(colored("        ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "         " + colored("██       ██      ██ ██      ██    ██   ██  ██  ███  ██  ██  ██  ████  ██   ██", "white"))
    print(colored("      ██████████████████", "blue") + "   " + colored("██████████████████", "green") + "           " + colored("██       ██████  ██  ███    ██    ██   ██  ██       ██  ██  ██   ███  ██   ██", "white"))
    print(colored("    ██████████████████", "blue"))
    print(colored("  ██████████████████", "blue"))
    print(colored("██████████████████", "blue"))
    
def selesai_logo():
    from termcolor import colored

    print(colored("\t\t███████ ███████ ██      ███████ ███████  █████  ██    ███     ███ ███████ ███   ██  █████  ███     ███ ███████ ██ ██      ██  ██  █████  ███   ██    ", "green"))
    print(colored("\t\t██      ██      ██      ██      ██      ██   ██ ██    ████   ████ ██      ████  ██ ██   ██ ████   ████ ██   ██ ██ ██      ██ ██  ██   ██ ████  ██    ", "green"))
    print(colored("\t\t███████ █████   ██      █████   ███████ ███████ ██    ██ ██ ██ ██ █████   ██ ██ ██ ███████ ██ ██ ██ ██ ███████ ██ ██      ████   ███████ ██ ██ ██    ", "green"))
    print(colored("\t\t     ██ ██      ██      ██           ██ ██   ██ ██    ██  ███  ██ ██      ██  ████ ██   ██ ██  ███  ██ ██      ██ ██      ██ ██  ██   ██ ██  ████    ", "green"))
    print(colored("\t\t███████ ███████ ███████ ███████ ███████ ██   ██ ██    ██       ██ ███████ ██   ███ ██   ██ ██       ██ ██      ██ ███████ ██  ██ ██   ██ ██   ███     ", "green"))
    print()
    print(colored("\t\t                                         ██████    █████  ███     ███ ██████   █████  ██████                    ", "green"))
    print(colored("\t\t                                        ██        ██   ██ ████   ████ ██   ██ ██   ██ ██   ██                   ", "green"))
    print(colored("\t\t                                        ██   ███  ███████ ██ ██ ██ ██ ██████  ███████ ██████                    ", "green"))
    print(colored("\t\t                                        ██     ██ ██   ██ ██  ███  ██ ██   ██ ██   ██ ██ ██                     ", "green"))
    print(colored("\t\t                                         ███████  ██   ██ ██       ██ ██████  ██   ██ ██  ███    ██    ██    ██ ", "green"))

clear_screen()
pertamina_logo()
time.sleep(5)
clear_screen()
selesai_logo()