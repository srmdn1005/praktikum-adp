import os
import time
from termcolor import colored

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def adidas_logo():

    print(colored("\n\t\t\t\t\t\t\t\t                      adidas   \n", "white", attrs=["bold"]))

    print(colored("\t\t\t\t\t\t\t\t   ███████             ████             ███████", "white"))
    print(colored("\t\t\t\t\t\t\t\t  ████████████       ████████       ████████████", "white"))
    print(colored("\t\t\t\t\t\t\t\t ███████████████    ██████████    ███████████████", "white"))
    print(colored("\t\t\t\t\t\t\t\t█████████████████  ████████████  █████████████████", "white"))
    print(colored("\t\t\t\t\t\t\t\t █████████████████ ████████████ █████████████████", "white"))
    print()

    print(colored("\t\t\t\t\t\t\t\t    ██████████████████████████████████████████", "white"))
    print()

    print(colored("\t\t\t\t\t\t\t\t       ████████████████████████████████████", "white"))
    print()

    print(colored("\t\t\t\t\t\t\t\t           █████████ ████████ █████████     ", "white"))
    print(colored("\t\t\t\t\t\t\t\t               █████    ██    █████     ", "white"))
    print()
    print(colored("\t\t\t\t\t\t\t\t     █████  ██████  ██ ██████   █████   ██████", "white"))
    print(colored("\t\t\t\t\t\t\t\t    ██   ██ ██   ██ ██ ██   ██ ██   ██ ████", "white"))
    print(colored("\t\t\t\t\t\t\t\t    ███████ ██   ██ ██ ██   ██ ███████    ████", "white"))
    print(colored("\t\t\t\t\t\t\t\t    ██   ██ ██████  ██ ██████  ██   ██ ██████", "white"))
    
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
adidas_logo()
time.sleep(5)
clear_screen()
selesai_logo()