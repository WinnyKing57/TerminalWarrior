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
from cli_lab.levels.linux import level14_linux_env_vars as linux_level14, level15_linux_ports_services as linux_level15, level16_linux_integrity as linux_level16, level17_linux_links_mounts as linux_level17
from cli_lab.levels.linux import level18_linux_scripts as linux_level18, level19_linux_ssh_hardening as linux_level19
from cli_lab.levels.windows import level1_windows_recon as win_level1, level2_windows_permissions as win_level2, level3_windows_searching as win_level3, level4_windows_networking as win_level4, level5_windows_cryptography as win_level5, level6_windows_registry as win_level6, level7_windows_tasks_services as win_level7, level8_Windows_event_logs as win_level8, level9_windows_disk_forensics as win_level9
from cli_lab.levels.windows import (
    level10_windows_powershell as win_level10,
    level11_windows_processes as win_level11,
    level12_windows_services as win_level12,
    level13_windows_updates as win_level13,
    level14_windows_firewall as win_level14,
    level15_windows_users_groups as win_level15,
    level16_windows_event_logs as win_level16,
    level17_windows_archives as win_level17,
    level18_windows_scheduled_tasks as win_level18,
    level19_windows_env_vars as win_level19,
    level20_windows_ports_services as win_level20,
    level21_windows_integrity as win_level21,
    level22_windows_junctions_disks as win_level22,
    level23_windows_scripts as win_level23,
    level24_windows_rdp_hardening as win_level24,
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
        print("14) Niveau 14 - Variables d'environnement")
        print("15) Niveau 15 - Ports et services réseau")
        print("16) Niveau 16 - Intégrité des fichiers")
        print("17) Niveau 17 - Liens symboliques et montages")
        print("18) Niveau 18 - Scripts shell")
        print("19) Niveau 19 - Durcissement SSH")
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
        elif choice == "14":
            linux_level14.main()
        elif choice == "15":
            linux_level15.main()
        elif choice == "16":
            linux_level16.main()
        elif choice == "17":
            linux_level17.main()
        elif choice == "18":
            linux_level18.main()
        elif choice == "19":
            linux_level19.main()
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
        print("11) Niveau 11 - Processus et performance")
        print("12) Niveau 12 - Services et démarrage")
        print("13) Niveau 13 - Mises à jour et logiciels")
        print("14) Niveau 14 - Pare-feu Windows Defender")
        print("15) Niveau 15 - Utilisateurs et groupes")
        print("16) Niveau 16 - Journaux d'événements")
        print("17) Niveau 17 - Archivage et extraction")
        print("18) Niveau 18 - Tâches planifiées (schtasks)")
        print("19) Niveau 19 - Variables d'environnement")
        print("20) Niveau 20 - Ports et services réseau")
        print("21) Niveau 21 - Intégrité des fichiers")
        print("22) Niveau 22 - Jonctions et disques")
        print("23) Niveau 23 - Scripts batch et PowerShell")
        print("24) Niveau 24 - Durcissement RDP")
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
        elif choice == "11":
            win_level11.run_level()
        elif choice == "12":
            win_level12.run_level()
        elif choice == "13":
            win_level13.run_level()
        elif choice == "14":
            win_level14.run_level()
        elif choice == "15":
            win_level15.run_level()
        elif choice == "16":
            win_level16.run_level()
        elif choice == "17":
            win_level17.run_level()
        elif choice == "18":
            win_level18.run_level()
        elif choice == "19":
            win_level19.run_level()
        elif choice == "20":
            win_level20.run_level()
        elif choice == "21":
            win_level21.run_level()
        elif choice == "22":
            win_level22.run_level()
        elif choice == "23":
            win_level23.run_level()
        elif choice == "24":
            win_level24.run_level()
        elif choice == "0":
            return
        else:
            print("Choix invalide !\n")


if __name__ == "__main__":
    main()
