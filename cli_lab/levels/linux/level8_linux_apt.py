import random
import pyfiglet

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Exécuter 'sudo apt update' pour actualiser les listes de paquets.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Exécuter 'apt list --upgradable' pour afficher les paquets à mettre à jour.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Exécuter 'sudo apt upgrade -y' pour mettre à jour le système.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Exécuter 'apt search nmap' pour rechercher le paquet nmap.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Exécuter 'sudo apt install nmap -y' pour installer nmap.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Exécuter 'sudo apt remove telnet -y' pour supprimer telnet.",
        "",
        f"{'✅' if state[7] else '◻️'} 7) Exécuter 'apt list --installed | grep nmap' pour vérifier l'installation.",
        "",
    ]

def print_help():
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche les défis en cours")
    print(" exit - Quitte le terminal")
    print(" sudo apt update - Actualise les listes de paquets")
    print(" apt list --upgradable - Liste les paquets à mettre à jour")
    print(" sudo apt upgrade -y - Met à jour tous les paquets")
    print(" apt search <paquet> - Recherche un paquet")
    print(" sudo apt install <paquet> -y - Installe un paquet")
    print(" sudo apt remove <paquet> -y - Supprime un paquet")
    print(" apt list --installed | grep <paquet> - Vérifie l'installation")
    print(" pwd - Affiche le répertoire courant (Print Working Directory)")
    print(" whoami - Affiche l'utilisateur courant")

def print_challenges(state):
    for line in build_challenge_list(state):
        print(line)

