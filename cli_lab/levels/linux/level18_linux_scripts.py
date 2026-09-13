import random
import pyfiglet

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Exécuter 'touch cleanup.sh' pour créer le script.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Exécuter 'echo \"#!/bin/bash\" > cleanup.sh' pour écrire l'en-tête.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Exécuter 'cat cleanup.sh' pour vérifier le contenu.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Exécuter 'chmod +x cleanup.sh' pour rendre le script exécutable.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Exécuter './cleanup.sh' pour lancer le nettoyage.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Exécuter 'ls -la cleanup.sh' pour vérifier les permissions.",
        "",
    ]

def print_help():
    print("=" * 60)
    print("   TERMINAL WARRIOR - AIDE DU NIVEAU 18 (SCRIPTS SHELL)")
    print("=" * 60)
    print("")
    print(" OBJECTIF :")
    print("   Créez un script cleanup.sh qui supprime les fichiers malveillants,")
    print("   rendez-le exécutable puis lancez-le pour nettoyer le système.")
    print("")
    print(" COMMANDES :")
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche les défis en cours")
    print(" exit - Quitte le terminal")
    print(" touch <fichier> - Crée un fichier vide")
    print(" echo '<texte>' > <fichier> - Écrit du texte dans un fichier")
    print(" cat <fichier> - Affiche le contenu d'un fichier")
    print(" chmod +x <script> - Rend un script exécutable")
    print(" ./<script> - Exécute un script du répertoire courant")
    print(" bash <script> - Exécute un script avec bash")
    print(" ls -la - Liste les fichiers avec les permissions")
    print(" pwd - Affiche le répertoire courant (Print Working Directory)")
    print(" whoami - Affiche l'utilisateur courant")
    print("")
    print(" DÉROULÉ CONSEILLÉ :")
    print(" 1. 'touch cleanup.sh' : crée le fichier de script vide.")
    print(" 2. 'echo '#!/bin/bash' > cleanup.sh' : écrit l'en-tête shebang indispensable.")
    print(" 3. 'cat cleanup.sh' : vérifie le contenu du script.")
    print(" 4. 'chmod +x cleanup.sh' : rend le script exécutable.")
    print(" 5. './cleanup.sh' : exécute le script et supprime les fichiers malveillants.")
    print(" 6. 'ls -la cleanup.sh' : vérifie les permissions (-rwxr-xr-x).")
    print("")
    print(" ASTUCE : Sans le shebang '#!/bin/bash' et sans le bit x, l'exécution par './'")
    print("          échoue. Vérifiez toujours les permissions avec 'ls -la'.")

def print_challenges(state):
    for line in build_challenge_list(state):
        print(line)

def main():
    challenge_state = {i: False for i in range(1, 7)}

    time1 = random.randint(1, 24)
    time2 = random.randint(10, 59)
    time3 = random.randint(10, 59)
    day = random.randint(1, 28)

    script_executed = False

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="slant")
    print(ascii_banner)
    print("\nBienvenue au niveau 18 (SCRIPTS SHELL) réalisé par (TerminalWarrior)\n")
    print("Créez un script cleanup.sh qui supprime les fichiers malveillants, puis exécutez-le.")
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
    print(f"System load: 0.07               Processes:          {random.randint(250, 350)}")
    print("Usage of /:   45.90% of 49.11GB  Users logged in:     1")
    print("Memory usage: 1210MB             IP address for eth0: 10.0.2.15")
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

        if cmd == "touch" and "cleanup.sh" in low:
            print("Fichier cleanup.sh créé.")
            if not challenge_state[1]:
                challenge_state[1] = True
                print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "echo":
            if "cleanup.sh" in low and ">" in low:
                body = " #!/bin/bash" if "#!" in low.replace(" ", "") else ""
                print_script = "echo '#!/bin/bash' > cleanup.sh : en-tête écrit." if "#!" in low.replace(" ", "") else "echo 'rm -f /tmp/malware.*; echo done' >> cleanup.sh : instructions ajoutées."
                print(print_script)
                if "#!" in low.replace(" ", "") and not challenge_state[2]:
                    challenge_state[2] = True
                    print("\nVous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print(" ".join(args))
            continue

        if cmd == "cat" and "cleanup.sh" in low:
            if not challenge_state[3]:
                challenge_state[3] = True
                print("\nVous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
            print("#!/bin/bash")
            print("rm -f /tmp/malware.* /var/tmp/beacon")
            print("echo 'Nettoyage terminé'")
            continue

        if cmd == "chmod" and "cleanup.sh" in low:
            print("SUCCESS: cleanup.sh est maintenant exécutable.")
            if not challenge_state[4]:
                challenge_state[4] = True
                print("\nVous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "./cleanup.sh" or command.strip().startswith("./cleanup.sh"):
            script_executed = True
            print("Suppression de /tmp/malware.* terminée.")
            print("Suppression de /var/tmp/beacon terminée.")
            print("Nettoyage terminé")
            print("SUCCESS: Le script a nettoyé les fichiers malveillants.")
            if not challenge_state[5]:
                challenge_state[5] = True
                print("\nVous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "bash" and "cleanup.sh" in low:
            script_executed = True
            print("Nettoyage terminé")
            print("SUCCESS: Le script a nettoyé les fichiers malveillants.")
            if not challenge_state[5]:
                challenge_state[5] = True
                print("\nVous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "ls":
            print("total 8K")
            print("-rwxr-xr-x 1 user user  132 Oct 10 09:12 cleanup.sh")
            print("\ncleanup.sh est exécutable (-rwxr-xr-x) : le script est prêt.")
            if not challenge_state[6]:
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