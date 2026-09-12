import random
import pyfiglet

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Exécuter 'id' pour afficher vos identifiants (UID/GID).",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Exécuter 'groups' pour afficher vos groupes.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Exécuter 'cat /etc/passwd' pour lister les comptes et repérer l'intrus.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Exécuter 'sudo groupadd ops' pour créer le groupe ops.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Exécuter 'sudo useradd -m agent -g ops' pour créer l'utilisateur agent.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Exécuter 'sudo usermod -aG sudo agent' pour donner les droits administrateur à agent.",
        "",
        f"{'✅' if state[7] else '◻️'} 7) Exécuter 'sudo userdel -r invader' pour supprimer le compte intrus.",
        "",
    ]

def print_help():
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche les défis en cours")
    print(" exit - Quitte le terminal")
    print(" id - Affiche les identifiants de l'utilisateur")
    print(" groups - Affiche les groupes de l'utilisateur")
    print(" whoami - Affiche l'utilisateur courant")
    print(" cat /etc/passwd - Affiche la liste des comptes")
    print(" sudo groupadd <groupe> - Crée un groupe")
    print(" sudo useradd -m <utilisateur> -g <groupe> - Crée un utilisateur")
    print(" sudo usermod -aG sudo <utilisateur> - Ajoute un utilisateur au groupe sudo")
    print(" sudo userdel -r <utilisateur> - Supprime définitivement un compte")
    print(" pwd - Affiche le répertoire courant (Print Working Directory)")

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
    print("\nBienvenue au niveau 10 (UTILISATEURS ET GROUPES) réalisé par (TerminalWarrior)\n")
    print("Un attaquant a créé un compte 'invader' sur la machine. Id, groupes et comptes à maîtriser.")
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
    print("System load: 0.35               Processes:          301")
    print("Usage of /:   48.77% of 49.11GB  Users logged in:     2")
    print(
        f"Memory usage: 1180MB             IP address for eth0: {ip_address}")
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

        if cmd == "sudo" and len(args) >= 1 and args[0] in ("groupadd", "useradd", "usermod", "userdel"):
            cmd = args[0]
            args = args[1:]

        if cmd == "id":
            print(f"uid=1000(user) gid=1000(user) groups=1000(user),4(adm),27(sudo)")
            if not challenge_state[1]:
                challenge_state[1] = True
                print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "groups":
            print("user adm sudo")
            if not challenge_state[2]:
                challenge_state[2] = True
                print("\nVous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "cat" and len(args) >= 1 and args[0].endswith("/passwd"):
            print("root:x:0:0:root:/root:/bin/bash")
            print("daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin")
            print("bin:x:2:2:bin:/bin:/usr/sbin/nologin")
            print("sys:x:3:3:sys:/dev:/usr/sbin/nologin")
            print("sync:x:4:65534:sync:/bin:/bin/sync")
            print("user:x:1000:1000:TerminalWarrior,,,:/home/user:/bin/bash")
            print("invader:x:1001:1001:,,,:/home/invader:/bin/bash")
            print("\nLe compte 'invader' n'est pas un compte légitime : c'est l'intrus !")
            if not challenge_state[3]:
                challenge_state[3] = True
                print("\nVous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "groupadd":
            if len(args) >= 1 and args[0] == "ops":
                print("Groupe 'ops' créé avec l'identifiant 1001.")
                if not challenge_state[4]:
                    challenge_state[4] = True
                    print("\nVous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print("groupadd: Le groupe existe déjà.")
            continue

        if cmd == "useradd":
            full = " ".join(args)
            if "agent" in args:
                print("useradd: répertoire personnel /home/agent créé.")
                print("useradd: copie des fichiers depuis /etc/skel.")
                print("Utilisateur 'agent' créé.")
                if not challenge_state[5]:
                    challenge_state[5] = True
                    print("\nVous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print("useradd: Aucun utilisateur valide fourni.")
            continue

        if cmd == "usermod":
            full = " ".join(args)
            if "agent" in args and "-aG" in args:
                print("Ajout de l'utilisateur 'agent' au groupe 'sudo' ...")
                print("utilisateur 'agent' ajouté au groupe 'sudo'.")
                if not challenge_state[6]:
                    challenge_state[6] = True
                    print("\nVous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print("usermod: Argument invalide. Utilisez : sudo usermod -aG sudo agent")
            continue

        if cmd == "userdel":
            full = " ".join(args)
            if "invader" in args and "-r" in args:
                print("userdel: suppression du répertoire personnel /home/invader ...")
                print("userdel: la boîte mail spool (/var/mail/invader) n'existe pas")
                print("SUCCESS: Le compte 'invader' a été supprimé.")
                if not challenge_state[7]:
                    challenge_state[7] = True
                    print("\nVous avez terminé le défi 7 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print("userdel: L'utilisateur 'invader' n'existe pas (ou utilisez -r).")
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