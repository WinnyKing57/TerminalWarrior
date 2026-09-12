import random
import pyfiglet

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Exécuter 'ls -la' pour repérer le lien suspect.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Exécuter 'readlink backup_link' pour voir sa cible.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Exécuter 'file backup_link' pour confirmer qu'il s'agit d'un lien symbolique.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Exécuter 'lsblk' pour lister les périphériques de stockage.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Exécuter 'rm backup_link' pour supprimer le lien malveillant.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Exécuter 'ln -s /home/user/real_backup backup_link' pour créer un lien correct.",
        "",
    ]

def print_help():
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche les défis en cours")
    print(" exit - Quitte le terminal")
    print(" ls -la - Liste les fichiers avec les liens")
    print(" readlink <lien> - Affiche la cible d'un lien symbolique")
    print(" file <fichier> - Identifie un fichier")
    print(" lsblk - Liste les périphériques de stockage")
    print(" rm <fichier> - Supprime un fichier ou un lien")
    print(" ln -s <cible> <lien> - Crée un lien symbolique")
    print(" mount - Affiche les points de montage")
    print(" df -h - Affiche l'espace disque")
    print(" pwd - Affiche le répertoire courant (Print Working Directory)")
    print(" whoami - Affiche l'utilisateur courant")

def print_challenges(state):
    for line in build_challenge_list(state):
        print(line)

def main():
    challenge_state = {i: False for i in range(1, 7)}

    time1 = random.randint(1, 24)
    time2 = random.randint(10, 59)
    time3 = random.randint(10, 59)
    day = random.randint(1, 28)

    link_removed = False

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="slant")
    print(ascii_banner)
    print("\nBienvenue au niveau 17 (LIENS SYMBOLIQUES ET MONTAGE) réalisé par (TerminalWarrior)\n")
    print("Un lien symbolique backup_link pointe vers un fichier sensible. Remplacez-le par un lien légitime.")
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
    print(f"System load: 0.09               Processes:          {random.randint(240, 340)}")
    print("Usage of /:   52.40% of 49.11GB  Users logged in:     1")
    print("Memory usage: 1170MB             IP address for eth0: 10.0.2.15")
    print("Swap usage:   0%\n")
    print("0 updates can be applied immediately\n")
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
        low = command.lower()

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
            print("total 16K")
            print("drwxr-xr-x 3 user user 4096 Oct 10 09:00 real_backup")
            print("lrwxrwxrwx 1 user user   11 Oct 10 09:05 backup_link -> /etc/shadow")
            if not link_removed:
                print("\nbackup_link pointe vers /etc/shadow : le fichier des mots de passe ! C'est un lien malveillant.")
            if not challenge_state[1]:
                challenge_state[1] = True
                print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "readlink":
            if "backup_link" in low:
                print("/etc/shadow" if not link_removed else "/home/user/real_backup")
                if not link_removed:
                    print("\nLa cible est bien /etc/shadow, un fichier critique.")
                else:
                    print("\nLe lien pointe maintenant vers le répertoire de sauvegarde légitime.")
                    if not challenge_state[6]:
                        challenge_state[6] = True
                        print("\nVous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print("readlink: invalid argument")
            if not challenge_state[2]:
                challenge_state[2] = True
                print("\nVous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "file" and "backup_link" in low:
            print("backup_link: symbolic link to /etc/shadow")
            if not challenge_state[3]:
                challenge_state[3] = True
                print("\nVous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "lsblk":
            print("NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT")
            print("sda      8:0    0   65G  0 disk")
            print("├─sda1   8:1    0    1M  0 part")
            print("├─sda2   8:2    0    1G  0 part /boot")
            print("└─sda5   8:5    0   64G  0 part /")
            print("sr0     11:0    1 1024M  0 rom")
            if not challenge_state[4]:
                challenge_state[4] = True
                print("\nVous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "mount":
            print("/dev/sda5 on / type ext4 (rw,relatime)")
            print("/dev/sda2 on /boot type ext4 (rw,relatime)")
            print("tmpfs on /run type tmpfs (rw,nosuid,noexec,relatime)")
            continue

        if cmd == "df":
            print("Filesystem     1K-blocks    Used Available Use% Mounted on")
            print("/dev/sda5      102640652 49103048 48314500  71% /")
            print("/dev/sda2        1039208   245684   729996  26% /boot")
            continue

        if cmd == "rm" and "backup_link" in low:
            link_removed = True
            print("SUCCESS: le lien malveillant backup_link a été supprimé.")
            if not challenge_state[5]:
                challenge_state[5] = True
                print("\nVous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "ln" and "s" in low:
            print("lien symbolique 'backup_link' -> '/home/user/real_backup' créé.")
            print("SUCCESS: le lien pointe maintenant vers la sauvegarde légitime.")
            if not challenge_state[6] and link_removed:
                challenge_state[6] = True
                print("\nVous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
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