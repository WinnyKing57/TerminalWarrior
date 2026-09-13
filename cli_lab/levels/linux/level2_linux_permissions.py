import random
import pyfiglet


def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Utiliser ls -la pour trouver le fichier verrouillé hidden_data.txt.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Utiliser read pour identifier les permissions de hidden_data.txt.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Utiliser su pour passer à l'utilisateur root.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Utiliser chown pour changer le propriétaire de hidden_data.txt en user.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Relire hidden_data.txt avec read pour confirmer l'accès.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Exécuter ls pour trouver HelloWorld.exe puis read dessus.",
        "",
        f"{'✅' if state[7] else '◻️'} 7) Passer à root avec su, chmod 777 sur HelloWorld.exe, puis relire avec read pour finir le défi.",
        "",
    ]


def print_help():
    print("=" * 60)
    print("      TERMINAL WARRIOR - AIDE DU NIVEAU 2 (PERMISSIONS)")
    print("=" * 60)
    print("")
    print(" OBJECTIF :")
    print("   Récupérer le contenu de deux fichiers protégés en manipulant")
    print("   les permissions et les propriétaires (chmod / chown) ainsi que")
    print("   les changements d'utilisateur (su).")
    print("")
    print(" COMMANDES :")
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche la liste des défis et votre progression")
    print(" exit - Quitte le terminal")
    print(" ls - Liste les fichiers du répertoire courant")
    print(" ls -la - Liste tous les fichiers et leurs permissions")
    print(" read <fichier> - Lit un fichier ou inspecte ses permissions")
    print(" cat <fichier> - Alias de read")
    print(" pwd - Affiche le répertoire courant (Print Working Directory)")
    print(" whoami - Affiche l'utilisateur courant")
    print(" su <utilisateur> - Change d'utilisateur")
    print(" chmod <octal> <fichier> - Modifie les permissions du fichier, en savoir plus sur les permissions octales sur https://www.linux.com/training-tutorials/understanding-linux-file-permissions/")
    print(" chown <utilisateur> <fichier> - Modifie le propriétaire du fichier")
    print("")
    print(" COMMENT LIRE LES PERMISSIONS (rw-r-----) :")
    print("   r = lecture, w = écriture, x = exécution, - = aucun droit.")
    print("   3 blocs : propriétaire | groupe | autres utilisateurs.")
    print("   Exemple 'rw-r-----' : le propriétaire lit/écrit, le groupe")
    print("   lit, les autres n'ont aucun accès.")
    print("")
    print(" DÉROULÉ CONSEILLÉ :")
    print(" 1. 'ls -la' : affiche hidden_data.txt et les permissions actuelles.")
    print(" 2. 'read hidden_data.txt' : on voit ses permissions. Vous êtes 'user'")
    print("    mais le fichier appartient à 'root' -> Accès refusé (logique !).")
    print(" 3. 'su root' (mot de passe : toor) : devenez root pour tout pouvoir.")
    print(" 4. 'chown user hidden_data.txt' : donnez la propriété du fichier à")
    print("    l'utilisateur 'user'.")
    print(" 5. Revenez sur votre session avec 'su user' (sans mot de passe).")
    print(" 6. 'read hidden_data.txt' : maintenant 'user' est propriétaire,")
    print("    la lecture est autorisée !")
    print(" 7. Pour HelloWorld.exe c'est le même principe : 'su root',")
    print("    'chmod 777 HelloWorld.exe' (donne tous les droits à tout le monde),")
    print("    puis 'read HelloWorld.exe'.")
    print("")
    print(" ASTUCE : un fichier en lecture mais dont vous n'êtes pas propriétaire")
    print(" sera refusé. Vérifiez à tout moment 'whoami' et 'ls -la'.")


def print_challenges(state):
    for line in build_challenge_list(state):
        print(line)


