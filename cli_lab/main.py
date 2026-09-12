import os
import sys

# Allow running as a script: python .\cli_lab\main.py
if __name__ == "__main__" and __package__ is None:
    repo_root = os.path.dirname(os.path.dirname(__file__))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)

from cli_lab import progression
from cli_lab.levels.linux import level1_linux_intro as linux_level1, level2_linux_permissions as linux_level2, level3_linux_searching as linux_level3, level4_linux_networking as linux_level4, level5_linux_cryptography as linux_level5
from cli_lab.levels.linux import level6_linux_processes as linux_level6, level7_linux_services as linux_level7, level8_linux_apt as linux_level8, level9_linux_ufw as linux_level9
from cli_lab.levels.linux import level10_linux_users as linux_level10, level11_linux_logs as linux_level11, level12_linux_archives as linux_level12, level13_linux_cron as linux_level13
from cli_lab.levels.linux import level14_linux_env_vars as linux_level14, level15_linux_ports_services as linux_level15, level16_linux_integrity as linux_level16, level17_linux_links_mounts as linux_level17
from cli_lab.levels.linux import level18_linux_scripts as linux_level18, level19_linux_ssh_hardening as linux_level19, level20_linux_bonus_flag as linux_level20
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
    level25_windows_bonus_flag as win_level25,
)

LINUX_LEVELS = {
    "1": ("Défi d'introduction", linux_level1),
    "2": ("Permissions et propriété", linux_level2),
    "3": ("Recherche sur le système", linux_level3),
    "4": ("Réseau", linux_level4),
    "5": ("Cryptographie et décodage", linux_level5),
    "6": ("Processus et surveillance système", linux_level6),
    "7": ("Services et systemd", linux_level7),
    "8": ("Gestion de paquets (APT)", linux_level8),
    "9": ("Pare-feu (UFW)", linux_level9),
    "10": ("Utilisateurs et groupes", linux_level10),
    "11": ("Journaux et surveillance", linux_level11),
    "12": ("Archivage et compression", linux_level12),
    "13": ("Tâches planifiées (Cron)", linux_level13),
    "14": ("Variables d'environnement", linux_level14),
    "15": ("Ports et services réseau", linux_level15),
    "16": ("Intégrité des fichiers", linux_level16),
    "17": ("Liens symboliques et montages", linux_level17),
    "18": ("Scripts shell", linux_level18),
    "19": ("Durcissement SSH", linux_level19),
    "20": ("BONUS - Décryptage de flag", linux_level20),
}

WINDOWS_LEVELS = {
    "1": ("Défi d'introduction", win_level1),
    "2": ("Permissions et propriété", win_level2),
    "3": ("Recherche sur le système", win_level3),
    "4": ("Défi réseau", win_level4),
    "5": ("Cryptographie et décodage", win_level5),
    "6": ("Exploration du registre", win_level6),
    "7": ("Planificateur de tâches et services", win_level7),
    "8": ("Forensique des journaux d'événements", win_level8),
    "9": ("Forensique du disque et récupération de fichiers", win_level9),
    "10": ("Défi de scripts PowerShell", win_level10),
    "11": ("Processus et performance", win_level11),
    "12": ("Services et démarrage", win_level12),
    "13": ("Mises à jour et logiciels", win_level13),
    "14": ("Pare-feu Windows Defender", win_level14),
    "15": ("Utilisateurs et groupes", win_level15),
    "16": ("Journaux d'événements", win_level16),
    "17": ("Archivage et extraction", win_level17),
    "18": ("Tâches planifiées (schtasks)", win_level18),
    "19": ("Variables d'environnement", win_level19),
    "20": ("Ports et services réseau", win_level20),
    "21": ("Intégrité des fichiers", win_level21),
    "22": ("Jonctions et disques", win_level22),
    "23": ("Scripts batch et PowerShell", win_level23),
    "24": ("Durcissement RDP", win_level24),
    "25": ("BONUS - Décryptage de flag", win_level25),
}


def main():
    data = progression.load_progress()
    while True:
        print("=== TerminalWarrior ===")
        print(f"\nProgression : Linux {progression.count_done(data, 'linux')}/{len(LINUX_LEVELS)} · "
              f"Windows {progression.count_done(data, 'windows')}/{len(WINDOWS_LEVELS)} · "
              f"Score : {progression.get_score(data)} pts\n")
        print("1) Défis Linux")
        print("2) Défis Windows")
        print("0) Quitter\n")

        terminal_choice = input("Sélectionnez un terminal : ").strip()

        if terminal_choice == "1":
            linux_menu(data)
        elif terminal_choice == "2":
            windows_menu(data)
        elif terminal_choice == "0":
            print("Au revoir")
            break
        else:
            print("Choix invalide !\n")


def linux_menu(data):
    while True:
        print("\n=== Niveaux Linux ===")
        for number, (label, _) in LINUX_LEVELS.items():
            mark = "✅ " if progression.is_done(data, "linux", number) else "  "
            print(f"{mark}{number}) Niveau {number} - {label}")
        print("0) Retour\n")

        choice = input("Sélectionnez un niveau : ").strip()
        if choice == "0":
            return
        if choice not in LINUX_LEVELS:
            print("Choix invalide !\n")
            continue

        label, level = LINUX_LEVELS[choice]
        try:
            completed = level.main()
        except KeyboardInterrupt:
            completed = False
        if completed:
            progression.mark_done(data, "linux", choice)
            progression.save_progress(data)
            print(f"\n✅ Niveau {choice} terminé ! +{progression.points_for('linux', choice)} points")
        else:
            print("\nNiveau non terminé.")


def windows_menu(data):
    while True:
        print("\n=== Niveaux Windows ===")
        for number, (label, _) in WINDOWS_LEVELS.items():
            mark = "✅ " if progression.is_done(data, "windows", number) else "  "
            print(f"{mark}{number}) Niveau {number} - {label}")
        print("0) Retour\n")

        choice = input("Sélectionnez un niveau : ").strip()
        if choice == "0":
            return
        if choice not in WINDOWS_LEVELS:
            print("Choix invalide !\n")
            continue

        label, level = WINDOWS_LEVELS[choice]
        try:
            completed = level.run_level()
        except KeyboardInterrupt:
            completed = False
        if completed:
            progression.mark_done(data, "windows", choice)
            progression.save_progress(data)
            print(f"\n✅ Niveau {choice} terminé ! +{progression.points_for('windows', choice)} points")
        else:
            print("\nNiveau non terminé.")


if __name__ == "__main__":
    main()