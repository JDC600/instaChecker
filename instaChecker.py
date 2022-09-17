import requests, os, time, sys, signal
from bs4 import BeautifulSoup as bs


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    CYAN = '\033[96m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def sig_handler(sig, frame):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n\n[*] {bcolors.OKGREEN}Saliendo...{bcolors.ENDC} [*]\n")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.exit(0)

def salir():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n\n[*] {bcolors.OKGREEN}Saliendo...{bcolors.ENDC} [*]\n")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.exit(0)

def login():
    # usuario = input("Usuario:")
    # contraseña = input("Contraseña:")
    # two_factor = input("2-Factor:")
    urlLogin = 'https://www.instagram.com/'
    r = requests.get(urlLogin)
    # soup = bs(r.content, 'html.parser')
    print(r)


def main():
    signal.signal(signal.SIGINT, sig_handler)
    print("\n           " + bcolors.WARNING + "[" + bcolors.ENDC + bcolors.OKBLUE + "MENU" + bcolors.ENDC + bcolors.WARNING + "]" + bcolors.ENDC)
    print("------<<<<-------->>>>------")
    print("        1. Login")
    print("        0. Salir")
    print("------<<<<-------->>>>------\n")

    opcionMenuGeneral = input("Selecciona la opción: ")

    if opcionMenuGeneral == "1":
        login()
    elif opcionMenuGeneral == "0":
        salir()
    else:        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"[+] {bcolors.FAIL}Opción invalida.{bcolors.ENDC} [+]")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        main()


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()