def main():

    challenge_state = {i: False for i in range(1, 8)}

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

    print("\nBienvenue au niveau 2 (PERMISSIONS & PROPRIÉTÉ) réalisé par (Diversion/diversionsec)\n")
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
    current_user = "user"
    root_password = "toor"

    hidden_data_owner = "root"
    hidden_data_group = "root"
    hidden_data_perms = "rw-r-----"

    helloworld_owner = "root"
    helloworld_group = "root"
    helloworld_perms = "rwx------"

    while True:

        prompt = f"{current_user}@linux:{current_directory}$ "
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

        if cmd == "ls":
            if len(args) == 0:
                print("HelloWorld.exe")
            elif args == ["-la"] or args == ["-l", "-a"]:
                print("drwxr-xr-x  2 user user 4096 Oct  3 12:00 .")
                print("drwxr-xr-x 10 user user 4096 Oct  3 12:00 ..")
                print(f"-rw-r-----  1 {hidden_data_owner} {hidden_data_group}   32 Oct  3 12:00 hidden_data.txt")
                print(f"-rw-r--r--  1 root root   16 Oct  3 12:00 root_password.txt")
                print(f"-{helloworld_perms}  1 {helloworld_owner} {helloworld_group} 8765 Oct  3 12:00 HelloWorld.exe")
                if not challenge_state[1]:
                    challenge_state[1] = True
                    print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print("ls: invalid option")
            continue

        if cmd in ["read", "cat"]:
            if len(args) == 0:
                print(f"{cmd}: missing file operand")
                continue
            filename = args[0]
            if filename == "hidden_data.txt":
                print(f"-{hidden_data_perms}  1 {hidden_data_owner} {hidden_data_group}   32 Oct  3 12:00 hidden_data.txt")
                if not challenge_state[2]:
                    challenge_state[2] = True
                    print("Vous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
                if current_user == "root" or hidden_data_owner == current_user:
                    print("Hidden data contents displayed.")
                    if current_user == "user" and hidden_data_owner == "user" and not challenge_state[5]:
                        challenge_state[5] = True
                        print("Vous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
                else:
                    print("Access denied: Permission denied.")
            elif filename == "root_password.txt":
                print("root: toor")
            elif filename == "HelloWorld.exe":
                print(f"-{helloworld_perms}  1 {helloworld_owner} {helloworld_group} 8765 Oct  3 12:00 HelloWorld.exe")
                if current_user == "user" and not challenge_state[6]:
                    challenge_state[6] = True
                    print("Vous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
                if current_user == "root" and helloworld_perms == "rwxrwxrwx":
                    print("HelloWorld.exe read successfully.")
                    if not challenge_state[7]:
                        challenge_state[7] = True
                        print("Vous avez terminé le défi 7 ! Tapez 'challenge' pour voir votre progression.")
                elif current_user == "root":
                    print("Access denied: File is not executable by all users.")
                else:
                    print("Access denied: Permission denied.")
            else:
                print(f"{cmd}: {filename}: No such file or directory")
            continue

        if cmd == "pwd":
            print("/home/user/Documents")
            continue

        if cmd == "whoami":
            print(current_user)
            continue

        if cmd == "su":
            if len(args) == 0:
                print("su: missing operand")
                continue
            target = args[0]
            if target == current_user:
                print(f"Already {current_user}.")
                continue
            if target == "root":
                password_input = input("Password: ").strip()
                if password_input == root_password:
                    current_user = "root"
                    print("Root access granted.")
                    if not challenge_state[3]:
                        challenge_state[3] = True
                        print("Vous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
                else:
                    print("Authentication failure")
            elif target == "user" and current_user == "root":
                current_user = "user"
                print("Switched to user.")
            else:
                print(f"su: user {target} does not exist")
            continue

        if cmd == "chown":
            if len(args) != 2:
                print("Usage: chown <username> <file>")
                continue
            if current_user != "root":
                print("chown: Permission denied")
                continue
            target_user, filename = args
            if filename != "hidden_data.txt":
                print(f"chown: cannot access '{filename}': No such file or directory")
                continue
            if target_user != "user":
                print(f"chown: invalid user: {target_user}")
                continue
            hidden_data_owner = "user"
            hidden_data_group = "user"
            print("Ownership of hidden_data.txt changed to user.")
            if not challenge_state[4]:
                challenge_state[4] = True
                print("Vous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "chmod":
            if len(args) != 2:
                print("Usage: chmod <octal> <file>")
                continue
            if current_user != "root":
                print("chmod: Permission denied")
                continue
            mode, filename = args
            if filename != "HelloWorld.exe":
                print(f"chmod: cannot access '{filename}': No such file or directory")
                continue
            if mode != "777":
                print("chmod: invalid mode. Try 777.")
                continue
            helloworld_perms = "rwxrwxrwx"
            print("Permissions of HelloWorld.exe changed to 777.")
            continue

        print(f"{cmd}: command not found")


    return all(challenge_state.values())

if __name__ == "__main__":
    main()
