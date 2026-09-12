import random
import pyfiglet

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Exécuter 'echo $PATH' pour afficher le PATH actuel.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Exécuter 'env' pour lister toutes les variables d'environnement.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Exécuter 'which ls' pour voir quel binaire est utilisé.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Exécuter 'echo $LD_PRELOAD' pour voir la variable de détournement.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Exécuter 'export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' pour corriger le PATH.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Exécuter 'unset LD_PRELOAD' pour supprimer la variable malveillante.",
        "",
        f"{'✅' if state[7] else '◻️'} 7) Exécuter 'set' pour vérifier que l'environnement est propre.",
        "",
    ]

def print_help():
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche les défis en cours")
    print(" exit - Quitte le terminal")
    print(" echo $<VARIABLE> - Affiche la valeur d'une variable")
    print(" printenv <VARIABLE> - Affiche la valeur d'une variable")
    print(" env - Liste les variables d'environnement")
    print(" set - Liste les variables de la session")
    print(" which <commande> - Localise un binaire dans le PATH")
    print(" export PATH=<chemins> - Modifie le PATH")
    print(" unset <VARIABLE> - Supprime une variable")
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
    print("\nBienvenue au niveau 14 (VARIABLES D'ENVIRONNEMENT) réalisé par (TerminalWarrior)\n")
    print("Un attaquant a modifié votre PATH et ajouté une variable LD_PRELOAD pour détourner les commandes.")
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
    print(f"System load: 0.41               Processes:          {random.randint(250, 350)}")
    print("Usage of /:   44.62% of 49.11GB  Users logged in:     1")
    print(
        f"Memory usage: {random.randint(1200, 1800)}MB             IP address for eth0: {ip_address}")
    print("Swap usage:   0%\n")
    print("0 updates can be applied immediately\n")
    print("Last Login: Thu Oct 3 12:00:00 UTC 2025\n")

    current_directory = "~"
    clean_path = "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    path_fixed = False
    preload_unset = False

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

        if low.startswith("echo $path") or low.startswith("printenv path"):
            print(clean_path if path_fixed else "/tmp/malware:/tmp/evilbin:/usr/local/bin:/usr/bin:/bin")
            if not path_fixed:
                print("\nLe PATH pointe d'abord vers /tmp/malware : un binaire piégé peut être exécuté à votre insu !")
            if not challenge_state[1]:
                challenge_state[1] = True
                print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "env" or cmd == "printenv":
            print("SHELL=/bin/bash")
            print("USER=user")
            print("HOME=/home/user")
            print("PATH=/tmp/malware:/tmp/evilbin:/usr/local/bin:/usr/bin:/bin")
            print("LD_PRELOAD=/tmp/hack.so")
            print("PYTHONSTARTUP=/tmp/evil.py")
            print("\nLD_PRELOAD et PYTHONSTARTUP pointent vers /tmp : c'est le signe d'un compromis !")
            if not challenge_state[2]:
                challenge_state[2] = True
                print("\nVous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "which":
            if "ls" in args:
                print("/tmp/malware/ls" if not path_fixed else "/usr/bin/ls")
                print("\nLa commande ls est détournée par un faux binaire dans /tmp !" if not path_fixed else "\nLe PATH est corrigé, ls pointe vers le vrai binaire.")
                if not challenge_state[3]:
                    challenge_state[3] = True
                    print("\nVous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print(f"which: no {args[0] if args else ''} in ({clean_path if path_fixed else '/tmp/malware:/tmp/evilbin:/usr/local/bin:/usr/bin:/bin'})")
            continue

        if low.startswith("echo $ld_preload"):
            print("/tmp/hack.so" if not preload_unset else "")
            if not preload_unset:
                print("\nLD_PRELOAD charge un module depuis /tmp : chaque commande exécute du code malveillant !")
            if not challenge_state[4]:
                challenge_state[4] = True
                print("\nVous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "export" and "path=" in low:
            if "path=" in low:
                path_fixed = True
                print("PATH exporté : /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin")
                print("SUCCESS: le PATH ne pointe plus vers /tmp.")
                if not challenge_state[5]:
                    challenge_state[5] = True
                    print("\nVous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "unset" and "ld_preload" in low:
            preload_unset = True
            print("LD_PRELOAD supprimée.")
            print("SUCCESS: la variable malveillante n'est plus chargée.")
            if not challenge_state[6]:
                challenge_state[6] = True
                print("\nVous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "set":
            print("SHELL=/bin/bash")
            print("USER=user")
            print("HOME=/home/user")
            print(f"PATH={clean_path if path_fixed else '/tmp/malware:/tmp/evilbin:/usr/local/bin:/usr/bin:/bin'}")
            if preload_unset:
                print("(LD_PRELOAD n'est plus définie)")
            if path_fixed and preload_unset:
                print("SUCCESS: L'environnement est propre, plus aucun détournement.")
                if not challenge_state[7]:
                    challenge_state[7] = True
                    print("\nVous avez terminé le défi 7 ! Tapez 'challenge' pour voir votre progression.")
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