import os
import sys
import time
import subprocess
from colorama import Fore, Back, Style, init

# Initialize colorama
init()

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def outils_reseaux():
    clear()
    print("╔══════════════════════════════════════════════════╗")
    print("║               Le HUB-Outils Réseau               ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║ 1. Tester la vitesse de la connexion internet    ║")
    print("║ 2. Modifier les paramètres de connexion          ║")
    print("║                                                  ║")
    print("║ 0. Retour                                        ║")
    print("╚══════════════════════════════════════════════════╝")

    while True:
       choice = input(Fore.LIGHTGREEN_EX + "Entrer votre choix: " + Style.RESET_ALL)

       if choice == "0":
          main()
       elif choice == '1':
          tester_vitesse_connexion()
       elif choice == '2':
          modifier_parametres_connexion()

def osint_tools():
    clear()
    print("╔══════════════════════════════════════════════════╗")
    print("║                     OSINT                        ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║ 1. Sherlock                                      ║")
    print("║ 2. Outil OSINT 2                                 ║")
    print("║                                                  ║")
    print("║ 0. Retour                                        ║")
    print("╚══════════════════════════════════════════════════╝")

    while True:
       choice = input(Fore.LIGHTGREEN_EX + "Entrer votre choix: " + Style.RESET_ALL)

       if choice == "0":
          main()
       elif choice == '1':
          print("╔════════════════════════════════╗")
          print("║   Enter un speudo ou un mail:  ║")
          print("╚════════════════════════════════╝")
          uSherlockName = input("Entrer : ")
          subprocess.Popen('python3 addons\sherlock-master\sherlock\sherlock.py '+ uSherlockName)
          pass
       elif choice == '2':
          # Call to the OSINT tool 2 function
          pass

def optimisations_activations():
    clear()
    print("╔══════════════════════════════════════════════════╗")
    print("║         Optimisations/Activations Windows        ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║ 1. Activation de Windows 10\\11 (Office)         ║")
    print("║ 2. Optimiser Windows 10                          ║")
    print("║ 3. Optimiser Windows 11                          ║")
    print("║                                                  ║")
    print("║ 0. Retour                                        ║")
    print("╚══════════════════════════════════════════════════╝")

    while True:
       choice = input(Fore.LIGHTGREEN_EX + "Entrer votre choix: " + Style.RESET_ALL)

       if choice == "0":
          main()
       elif choice == '1':
          subprocess.run ([r"addons\MAS_AIO-CRC32_31F7FD1E.cmd"])
          pass
       elif choice == '2':
          # Call to the Windows 11 optimization function
          pass
       elif choice == '3':
          # Call to the Windows 11 optimization function
          pass

def aide():
    clear()
    print("╔══════════════════════════════════════════════════╗")
    print("║                    Aide                          ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║ Pour toute aide, contactez le support ou         ║")
    print("║ consultez la documentation.                      ║")
    print("║                                                  ║")
    print("║ 0. Retour                                        ║")
    print("╚══════════════════════════════════════════════════╝")

    input("Appuyez sur Entrée pour revenir...")
    main()

def check_for_updates():
    clear()
    print("Vérification des mises à jour...")
    # Placeholder for actual update checking logic
    time.sleep(2)
    print("Le script est à jour.")
    input("Appuyez sur Entrée pour revenir...")
    main()

def tester_vitesse_connexion():
    clear()
    print("Tester la vitesse de connexion Internet")
    # Placeholder for speed test functionality
    input("Appuyez sur Entrée pour revenir...")
    outils_reseaux()

def modifier_parametres_connexion():
    clear()
    print("Modifier les paramètres de connexion")
    # Placeholder for modifying connection settings
    input("Appuyez sur Entrée pour revenir...")
    outils_reseaux()

def main():
    clear()
    print(Fore.GREEN + "")
    print("       ________________________________________________")
    print("      /                                                \\")
    print("     |    _________________________________________     |")
    print("     |   |                                         |    |")
    print("     |   |  C:\> _                                 |    |")
    print("     |   |   _____ _            _   _ _   _ ____   |    |")
    print("     |   |  |_   _| |__   ___  | | | | | | | __ )  |    |")
    print("     |   |    | | | '_ \ / _ \ | |_| | | | |  _ \  |    |")
    print("     |   |    | | | | | |  __/ |  _  | |_| | |_) | |    |")
    print("     |   |    |_| |_| |_|\___| |_| |_|\___/|____/  |    |")
    print("     |   |                                         |    |")
    print(Fore.GREEN + "     |   |           " + Fore.LIGHTGREEN_EX + "Created by:" + Style.RESET_ALL + " " + Fore.LIGHTRED_EX + "Milisof" + Style.RESET_ALL + "           " + Fore.GREEN + "|    |")
    print(Fore.GREEN + "     |   |            " + Fore.LIGHTGREEN_EX + "Version:" + Style.RESET_ALL + "  " + Fore.LIGHTRED_EX + "beta 0.1" + Style.RESET_ALL + "           " + Fore.GREEN + "|    |")
    print(Fore.GREEN + "     |   |       " + Fore.LIGHTGREEN_EX + "Follow me on Github:" + Style.RESET_ALL + " " + Fore.LIGHTRED_EX + "@Milis0f" + Style.RESET_ALL + "     " + Fore.GREEN + "|    |")
    print(Fore.GREEN + "     |   |                                         |    |")
    print(Fore.GREEN + "     |   |        " + Fore.LIGHTRED_EX + "SELECT AN OPTION TO BEGIN:" + Style.RESET_ALL + "       " + Fore.GREEN + "|    |")
    print(Fore.GREEN + "     |   |_________________________________________|    |")
    print("     |                                                  |")
    print("      \_________________________________________________/")
    print("             \___________________________________/\n\n" + Style.RESET_ALL)
    print(Fore.GREEN + "[01]   Outils Réseau")
    print(Fore.GREEN + "[02]   OSINT")
    print(Fore.GREEN + "[03]   Optimisations/Activations Windows")
    print(Fore.GREEN + "[04]   Aide/Credits")
    print(Fore.GREEN + "[99]   Mise à jour du Script")
    print(Fore.GREEN + "[00]   Quitter")

    while True:
       choice = input(Fore.LIGHTGREEN_EX + "Entrer votre choix: " + Style.RESET_ALL)

       if choice == "00":
          sys.exit()
       elif choice == '01':
          outils_reseaux()
       elif choice == '02':
          osint_tools()
       elif choice == '03':
          optimisations_activations()
       elif choice == '04':
          aide()
       elif choice == '99':
          check_for_updates()

if __name__ == "__main__":
    main()
