import random
import pyfiglet

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Exécuter 'tail -n 50 /var/log/syslog' pour afficher la fin du journal système.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Exécuter 'head -n 20 /var/log/syslog' pour afficher le début du journal.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Exécuter 'grep sshd /var/log/auth.log' pour rechercher les tentatives SSH.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Exécuter 'journalctl -xe' pour consulter les dernières entrées du journal systemd.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Exécuter 'dmesg' pour afficher les messages du noyau.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Exécuter 'cat /var/log/syslog' pour lire le journal complet et trouver la trace de l'attaque.",
        "",
    ]

def print_help():
    print("=" * 60)
    print("   TERMINAL WARRIOR - AIDE DU NIVEAU 11 (JOURNAUX ET SURVEILLANCE)")
    print("=" * 60)
    print("")
    print(" OBJECTIF :")
    print("   Des connexions suspectes ont été enregistrées sur la machine.")
    print("   Inspectez les journaux système pour découvrir les tentatives d'accès")
    print("   et confirmer la trace de l'attaque.")
    print("")
    print(" COMMANDES :")
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche les défis en cours")
    print(" exit - Quitte le terminal")
    print(" tail -n <n> <fichier> - Affiche les dernières lignes d'un fichier")
    print(" head -n <n> <fichier> - Affiche les premières lignes d'un fichier")
    print(" grep <motif> <fichier> - Recherche dans un fichier")
    print(" cat <fichier> - Affiche le contenu d'un fichier")
    print(" journalctl -xe - Affiche les journaux systemd récents")
    print(" dmesg - Affiche les messages du noyau")
    print(" pwd - Affiche le répertoire courant (Print Working Directory)")
    print(" whoami - Affiche l'utilisateur courant")
    print("")
    print(" DÉROULÉ CONSEILLÉ :")
    print(" 1. 'tail -n 50 /var/log/syslog' : affiche les 50 dernières lignes du journal système.")
    print(" 2. 'head -n 20 /var/log/syslog' : affiche le début du journal.")
    print(" 3. 'grep sshd /var/log/auth.log' : recherche les tentatives de connexion SSH.")
    print(" 4. 'journalctl -xe' : consulte les dernières entrées du journal systemd.")
    print(" 5. 'dmesg' : affiche les messages du noyau (passage d'une interface en mode promiscuous).")
    print(" 6. 'cat /var/log/syslog' : lit le journal complet et confirme la compromission.")
    print("")
    print(" ASTUCE : la dernière ligne du journal /var/log/syslog est la preuve de l'attaque ;")
    print("          croisez dmesg (mode promiscuous) et grep sshd pour bâtir votre analyse.")

def print_challenges(state):
    for line in build_challenge_list(state):
        print(line)