def main():
    challenge_state = {i: False for i in range(1, 8)}

    time1 = random.randint(1, 24)
    time2 = random.randint(10, 59)
    time3 = random.randint(10, 59)
    day = random.randint(1, 28)
    ip_parts = [str(random.randint(10, 100)) for _ in range(4)]
    ip_address = ".".join(ip_parts)

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="slant")
    print(ascii_banner)
    print("\nBienvenue au niveau 8 (GESTION DES PAQUETS APT) réalisé par (TerminalWarrior)\n")
    print("Le système manque d'une partie des outils nécessaires et plusieurs paquets sont périmés.")
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
    print("System load: 0.22               Processes:          312")
    print("Usage of /:   56.30% of 49.11GB  Users logged in:     1")
    print(
        f"Memory usage: 1210MB             IP address for eth0: {ip_address}")
    print("Swap usage:   0%\n")
    print("42 updates can be applied immediately.\n")
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

        if cmd == "sudo" and len(args) >= 1 and args[0] == "apt":
            args = args[1:]
            cmd = "apt"

        if cmd == "apt":
            full = " ".join(args)
            subcommand = args[0] if args else ""

            if subcommand == "update":
                print("Get:1 http://archive.ubuntu.com/ubuntu focal InRelease [265 kB]")
                print("Get:2 http://archive.ubuntu.com/ubuntu focal-updates InRelease [114 kB]")
                print("Get:3 http://archive.ubuntu.com/ubuntu focal-security InRelease [114 kB]")
                print("Fetched 493 kB in 2s (241 kB/s)")
                print("Reading package lists... Done")
                print("Building dependency tree... Done")
                print(f"42 packages can be upgraded. Run 'apt list --upgradable' to see them.")
                if not challenge_state[1]:
                    challenge_state[1] = True
                    print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
            elif subcommand == "list":
                if "--upgradable" in args:
                    print("Listing...")
                    print("base-files/focal-updates 11ubuntu5.8 amd64 [upgradable from: 11ubuntu5.6]")
                    print("libssl1.1/focal-updates 1.1.1f-1ubuntu2.22 amd64 [upgradable from: 1.1.1f-1ubuntu2.20]")
                    print("openssh-server/focal-updates 1:8.2p1-4ubuntu0.11 amd64 [upgradable from: 1:8.2p1-4ubuntu0.9]")
                    print("telnet/focal 0.17-41.2build1 amd64 [upgradable from: 0.17-41.2build1]")
                    print("nmap/focal 7.80+dfsg1-2build1 amd64 [installed,upgradable to: 7.80+dfsg1-2build1]")
                    if not challenge_state[2]:
                        challenge_state[2] = True
                        print("\nVous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
                elif "--installed" in args:
                    if "grep" in args and "nmap" in args:
                        print("Listing...")
                        print("nmap/focal,now 7.80+dfsg1-2build1 amd64 [installed]")
                        print("\nSUCCESS: nmap est bien installé.")
                        if not challenge_state[7]:
                            challenge_state[7] = True
                            print("\nVous avez terminé le défi 7 ! Tapez 'challenge' pour voir votre progression.")
                    else:
                        print("Listing...")
                        print("base-files/focal,now 11ubuntu5.8 amd64 [installed]")
                        print("openssh-server/focal,now 1:8.2p1-4ubuntu0.11 amd64 [installed]")
                        print("nmap/focal,now 7.80+dfsg1-2build1 amd64 [installed]")
                        print("python3/focal,now 3.8.10-0ubuntu1~20.04 amd64 [installed]")
                        print("telnet/focal,now 0.17-41.2build1 amd64 [installed]")
                else:
                    print(f"apt: unknown list option '{' '.join(args)}'")
            elif subcommand == "upgrade":
                print("Reading package lists... Done")
                print("Building dependency tree... Done")
                print("Calculating upgrade... Done")
                print("Get:42 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 openssh-server 1:8.2p1-4ubuntu0.11 [729 kB]")
                print("Fetched 47.3 MB in 4s (10.1 MB/s)")
                print("Preconfiguring packages ...")
                print("Preparing to unpack .../openssh-server_1%3a8.2p1-4ubuntu0.11_amd64.deb ...")
                print("Unpacking openssh-server (1:8.2p1-4ubuntu0.11) ...")
                print("Setting up openssh-server (1:8.2p1-4ubuntu0.11) ...")
                print("Processing triggers for man-db (2.9.1-1) ...")
                print("Processing triggers for libc-bin (2.31-0ubuntu9.9) ...")
                print("SUCCESS: Le système est maintenant à jour.")
                if not challenge_state[3]:
                    challenge_state[3] = True
                    print("\nVous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
            elif subcommand == "search":
                if len(args) > 1:
                    pkg = args[1]
                    if pkg == "nmap":
                        print("Sorting... Done")
                        print("Full Text Search... Done")
                        print("nmap/focal 7.80+dfsg1-2build1 amd64")
                        print("  The Network Mapper")
                        print("\nLe paquet nmap est disponible dans les dépôts.")
                    else:
                        print(f"Sorting... Done\nFull Text Search... Done\n{len([1])} packages matching '{pkg}' are available.")
                    if "nmap" in args:
                        if not challenge_state[4]:
                            challenge_state[4] = True
                            print("\nVous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
                else:
                    print("Usage: apt search <paquet>")
            elif subcommand == "install":
                if len(args) > 1 and args[1] == "nmap":
                    print("Reading package lists... Done")
                    print("Building dependency tree... Done")
                    print("The following additional packages will be installed:")
                    print("  libblas3 liblinear4 liblua5.3-0 libpcre3 nmap-common")
                    print("Suggested packages:")
                    print("  mtr-tiny ncat ndiff zenmap")
                    print("Setting up nmap-common (7.80+dfsg1-2build1) ...")
                    print("Setting up libpcre3 (2:8.39-13build4) ...")
                    print("Setting up nmap (7.80+dfsg1-2build1) ...")
                    print("Processing triggers for man-db (2.9.1-1) ...")
                    print("SUCCESS: Le paquet nmap a été installé.")
                    if not challenge_state[5]:
                        challenge_state[5] = True
                        print("\nVous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
                else:
                    print(f"apt: package '{' '.join(args[1:])}' not found")
            elif subcommand == "remove":
                if len(args) > 1 and args[1] == "telnet":
                    print("Reading package lists... Done")
                    print("Building dependency tree... Done")
                    print("The following packages will be REMOVED:")
                    print("  telnet")
                    print("Removing telnet (0.17-41.2build1) ...")
                    print("Processing triggers for man-db (2.9.1-1) ...")
                    print("SUCCESS: Le paquet telnet a été supprimé.")
                    if not challenge_state[6]:
                        challenge_state[6] = True
                        print("\nVous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
                else:
                    print(f"apt: package '{' '.join(args[1:])}' is not installed")
            else:
                print(f"apt: unknown subcommand '{subcommand}'")
            continue

        if cmd == "telnet":
            print(f"telnet: command not found")
            print("(Le paquet telnet n'est pas installé — ou vient d'être désinstallé.)")
            continue

        if cmd == "nmap":
            print(f"nmap: command not found")
            print("(Installez le paquet nmap avec 'sudo apt install nmap -y'.)")
            continue

        if cmd == "pwd":
            print("/home/user")
            continue

        if cmd == "whoami":
            print("root" if command.startswith("sudo") else "user")
            continue

        print(f"{cmd}: command not found")

if __name__ == "__main__":
    main()