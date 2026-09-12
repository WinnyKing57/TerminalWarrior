import random
import pyfiglet

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Exécuter 'file backup.tar.gz' pour identifier l'archive.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Exécuter 'tar -tzf backup.tar.gz' pour lister le contenu de l'archive.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Exécuter 'tar -xzf backup.tar.gz' pour extraire l'archive.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Exécuter 'ls' pour voir les fichiers extraits.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Exécuter 'gzip -d data.log.gz' pour décompresser le journal.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Exécuter 'cat extracted_flag.txt' pour lire l'indice caché dans l'archive.",
        "",
    ]

def print_help():
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche les défis en cours")
    print(" exit - Quitte le terminal")
    print(" file <fichier> - Identifie le type d'un fichier")
    print(" tar -tzf <archive> - Liste le contenu d'une archive .tar.gz")
    print(" tar -xzf <archive> - Extrait une archive .tar.gz")
    print(" tar -czf <archive> <fichiers> - Crée une archive compressée")
    print(" gzip -d <fichier>.gz - Décompresse un fichier")
    print(" gunzip <fichier>.gz - Décompresse un fichier")
    print(" ls - Liste les fichiers du répertoire courant")
    print(" cat <fichier> - Affiche le contenu d'un fichier")
    print(" pwd - Affiche le répertoire courant (Print Working Directory)")
    print(" whoami - Affiche l'utilisateur courant")

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
    print("\nBienvenue au niveau 12 (ARCHIVAGE ET COMPRESSION) réalisé par (TerminalWarrior)\n")
    print("Une archive 'backup.tar.gz' contient une sauvegarde avec une trace compromettante.")
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
    print("System load: 0.12               Processes:          268")
    print("Usage of /:   71.33% of 49.11GB  Users logged in:     1")
    print(
        f"Memory usage: 1244MB             IP address for eth0: {ip_address}")
    print("Swap usage:   0%\n")
    print("0 updates can be applied immediately.\n")
    print("Last Login: Thu Oct 3 12:00:00 UTC 2025\n")

    current_directory = "~"
    extracted_files = ["stolen_data.db", "notes.txt", "extracted_flag.txt", "data.log.gz"]

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

        if cmd == "file":
            filename = args[0] if args else ""
            if filename == "backup.tar.gz":
                print("backup.tar.gz: gzip compressed data, last modified: Tue Oct  2 22:14:02 2025, from Unix, original size modulo 2^32 1433")
                if not challenge_state[1]:
                    challenge_state[1] = True
                    print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
            elif filename:
                print(f"{filename}: ASCII text")
            else:
                print("Usage: file <fichier>")
            continue

        if cmd == "tar":
            if len(args) < 1:
                print("Usage: tar -tzf <archive>  |  tar -xzf <archive>")
                continue
            opt = args[0]
            archive = args[1] if len(args) > 1 else ""
            if archive != "backup.tar.gz":
                print(f"tar: {archive}: Cannot open: No such file or directory")
                continue
            if "t" in opt:
                print("backup/stolen_data.db")
                print("backup/notes.txt")
                print("backup/extracted_flag.txt")
                print("backup/data.log.gz")
                if not challenge_state[2]:
                    challenge_state[2] = True
                    print("\nVous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
            elif "x" in opt:
                print("backup/")
                print(f"extraction des éléments de ./backup/ terminée")
                print("SUCCESS: L'archive a été extraite dans 'backup/'.")
                if not challenge_state[3]:
                    challenge_state[3] = True
                    print("\nVous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
            elif "c" in opt:
                print("Archive créée.")
            else:
                print(f"tar: invalid option '{opt}'")
            continue

        if cmd == "ls":
            print("backup/            backup.tar.gz    notes.txt")
            print("data.log.gz       extracted_flag.txt")
            if not challenge_state[4]:
                challenge_state[4] = True
                print("\nVous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "gzip" or cmd == "gunzip":
            if len(args) >= 1 and (args[0] == "-d" or cmd == "gunzip"):
                target = args[1] if len(args) > 1 else (args[0] if cmd == "gunzip" else "")
            else:
                target = args[0] if args else ""
            if target == "data.log.gz":
                print("SUCCESS: 'data.log.gz' a été décompressé en 'data.log'.")
                if not challenge_state[5]:
                    challenge_state[5] = True
                    print("\nVous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
            elif target:
                print(f"gzip: {target}: No such file or directory")
            else:
                print("Usage: gzip -d <fichier>.gz")
            continue

        if cmd == "cat":
            filename = args[0] if args else ""
            if filename == "extracted_flag.txt":
                print("Exfiltration vers 185.220.101.4 — C'est la preuve de l'attaque !")
                print("SUCCESS: Niveau terminé ! Tapez 'challenge' pour voir votre progression.")
                if not challenge_state[6]:
                    challenge_state[6] = True
                    print("\nVous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
            elif filename == "notes.txt":
                print("Sauvegarde des données de la base clients avant migration.")
            elif filename == "data.log":
                print("Oct 02 21:58:12 backup: dump du fichier /var/www/app/.env OK")
                print("Oct 02 22:14:02 backup: compression de backup.tar.gz OK")
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

if __name__ == "__main__":
    main()