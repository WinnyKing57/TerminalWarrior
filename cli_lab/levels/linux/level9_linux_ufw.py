import random
import pyfiglet

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Exécuter 'sudo ufw status' pour vérifier l'état du pare-feu.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Exécuter 'sudo ufw enable' pour activer le pare-feu.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Exécuter 'sudo ufw default deny incoming' pour refuser le trafic entrant par défaut.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Exécuter 'sudo ufw allow 22' pour autoriser le port SSH.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Exécuter 'sudo ufw deny 8080' pour bloquer le port 8080.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Exécuter 'sudo ufw status verbose' pour vérifier la configuration finale.",
        "",
    ]

def print_help():
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche les défis en cours")
    print(" exit - Quitte le terminal")
    print(" sudo ufw status - Affiche l'état du pare-feu")
    print(" sudo ufw enable - Active le pare-feu")
    print(" sudo ufw default deny incoming - Refuse le trafic entrant par défaut")
    print(" sudo ufw default allow outgoing - Autorise le trafic sortant par défaut")
    print(" sudo ufw allow <port> - Autorise un port")
    print(" sudo ufw deny <port> - Bloque un port")
    print(" sudo ufw status verbose - Affiche la configuration détaillée")
    print(" pwd - Affiche le répertoire courant (Print Working Directory)")
    print(" whoami - Affiche l'utilisateur courant")

def print_challenges(state):
    for line in build_challenge_list(state):
        print(line)

def main():
    challenge_state = {i: False for i in range(1, 7)}
    ufw_enabled = False

    time1 = random.randint(1, 24)
    time2 = random.randint(10, 59)
    time3 = random.randint(10, 59)
    day = random.randint(1, 28)
    ip_parts = [str(random.randint(10, 100)) for _ in range(4)]
    ip_address = ".".join(ip_parts)

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="slant")
    print(ascii_banner)
    print("\nBienvenue au niveau 9 (PARE-FEU UFW) réalisé par (TerminalWarrior)\n")
    print("Un service web vulnérable écoute sur le port 8080. Sécurisez la machine avec le pare-feu.")
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
    print("System load: 0.44               Processes:          289")
    print("Usage of /:   61.08% of 49.11GB  Users logged in:     1")
    print(
        f"Memory usage: 1311MB             IP address for eth0: {ip_address}")
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

        if cmd == "sudo" and len(args) >= 1 and args[0] == "ufw":
            args = args[1:]
            cmd = "ufw"

        if cmd == "ufw":
            full = " ".join(args)
            if full == "status" or full.startswith("status verbose"):
                if not ufw_enabled:
                    print("Status: inactive")
                    print("\nLe pare-feu est inactif : activez-le avec 'sudo ufw enable'.")
                else:
                    print("Status: active")
                    print("Logging: on (low)")
                    print("Default: deny (incoming), allow (outgoing), disabled (routed)")
                    print("New profiles: skip\n")
                    print("To                         Action      From")
                    print("--                         ------      ----")
                    print("22/tcp                     ALLOW IN    Anywhere")
                    print("8080/tcp                   DENY IN     Anywhere")
                if not challenge_state[1] and not ufw_enabled:
                    challenge_state[1] = True
                    print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
                if full.startswith("status verbose") and ufw_enabled:
                    if not challenge_state[6]:
                        challenge_state[6] = True
                        print("\nVous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
            elif full == "enable":
                print("Command may disrupt existing ssh connections. Proceed with operation (y|n)? y")
                print("Firewall is active and enabled on system startup")
                ufw_enabled = True
                if not challenge_state[2]:
                    challenge_state[2] = True
                    print("\nVous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
            elif full == "default deny incoming":
                print("Default incoming policy changed to 'deny'")
                print("(Be sure to update your rules accordingly)")
                if not challenge_state[3]:
                    challenge_state[3] = True
                    print("\nVous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
            elif full == "default allow outgoing":
                print("Default outgoing policy changed to 'allow'")
                print("(Be sure to update your rules accordingly)")
            elif full.startswith("allow"):
                parts_full = args
                if len(parts_full) > 1:
                    target = parts_full[1]
                    print(f"Rule added")
                    print(f"Rule added (v6)")
                    print(f"Port {target} autorisé.")
                    if target in ("22", "ssh"):
                        if not challenge_state[4]:
                            challenge_state[4] = True
                            print("\nVous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
                else:
                    print("Usage: sudo ufw allow <port>")
            elif full.startswith("deny"):
                parts_full = args
                if len(parts_full) > 1:
                    target = parts_full[1]
                    print(f"Rule added")
                    print(f"Rule added (v6)")
                    print(f"Port {target} bloqué.")
                    if target in ("8080", "http-alt"):
                        if not challenge_state[5]:
                            challenge_state[5] = True
                            print("\nVous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
                else:
                    print("Usage: sudo ufw deny <port>")
            else:
                print(f"ufw: unknown subcommand '{full}'")
                print("Utilisez 'sudo ufw status' pour voir l'état du pare-feu.")
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