import os
import sys

# Allow running as a script: python .\cli_lab\main.py
if __name__ == "__main__" and __package__ is None:
    repo_root = os.path.dirname(os.path.dirname(__file__))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)

from cli_lab.levels.linux import level1_linux_intro as linux_level1, level2_linux_permissions as linux_level2, level3_linux_searching as linux_level3, level4_linux_networking as linux_level4, level5_linux_cryptography as linux_level5
from cli_lab.levels.linux import level6_linux_processes as linux_level6, level7_linux_services as linux_level7, level8_linux_apt as linux_level8, level9_linux_ufw as linux_level9
from cli_lab.levels.linux import level10_linux_users as linux_level10, level11_linux_logs as linux_level11, level12_linux_archives as linux_level12, level13_linux_cron as linux_level13
from cli_lab.levels.windows import level1_windows_recon as win_level1, level2_windows_permissions as win_level2, level3_windows_searching as win_level3, level4_windows_networking as win_level4, level5_windows_cryptography as win_level5, level6_windows_registry as win_level6, level7_windows_tasks_services as win_level7, level8_Windows_event_logs as win_level8, level9_windows_disk_forensics as win_level9
from cli_lab.levels.windows import (
    level10_windows_powershell as win_level10,
)

from cli_lab.levels.windows import (
    level10_windows_powershell as win_level10,
)


def main():
    while True:
        print("=== TerminalWarrior ===\n")
        print("1) Défis Linux")
        print("2) Défis Windows")
        print("0) Quitter\n")

        terminal_choice = input("Sélectionnez un terminal : ").strip()

        if terminal_choice == "1":
            linux_menu()
        elif terminal_choice == "2":
            windows_menu()
        elif terminal_choice == "0":
            print("Au revoir")
            break
        else:
            print("Choix invalide !\n")


def linux_menu():
    while True:
        print("\n=== Niveaux Linux ===")
        print("1) Niveau 1 - Défi d'introduction")
        print("2) Niveau 2 - Permissions et propriété")
        print("3) Niveau 3 - Recherche sur le système")
        print("4) Niveau 4 - Réseau")
        print("5) Niveau 5 - Cryptographie et décodage")
        print("6) Niveau 6 - Processus et surveillance système")
        print("7) Niveau 7 - Services et systemd")
        print("8) Niveau 8 - Gestion de paquets (APT)")
        print("9) Niveau 9 - Pare-feu (UFW)")
        print("10) Niveau 10 - Utilisateurs et groupes")
        print("11) Niveau 11 - Journaux et surveillance")
        print("12) Niveau 12 - Archivage et compression")
        print("13) Niveau 13 - Tâches planifiées (Cron)")
        print("0) Retour\n")

        choice = input("Sélectionnez un niveau : ").strip()

        if choice == "1":
            linux_level1.main()
        elif choice == "2":
            linux_level2.main()
        elif choice == "3":
            linux_level3.main()
        elif choice == "4":
            linux_level4.main()
        elif choice == "5":
            linux_level5.main()
        elif choice == "6":
            linux_level6.main()
        elif choice == "7":
            linux_level7.main()
        elif choice == "8":
            linux_level8.main()
        elif choice == "9":
            linux_level9.main()
        elif choice == "10":
            linux_level10.main()
        elif choice == "11":
            linux_level11.main()
        elif choice == "12":
            linux_level12.main()
        elif choice == "13":
            linux_level13.main()
        elif choice == "0":
            return
        else:
            print("Choix invalide !\n")


def windows_menu():
    while True:
        print("\n=== Niveaux Windows ===")
        print("1) Niveau 1 - Défi d'introduction")
        print("2) Niveau 2 - Permissions et propriété")
        print("3) Niveau 3 - Recherche sur le système")
        print("4) Niveau 4 - Défi réseau")
        print("5) Niveau 5 - Cryptographie et décodage")
        print("6) Niveau 6 - Exploration du registre")
        print("7) Niveau 7 - Planificateur de tâches et services")
        print("8) Niveau 8 - Forensique des journaux d'événements")
        print("9) Niveau 9 - Forensique du disque et récupération de fichiers")
        print("10) Niveau 10 - Défi de scripts PowerShell")
        print("0) Retour\n")

        choice = input("Sélectionnez un niveau : ").strip()

        if choice == "1":
            win_level1.run_level()
        elif choice == "2":
            win_level2.run_level()
        elif choice == "3":
            win_level3.run_level()
        elif choice == "4":
            win_level4.run_level()
        elif choice == "5":
            win_level5.run_level()
        elif choice == "6":
            win_level6.run_level()
        elif choice == "7":
            win_level7.run_level()
        elif choice == "8":
            win_level8.run_level()
        elif choice == "9":
            win_level9.run_level()
        elif choice == "10":
            win_level10.run_level()
        elif choice == "0":
            return
        else:
            print("Choix invalide !\n")


if __name__ == "__main__":
    main()
