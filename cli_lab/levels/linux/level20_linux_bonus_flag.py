import base64
import random
import pyfiglet


def build_challenge_list(state, names):
    enc, bin_, txt = names
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Exécuter 'cat {enc}' pour lire le fichier chiffré.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Exécuter 'xxd -r -p {enc} {bin_}' pour décoder l'hexadécimal.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Exécuter 'cat {bin_}' pour voir la couche suivante.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Exécuter 'base64 -d {bin_} {txt}' pour décoder la base64.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Exécuter 'cat {txt}' pour lire le message en clair.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Exécuter 'echo <FLAG>' pour soumettre le drapeau (utilisez cat {txt}).",
        "",
    ]


def print_help():
    print("=" * 60)
    print("   TERMINAL WARRIOR - AIDE DU NIVEAU BONUS (DÉCRYPTAGE DE FLAG)")
    print("=" * 60)
    print("")
    print(" OBJECTIF :")
    print("   Le drapeau est chiffré en deux couches : hexadécimal, puis base64.")
    print("   Décodez chaque couche dans l'ordre, lisez le drapeau en clair, puis")
    print("   soumettez-le exactement avec 'echo'.")
    print("")
    print(" COMMANDES :")
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche les défis en cours")
    print(" exit - Quitte le terminal")
    print(" cat <fichier> - Affiche le contenu d'un fichier")
    print(" xxd -r -p <hex> <sortie> - Convertit de l'hexadécimal en binaire")
    print(" file <fichier> - Identifie un fichier")
    print(" base64 -d <entree> <sortie> - Décode un fichier base64")
    print(" echo <texte> - Affiche du texte (sert à soumettre le drapeau)")
    print(" pwd - Affiche le répertoire courant (Print Working Directory)")
    print(" whoami - Affiche l'utilisateur courant")
    print("")
    print(" DÉROULÉ CONSEILLÉ :")
    print(" 1. 'cat <fichier>.enc' : lit la première couche (longue chaîne hexadécimale).")
    print(" 2. 'xxd -r -p <fichier>.enc <binaire>.bin' : décode l'hexadécimal en binaire.")
    print(" 3. 'cat <binaire>.bin' : révèle la couche base64.")
    print(" 4. 'base64 -d <binaire>.bin <texte>.txt' : décode la base64 en message clair.")
    print(" 5. 'cat <texte>.txt' : lit le drapeau en clair.")
    print(" 6. 'echo <FLAG>' : soumet le drapeau exactement tel qu'affiché pour valider.")
    print("")
    print(" ASTUCE : Chaque commande affiche un SUCCESS quand la couche est bien décodée.")
    print("          Copiez le drapeau depuis 'cat <texte>.txt' : la soumission est")
    print("          sensible à la casse et aux caractères.")


def print_challenges(state, names):
    for line in build_challenge_list(state, names):
        print(line)


def main():
    challenge_state = {i: False for i in range(1, 7)}

    test_flag = globals().get("_TEST_FLAG")
    test_names = globals().get("_TEST_NAMES")
    if test_flag and test_names:
        enc, bin_, txt = test_names
        final_flag = test_flag
    else:
        num1 = random.randint(1000, 9999)
        num2 = random.randint(1000, 9999)
        enc = f"flag_{num1}_{num2}.enc"
        bin_ = f"recovered_{num1}.bin"
        txt = "flag_clean.txt"
        final_flag = "TW_BONUS_LNX_" + "".join(random.choice("0123456789ABCDEF") for _ in range(8))

    layer_b64 = base64.b64encode(final_flag.encode()).decode()
    layer_hex = layer_b64.encode().hex()
    names = (enc, bin_, txt)
    decoded = False

    time1 = random.randint(1, 24)
    time2 = random.randint(10, 59)
    time3 = random.randint(10, 59)
    day = random.randint(1, 28)

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="slant")
    print(ascii_banner)
    print("\nBienvenue au niveau BONUS (DÉCRYPTAGE DE FLAG) réalisé par (TerminalWarrior)\n")
    print(f"Un attaquant a chiffré le drapeau dans '{enc}' en deux couches (hexadécimal puis base64).")
    print("Décodez-le, lisez le drapeau, puis soumettez-le avec echo.")
    print("Tapez 'help' et 'challenge' pour accéder au menu d'aide et consulter les défis.")
    input("Appuyez sur Entrée pour continuer...")
    print("")

    print_challenges(challenge_state, names)
    print("\nWelcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-91-generic x86_64)\n")
    print("* Documentation: https://help.ubuntu.com")
    print("* Management:    https://landscape.canonical.com")
    print("* Support:       https://ubuntu.com/advantage\n")
    print(
        f"System information as of [Thu Oct {day} {time1:02d}:{time2:02d}:{time3:02d} UTC 2025]\n")
    print(f"System load: 0.05               Processes:          {random.randint(240, 340)}")
    print("Usage of /:   41.77% of 49.11GB  Users logged in:     1")
    print("Memory usage: 1355MB             IP address for eth0: 10.0.2.15")
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
            print_challenges(challenge_state, names)
            print()
            continue

        if cmd == "exit":
            print("Au revoir")
            break

        if cmd == "cat":
            if enc in low:
                print(layer_hex)
                print("\nUne longue chaîne hexadécimale : premières données chiffrées.")
                if not challenge_state[1]:
                    challenge_state[1] = True
                    print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
            elif bin_ in low:
                print(layer_b64)
                print("\nLa base64 révèle la couche suivante du message.")
                if not challenge_state[3]:
                    challenge_state[3] = True
                    print("\nVous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
            elif txt in low:
                print(final_flag)
                print("\nC'est le drapeau en clair ! Soumettez-le avec echo.")
                if not challenge_state[5]:
                    challenge_state[5] = True
                    print("\nVous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print(f"cat: {args[0] if args else ''}: No such file")
            continue

        if cmd == "xxd" and "-r" in low:
            if enc in low and bin_ in low:
                print(f"Fichier binaire '{bin_}' créé à partir de l'hexadécimal.")
                print(f"SUCCESS: {enc} décodé en binaire (base64).")
                if not challenge_state[2]:
                    challenge_state[2] = True
                    print("\nVous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print("Usage: xxd -r -p <entree> <sortie>")
            continue

        if cmd == "base64" and "-d" in low:
            if bin_ in low and txt in low:
                print(f"Fichier '{txt}' créé : contenu base64 déchiffré.")
                print(f"SUCCESS: base64 décodée, le drapeau est dans {txt}.")
                if not challenge_state[4]:
                    challenge_state[4] = True
                    print("\nVous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print("Usage: base64 -d <entree> <sortie>")
            continue

        if cmd == "echo":
            submitted = " ".join(args).strip()
            if submitted == final_flag:
                print(f"Flag valide : {final_flag}")
                print("SUCCESS: Niveau BONUS terminé ! Réussite totale, le drapeau est capturé.")
                if not challenge_state[6]:
                    challenge_state[6] = True
                    print("\nVous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
            elif submitted.lower().startswith("tw_bonus"):
                print("Flag incorrect, réessayez.")
                print(f"Indice : lisez {txt} puis soumettez la valeur exacte.")
            else:
                print(submitted)
            continue

        if cmd == "file" and bin_ in low:
            print(f"{bin_}: ASCII text")
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