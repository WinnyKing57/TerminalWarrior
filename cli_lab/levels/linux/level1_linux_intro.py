import random
import pyfiglet


def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Lire le fichier Flag.txt.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Trouver le nom d'utilisateur ssh de l'autre ordinateur.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Trouver le mot de passe ssh de l'autre ordinateur.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Trouver l'adresse IP de l'autre ordinateur.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Se connecter en ssh à l'autre ordinateur.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Trouver hidden.txt et le lire sur l'autre ordinateur.",
        "",
    ]


def print_help():
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche la liste des défis et votre progression")
    print(" exit - Quitte le terminal")
    print(" ls / ls -la - Liste les fichiers du répertoire courant")
    print(" cat <fichier> - Lit un fichier, cat est l'abréviation de concatenate")
    print(" cd <dossier> - Change de répertoire")
    print(" pwd - Affiche le chemin du répertoire courant (Print Working Directory)")
    print(" whoami - Affiche le nom de l'utilisateur actuellement connecté")
    print(" ssh <Utilisateur>@<IP> - Crée une connexion sécurisée à un autre ordinateur")


def print_challenges(state):
    for line in build_challenge_list(state):
        print(line)


def main():

    challenge_state = {i: False for i in range(1, 7)}

    processes = random.randint(100, 200)
    memoryusage = random.randint(100, 800)
    time1 = random.randint(1, 24)
    time2 = random.randint(10, 59)
    time3 = random.randint(10, 59)
    day = random.randint(1, 28)
    ip_parts = [str(random.randint(1, 254)) for _ in range(4)]
    other_ip_address = ".".join(ip_parts)
    ip_address = ".".join(ip_parts)

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="small")
    print(ascii_banner)

    print("\nBienvenue au niveau 1 (INTRO) réalisé par (Diversion/diversionsec)\n")
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
    print(f"System load: 0.00               Processes:          {processes}")
    print("Usage of /:   20.75% of 49.11GB  Users logged in:     1")
    print(
        f"Memory usage: {memoryusage}MB             IP address for eth0: {ip_address}")
    print("Swap usage:   0%\n")
    print("0 updates can be applied immediately\n")
    print("Last Login: Thu Oct 3 12:00:00 UTC 2025\n")

    current_directory = "~"
    ssh_username = ['JoeBiden', 'DonaldTrump', 'JeremyClarkson', 'RichardHammond',
                    'JamesMay', 'GordonRamsay', 'ColdPlay', 'JeffreyDahmer', 'HarryPotter', 'KimJongUn']
    ssh_password = ['DumbassLeftHisPassword', 'Password123!', 'ILeftMyKeysAgain', 'Admin1234', 'qwerty_is_bad',
                    'LetMeInPlease', 'Eggcellent123', 'Passw0rd!', 'ThisIsNotASecurePass', 'ForgottenPassword69',]
    randomusername = random.choice(ssh_username)
    randompassword = random.choice(ssh_password)
    on_remote = False

    while True:
        if on_remote:
            prompt = f"{randomusername}@linux:~$ "
        else:
            prompt = f"user@linux:{current_directory}$ "

        command = input(prompt).strip()

        if command == "help":
            print_help()
            continue

        if command == "exit":
            if on_remote:
                print("Déconnexion de la machine distante.")
                on_remote = False
                continue
            print("Au revoir")
            break

        if command == "challenge":
            print()
            print_challenges(challenge_state)
            print()
            continue

        if not on_remote:

            if command == "ls":
                if current_directory == "~":
                    print("Bin.txt  Flag  notes.txt  Documents")
                elif current_directory == "~/Flag":
                    print("Flag.txt  something.txt  birthday.txt")
                elif current_directory == "~/Documents":
                    print("ssh_Username.txt  ssh_Password.txt")
            elif command == "pwd":
                print("/home/user" + ("" if current_directory ==
                      "~" else current_directory[1:]))
            elif command == "whoami":
                print("user")
            elif command == "cd Flag":
                current_directory = "~/Flag"
            elif command == "cd Documents":
                current_directory = "~/Documents"
            elif command == "cd ..":
                current_directory = "~"
            elif command.startswith("cat "):
                filename = command[4:]

                if current_directory == "~":
                    if filename == "notes.txt":
                        print(
                            f"L'adresse IP ssh de l'autre ordinateur est {other_ip_address}")
                        if not challenge_state[4]:
                            challenge_state[4] = True
                            print(
                                "Vous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
                    elif filename == "Bin.txt":
                        print("Juste des notes binaires au hasard...")
                    else:
                        print(f"cat: {filename}: No such file")
                elif current_directory == "~/Flag":
                    if filename == "Flag.txt":
                        print(
                            "Vous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
                        challenge_state[1] = True
                    elif filename == "birthday.txt":
                        print("Joyeux anniversaire John !")
                    elif filename == "something.txt":
                        print("Je ne sais pas quoi mettre ici.")
                    else:
                        print(f"cat: {filename}: No such file")
                elif current_directory == "~/Documents":
                    if filename == "ssh_Username.txt":
                        print("Vous avez trouvé le fichier ssh_Username.txt !")
                        print("Utilisateur :", randomusername)
                        if not challenge_state[2]:
                            challenge_state[2] = True
                            print(
                                "Vous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
                    elif filename == "ssh_Password.txt":
                        print("Vous avez trouvé le fichier ssh_Password.txt !")
                        print("Mot de passe :", randompassword)
                        if not challenge_state[3]:
                            challenge_state[3] = True
                            print(
                                "Vous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
                    else:
                        print(f"cat: {filename}: No such file")
                else:
                    print(f"cat: {filename}: No such file")
            elif command == "ssh " + randomusername + "@" + other_ip_address + "":
                print("Tentative de connexion ssh à l'autre ordinateur...")
                password_input = input("Password: ").strip()

                if password_input == randompassword:
                    print(
                        "Identifiants corrects. Connexion ssh réussie à l'autre ordinateur.")
                    on_remote = True
                    if not challenge_state[5]:
                        challenge_state[5] = True
                        print(
                            "Vous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
                else:
                    print("Authentication failed.")
            elif command == "":
                continue
            else:
                print(f"{command}: command not found")
        else:
            if command == "ls":
                print("Utilisez ls -la pour trouver le fichier hidden.txt")
            elif command == "ls -la":
                print(".  ..  hidden.txt")
            elif command == "cat hidden.txt":
                print("Vous avez trouvé hidden.txt ! Défi 6 terminé !")
                if not challenge_state[6]:
                    challenge_state[6] = True
                    print("Tapez 'challenge' pour voir votre progression.")
            elif command == "":
                continue
            else:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()