import random
import pyfiglet
import hashlib

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Exécuter 'sha256sum /usr/bin/agent' pour calculer l'empreinte actuelle.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Exécuter 'cat /usr/bin/agent.expected' pour lire l'empreinte officielle.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Exécuter 'cmp /usr/bin/agent /usr/bin/agent.orig' pour comparer les fichiers.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Exécuter 'md5sum /usr/bin/agent' pour une empreinte complémentaire.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Exécuter 'cp /usr/bin/agent.orig /usr/bin/agent' pour restaurer le binaire.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Exécuter 'sha256sum /usr/bin/agent' pour vérifier que l'empreinte correspond.",
        "",
    ]

def print_help():
    print("=" * 60)
    print("   TERMINAL WARRIOR - AIDE DU NIVEAU 16 (INTÉGRITÉ DES FICHIERS)")
    print("=" * 60)
    print("")
    print(" OBJECTIF :")
    print("   Le binaire /usr/bin/agent a peut-être été altéré. Calculez son empreinte,")
    print("   comparez-la au fichier de référence, puis restaurez le binaire d'origine.")
    print("")
    print(" COMMANDES :")
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche les défis en cours")
    print(" exit - Quitte le terminal")
    print(" sha256sum <fichier> - Calcule l'empreinte SHA256")
    print(" md5sum <fichier> - Calcule l'empreinte MD5")
    print(" cat <fichier> - Affiche le contenu d'un fichier")
    print(" cmp <fichier1> <fichier2> - Compare deux fichiers")
    print(" diff -q <fichier1> <fichier2> - Compare deux fichiers")
    print(" cp <source> <cible> - Copie un fichier")
    print(" ls -la <fichier> - Affiche les détails d'un fichier")
    print(" pwd - Affiche le répertoire courant (Print Working Directory)")
    print(" whoami - Affiche l'utilisateur courant")
    print("")
    print(" DÉROULÉ CONSEILLÉ :")
    print(" 1. 'sha256sum /usr/bin/agent' : calcule l'empreinte actuelle du binaire.")
    print(" 2. 'cat /usr/bin/agent.expected' : lit l'empreinte officielle à comparer.")
    print(" 3. 'cmp /usr/bin/agent /usr/bin/agent.orig' : confirme que les fichiers diffèrent.")
    print(" 4. 'md5sum /usr/bin/agent' : calcule une empreinte MD5 complémentaire.")
    print(" 5. 'cp /usr/bin/agent.orig /usr/bin/agent' : restaure la version officielle.")
    print(" 6. 'sha256sum /usr/bin/agent' : l'empreinte correspond désormais au fichier officiel.")
    print("")
    print(" ASTUCE : Le fichier 'agent.expected' est fiable : c'est l'empreinte actuelle du")
    print("          binaire qui est falsifiée. Une fois restauré, revérifiez l'empreinte.")

def print_challenges(state):
    for line in build_challenge_list(state):
        print(line)

def main():
    challenge_state = {i: False for i in range(1, 7)}

    time1 = random.randint(1, 24)
    time2 = random.randint(10, 59)
    time3 = random.randint(10, 59)
    day = random.randint(1, 28)

    expected_hash = "a1b2c3d4e5f60718293a4b5c6d7e8f9a0b1c2d3e4f60718293a4b5c6d7e8f9a0"
    altered_hash = "d1e2f3a4b5c60718293a4b5c6d7e8f9a0b1c2d3e4f60718293a4b5c6d7e8f9a0"
    restored = False

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="slant")
    print(ascii_banner)
    print("\nBienvenue au niveau 16 (INTÉGRITÉ DES FICHIERS) réalisé par (TerminalWarrior)\n")
    print("Le binaire /usr/bin/agent a peut-être été modifié. Vérifiez son empreinte et restaurez-le.")
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
    print(f"System load: 0.18               Processes:          {random.randint(260, 360)}")
    print("Usage of /:   47.11% of 49.11GB  Users logged in:     1")
    print("Memory usage: 1290MB             IP address for eth0: 10.0.2.15")
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

        if cmd == "sha256sum":
            if "agent" in low:
                h = expected_hash if restored else altered_hash
                print(f"{h}  /usr/bin/agent")
                if restored and not challenge_state[6]:
                    print("\nL'empreinte correspond à l'empreinte officielle : le binaire est restauré.")
                    print("SUCCESS: Niveau 16 terminé !")
                    challenge_state[6] = True
                    print("\nVous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
                elif not challenge_state[1]:
                    challenge_state[1] = True
                    print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
                    print("(L'empreinte est bizarre, comparez-la avec le fichier officiel.)")
            else:
                print(f"sha256sum: {args[0] if args else ''}: No such file or directory")
            continue

        if cmd == "cat" and "agent.expected" in low:
            print(expected_hash + "  /usr/bin/agent")
            print("\nC'est l'empreinte officielle du binaire. Comparez-la avec la valeur actuelle.")
            if not challenge_state[2]:
                challenge_state[2] = True
                print("\nVous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "cmp" or cmd == "diff":
            if "agent" in low and "orig" in low:
                print(f"/usr/bin/agent /usr/bin/agent.orig differ: byte 41, line 1")
                print("\nLes fichiers diffèrent : le binaire /usr/bin/agent a été modifié !")
                if not challenge_state[3]:
                    challenge_state[3] = True
                    print("\nVous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print("Files are identical.")
            continue

        if cmd == "md5sum" and "agent" in low:
            print("9f86d081884c7d659a2feaa0c55ad015  /usr/bin/agent")
            if not challenge_state[4]:
                challenge_state[4] = True
                print("\nVous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "cp" and "agent.orig" in low and "/usr/bin/agent" in low:
            restored = True
            print("SUCCESS: le binaire /usr/bin/agent a été restauré depuis la copie officielle.")
            if not challenge_state[5]:
                challenge_state[5] = True
                print("\nVous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "ls" and "agent" in low:
            print("-rwxr-xr-x 1 root root 14336 Oct  2 22:14 /usr/bin/agent")
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