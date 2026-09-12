import random
import pyfiglet


def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Exécuter 'ls -la' pour révéler le fichier caché .security.log.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Exécuter 'find . -name .security.log' pour localiser le fichier journal caché.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Exécuter 'locate .security.log' pour chercher dans tout le système de fichiers.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Exécuter 'which grep' et 'whereis grep' pour localiser l'utilitaire grep.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Exécuter 'grep FAILED .security.log' pour fouiller le journal caché.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Utiliser 'grep sshd .security.log' pour confirmer le nom du service et terminer le niveau.",
        "",
    ]


def print_help():
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche la liste des défis et votre progression")
    print(" exit - Quitte le terminal")
    print(" ls - Liste les fichiers du répertoire courant")
    print(" ls -la - Liste tous les fichiers, y compris les fichiers cachés")
    print(" find <chemin> -name <motif> - Recherche des fichiers")
    print(" locate <motif> - Recherche un nom de fichier dans la base de données")
    print(" which <commande> - Affiche le chemin vers un exécutable de commande")
    print(" whereis <commande> - Localise les binaires, sources et pages de manuel")
    print(" grep <motif> <fichier> - Recherche dans le contenu d'un fichier")
    print(" pwd - Affiche le répertoire courant (Print Working Directory)")
    print(" whoami - Affiche l'utilisateur courant")


def print_challenges(state):
    for line in build_challenge_list(state):
        print(line)


def main():

    challenge_state = {i: False for i in range(1, 7)}

    processes = random.randint(100, 200)
    memoryusage = random.randint(100, 800)
    time1 = random.randint(1, 24)
    time2 = random.randint(10, 59)
    time3 = random.randint(10, 59)
    day = random.randint(1, 28)
    ip_parts = [str(random.randint(1, 254)) for _ in range(4)]
    other_ip_address = ".".join(ip_parts)
    ip_address = ".".join(ip_parts)

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="small")
    print(ascii_banner)

    print("\nBienvenue au niveau 3 (RECHERCHE) réalisé par (Diversion/diversionsec)\n")
    print("Tapez 'help' et 'challenge' pour accéder au menu d'aide et consulter les défis.")
    input("Appuyez sur Entrée pour continuer...")
    print("")

    print_challenges(challenge_state)
    print("\nWelcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-91-generic x86_64)\n")
    print("* Documentation: https://help.ubuntu.com")
    print("* Management:    https://landscape.canonical.com")
    print("* Support:       https://ubuntu.com/advantage\n")
    print(
        f"System information as of [Thu Oct {day} {time1:02d}:{time2:02d}:{time3:02d} UTC 2025]\n")
    print(f"System load: 0.00               Processes:          {processes}")
    print("Usage of /:   20.75% of 49.11GB  Users logged in:     1")
    print(
        f"Memory usage: {memoryusage}MB             IP address for eth0: {ip_address}")
    print("Swap usage:   0%\n")
    print("0 updates can be applied immediately\n")
    print("Last Login: Thu Oct 3 12:00:00 UTC 2025\n")

    current_directory = "~"
    hidden_file_found = False
    hidden_file_path = "./.security.log"
    security_log_content = [
        "Oct 10 12:05:12 auth[1234]: Accepted password for user from 10.0.0.5 port 54321 ssh2",
        "Oct 10 12:12:34 auth[1234]: FAILED LOGIN for invalid user admin from 10.0.0.8 port 54444",
        "Oct 10 12:15:22 auth[1234]: FAILED LOGIN for user guest from 10.0.0.9 port 54445",
        "Oct 10 12:20:00 auth[1234]: Accepted password for user from 10.0.0.5 port 54322 ssh2",
        "Oct 10 12:30:01 auth[1234]: Notice: suspicious activity detected",
        "Oct 10 12:35:00 sshd[1234]: sshd: error: Could not chdir to home directory /home/user: No such file or directory",
        "Oct 10 12:40:00 sshd[1234]: Failed password for invalid user root from 10.0.0.2 port 51234 ssh2",
    ]
    grep_path = "/usr/bin/grep"

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

        if cmd == "ls":
            if len(args) == 0:
                print("Documents")
            elif args == ["-la"] or args == ["-l", "-a"]:
                print("drwxr-xr-x  2 user user 4096 Oct 10 12:00 .")
                print("drwxr-xr-x 10 user user 4096 Oct 10 11:59 ..")
                print("drwxr-xr-x  2 user user 4096 Oct 10 12:00 Documents")
                print("-rw-r--r--  1 user user   66 Oct 10 12:00 .security.log")
                if not challenge_state[1]:
                    challenge_state[1] = True
                    print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print("ls: invalid option")
            continue

        if cmd == "find":
            if len(args) >= 3 and args[1] == "-name":
                pattern = args[2].strip('"')
                if pattern == ".security.log":
                    print(hidden_file_path)
                    if not challenge_state[2]:
                        challenge_state[2] = True
                        print("Vous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
                else:
                    print(f"find: '{pattern}': No such file or directory")
            else:
                print("Usage: find <path> -name <pattern>")
            continue

        if cmd == "locate":
            if len(args) != 1:
                print("Usage: locate <pattern>")
                continue
            pattern = args[0]
            if pattern == ".security.log":
                print(hidden_file_path)
                if not challenge_state[3]:
                    challenge_state[3] = True
                    print("Vous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print(f"locate: {pattern}: No such file or directory")
            continue

        if cmd == "which":
            if len(args) != 1:
                print("Usage: which <command>")
                continue
            if args[0] == "grep":
                print(grep_path)
                if not challenge_state[4]:
                    challenge_state[4] = True
                    print("Vous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print(f"which: no {args[0]} in ({grep_path})")
            continue

        if cmd == "whereis":
            if len(args) != 1:
                print("Usage: whereis <command>")
                continue
            if args[0] == "grep":
                print(f"grep: {grep_path} /usr/share/man/man1/grep.1.gz")
                if not challenge_state[4]:
                    challenge_state[4] = True
                    print("Vous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print(f"whereis: {args[0]}: not found")
            continue

        if cmd == "grep":
            if len(args) < 2:
                print("Usage: grep <pattern> <file>")
                continue
            pattern = args[0].strip('"')
            filename = args[1]
            if filename == ".security.log":
                matches = [line for line in security_log_content if pattern.lower() in line.lower()]
                for line in matches:
                    print(line)
                if pattern.upper() == "FAILED" and matches and not challenge_state[5]:
                    challenge_state[5] = True
                    print("Vous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
                if pattern.lower() == "sshd" and matches and not challenge_state[6]:
                    challenge_state[6] = True
                    print("Vous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print(f"grep: {filename}: No such file or directory")
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