def main():
    challenge_state = {i: False for i in range(1, 7)}

    time1 = random.randint(1, 24)
    time2 = random.randint(10, 59)
    day = random.randint(1, 28)
    ip_parts = [str(random.randint(10, 100)) for _ in range(4)]
    ip_address = ".".join(ip_parts)
    attacker_ip = f"{random.randint(101, 250)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="slant")
    print(ascii_banner)
    print("\nBienvenue au niveau 11 (JOURNAUX ET SURVEILLANCE) réalisé par (TerminalWarrior)\n")
    print("Des connexions suspectes ont été enregistrées. Inspectez les journaux pour le prouver.")
    print("Tapez 'help' et 'challenge' pour accéder au menu d'aide et consulter les défis.")
    input("Appuyez sur Entrée pour continuer...")
    print("")

    print_challenges(challenge_state)
    print("\nWelcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-91-generic x86_64)\n")
    print("* Documentation: https://help.ubuntu.com")
    print("* Management:    https://landscape.canonical.com")
    print("* Support:       https://ubuntu.com/advantage\n")
    print(
        f"System information as of [Thu Oct {day} {time1:02d}:{time2:02d}:00 UTC 2025]\n")
    print("System load: 1.92               Processes:          402")
    print("Usage of /:   53.44% of 49.11GB  Users logged in:     1")
    print(
        f"Memory usage: 1605MB             IP address for eth0: {ip_address}")
    print("Swap usage:   0%\n")
    print("0 updates can be applied immediately.\n")
    print("Last Login: Thu Oct 3 12:00:00 UTC 2025\n")

    current_directory = "~"
    syslog_lines = [
        f"Oct {day} {time1:02d}:{time2:02d}:01 sshd[2101]: Failed password for invalid user root from {attacker_ip} port 52058 ssh2",
        f"Oct {day} {time1:02d}:{time2:02d}:12 sshd[2103]: Failed password for invalid user admin from {attacker_ip} port 52060 ssh2",
        f"Oct {day} {time1:02d}:{time2:02d}:25 sshd[2105]: Failed password for invalid user user from {attacker_ip} port 52062 ssh2",
        f"Oct {day} {time1:02d}:{time2:02d}:41 sshd[2107]: Failed password for root from {attacker_ip} port 52064 ssh2",
        f"Oct {day} {time1:02d}:{time2:02d}:50 sshd[2109]: srv really routes the world via a secret tunnel",
        f"Oct {day} {time1:02d}:{time2:02d}:59 kernel: [ 9142.031385] Device eth0 left promiscuous mode",
        f"Oct {day} {time1:02d}:{time2:02d}:59 SUCCESS: La trace de l'attaque est confirmée, la ligne de creds est dans le journal.",
    ]

    while True:
        prompt = f"user@linux:{current_directory}$ "
        command = input(prompt).strip()
        if not command:
            continue

        parts = command.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd == "help":
            print_help()
            continue

        if cmd == "challenge":
            print()
            print_challenges(challenge_state)
            print()
            continue

        if cmd == "exit":
            print("Au revoir")
            break

        if cmd == "tail":
            filename = args[-1] if args else ""
            if filename and filename.endswith("/syslog"):
                print("-- FIN CT --")
                for line in syslog_lines[-5:]:
                    print(line)
                if not challenge_state[1]:
                    challenge_state[1] = True
                    print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
            elif filename and filename.endswith("/auth.log"):
                print("-- FIN CT --")
                print(f"Oct {day} {time1:02d}:{time2:02d}:59 sshd[2109]: Connection closed by authenticating user from {attacker_ip}")
            else:
                print(f"tail: cannot open '{filename}' for reading: No such file or directory")
            continue

        if cmd == "head":
            filename = args[-1] if args else ""
            if filename and filename.endswith("/syslog"):
                print("-- DEBUT CT --")
                print(f"Oct {day} {time1:02d}:46:51 kernel: [ 9000.000000] systemd[1]: Starting Flush Journal to Persistent Storage...")
                print(f"Oct {day} {time1:02d}:47:02 systemd[1]: Started Daily apt upgrade and clean activities.")
                print(f"Oct {day} {time1:02d}:47:10 cron[2234]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)")
                if not challenge_state[2]:
                    challenge_state[2] = True
                    print("\nVous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print(f"head: cannot open '{filename}' for reading: No such file or directory")
            continue

        if cmd == "grep":
            if len(args) >= 2:
                pattern = args[0]
                filename = args[1]
                if "sshd" in pattern and "/auth.log" in filename:
                    for line in syslog_lines:
                        if "sshd" in line:
                            print(line)
                    print(f"\n{len([l for l in syslog_lines if 'sshd' in l])} connexions SSH échouées depuis {attacker_ip} : attaque par force brute !")
                    if not challenge_state[3]:
                        challenge_state[3] = True
                        print("\nVous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
                elif "sshd" in pattern:
                    print(f"{filename}: No such file or directory")
                else:
                    print(f"grep: {pattern}: No such file or directory")
            else:
                print("Usage: grep <motif> <fichier>")
            continue

        if cmd == "journalctl":
            if args and args[0] == "-xe":
                print("-- Logs begin at Mon 2025-09-29 08:00:00 UTC. --")
                print(f"Oct {day} {time1:02d}:{time2:02d}:35 ubuntu sshd[2107]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost={attacker_ip}")
                print(f"Oct {day} {time1:02d}:{time2:02d}:41 ubuntu sshd[2107]: Failed password for root from {attacker_ip} port 52064 ssh2")
                print("-- Subject: Security event --")
                if not challenge_state[4]:
                    challenge_state[4] = True
                    print("\nVous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print("Usage: journalctl -xe")
            continue

        if cmd == "dmesg":
            print("Démarrage de dmesg ...")
            print(f"[ 9000.000000] Linux version 5.15.0-91-generic (buildd@lcy02-amd64-052)")
            print(f"[ 9142.031385] Device eth0 entered promiscuous mode")
            print(f"[ 9142.031385] Device eth0 left promiscuous mode")
            print("[ 9142.031385] CE: hpet increasing min_delta_ns")
            print("\nUne interface est passée en mode promiscuous : capture réseau suspecte.")
            if not challenge_state[5]:
                challenge_state[5] = True
                print("\nVous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "cat":
            filename = args[0] if args else ""
            if filename.endswith("/syslog"):
                for line in syslog_lines:
                    print(line)
                print("\nLa dernière ligne confirme la compromission : la machine était utilisée comme relais.")
                if not challenge_state[6]:
                    challenge_state[6] = True
                    print("\nVous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
            elif filename.endswith("/crontab"):
                print("18 3 * * * root run-parts /etc/cron.daily")
                print("5 12 * * * root test -x /usr/sbin/sshd-test && /usr/sbin/sshd-test")
            else:
                print(f"cat: {filename}: No such file or directory")
            continue

        if cmd == "pwd":
            print("/home/user")
            continue

        if cmd == "whoami":
            print("user")
            continue

        print(f"{cmd}: command not found")

    return all(challenge_state.values())

if __name__ == "__main__":
    main()