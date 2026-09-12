import random
import pyfiglet

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Exécuter 'cat /etc/ssh/sshd_config' pour afficher la configuration SSH.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Exécuter 'grep -E \"PermitRootLogin|PasswordAuthentication\" /etc/ssh/sshd_config' pour repérer les options vulnérables.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Exécuter 'sudo sed -i \"s/PermitRootLogin yes/PermitRootLogin no/\" /etc/ssh/sshd_config' pour interdire root.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Exécuter 'ssh-keygen -t ed25519' pour générer une paire de clés.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Exécuter 'sudo systemctl restart ssh' pour appliquer la nouvelle configuration.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Exécuter 'grep PasswordAuthentication /etc/ssh/sshd_config' pour vérifier la désactivation du mot de passe.",
        "",
    ]

def print_help():
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche les défis en cours")
    print(" exit - Quitte le terminal")
    print(" cat /etc/ssh/sshd_config - Affiche la configuration SSH")
    print(" grep <motif> <fichier> - Recherche dans un fichier")
    print(" sudo sed -i ... - Édite un fichier en place")
    print(" ssh-keygen -t ed25519 - Génère une paire de clés SSH")
    print(" sudo systemctl restart ssh - Relance le serveur SSH")
    print(" ssh <utilisateur>@<hote> - Se connecte en SSH")
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
    root_disabled = False

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="slant")
    print(ascii_banner)
    print("\nBienvenue au niveau 19 (DURCISSEMENT SSH) réalisé par (TerminalWarrior)\n")
    print("Le serveur SSH autorise la connexion root par mot de passe. Corrigez cette configuration.")
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
    print(f"System load: 0.15               Processes:          {random.randint(270, 370)}")
    print("Usage of /:   40.25% of 49.11GB  Users logged in:     1")
    print("Memory usage: 1240MB             IP address for eth0: 10.0.2.15")
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

        if cmd == "cat" and "sshd_config" in low:
            print("#Port 22")
            print("Protocol 2")
            print("HostKey /etc/ssh/ssh_host_ed25519_key")
            if root_disabled:
                print("PermitRootLogin no")
                print("PasswordAuthentication no")
            else:
                print("PermitRootLogin yes")
                print("#PasswordAuthentication yes")
                print("PasswordAuthentication yes")
            print("PubkeyAuthentication yes")
            print("ChallengeResponseAuthentication no")
            print("\nPermitRootLogin et PasswordAuthentication sont actifs : risque élevé !")
            if not challenge_state[1]:
                challenge_state[1] = True
                print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "grep" and "sshd_config" in low:
            if "permitrootlogin" in low or "passwordauthentication" in low:
                if "passwordauthentication" in low and root_disabled:
                    print("PermitRootLogin no")
                    print("PasswordAuthentication no")
                    print("\nLes deux options sont désormais sécurisées : SUCCESS, la configuration est durcie.")
                    if not challenge_state[6]:
                        challenge_state[6] = True
                        print("\nVous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
                else:
                    print("PermitRootLogin yes" if not root_disabled else "PermitRootLogin no")
                    print("PasswordAuthentication yes")
                    print("\nLa login root par mot de passe est autorisée : à corriger.")
                    if not challenge_state[2]:
                        challenge_state[2] = True
                        print("\nVous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print(f"grep: {args[1] if len(args) > 1 else ''}: No such file or directory")
            continue

        if cmd == "sudo" and "sed" in low and "sshd_config" in low:
            if "permitrootlogin no" in low:
                root_disabled = True
                print("PermitRootLogin no : configuration mise à jour dans /etc/ssh/sshd_config")
                print("SUCCESS: la connexion root par mot de passe est interdite.")
                if not challenge_state[3]:
                    challenge_state[3] = True
                    print("\nVous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print("sed: expression invalide. Utilisez : sed -i \"s/PermitRootLogin yes/PermitRootLogin no/\"")
            continue

        if cmd == "sudo" and "systemctl" in low and ("restart" in low and "ssh" in low):
            print("Restarting OpenBSD Secure Shell server: sshd.")
            print("SUCCESS: la configuration SSH est appliquée (démarrage du service).")
            if not challenge_state[5]:
                challenge_state[5] = True
                print("\nVous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "ssh-keygen":
            if len(args) >= 2 and args[1] == "ed25519":
                print("Generating public/private ed25519 key pair.")
                print("Your identification has been saved in /home/user/.ssh/id_ed25519")
                print("Your public key has been saved in /home/user/.ssh/id_ed25519.pub")
                print("The key fingerprint is:")
                print("SHA256:9F6dLPn6G8qXpZ0Zz7Y9Q+4Mv3TqC7kJrPqE8wY5HnA user@localhost")
                print("SUCCESS: paire de clés générée.")
                if not challenge_state[4]:
                    challenge_state[4] = True
                    print("\nVous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print("Usage: ssh-keygen -t ed25519")
            continue

        if cmd == "pwd":
            print("/home/user")
            continue

        if cmd == "whoami":
            print("root" if command.startswith("sudo") else "user")
            continue

        print(f"{cmd}: command not found")

    return all(challenge_state.values())

if __name__ == "__main__":
    main()