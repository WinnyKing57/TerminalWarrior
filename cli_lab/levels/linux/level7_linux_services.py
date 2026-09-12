import random
import pyfiglet

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Exécuter 'systemctl list-units --type=service' pour lister les services actifs.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Exécuter 'systemctl status backdoor.service' pour inspecter le service suspect.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Exécuter 'journalctl -u backdoor.service' pour lire les journaux du service.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Exécuter 'systemctl stop backdoor.service' pour arrêter le service.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Exécuter 'systemctl disable backdoor.service' pour empêcher son démarrage automatique.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Exécuter 'systemctl enable sshd' pour réactiver le service SSH.",
        "",
    ]

def print_help():
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche les défis en cours")
    print(" exit - Quitte le terminal")
    print(" systemctl list-units --type=service - Liste les services actifs")
    print(" systemctl status <service> - Affiche l'état d'un service")
    print(" systemctl start <service> - Démarre un service")
    print(" systemctl stop <service> - Arrête un service")
    print(" systemctl enable <service> - Active un service au démarrage")
    print(" systemctl disable <service> - Désactive un service au démarrage")
    print(" journalctl -u <service> - Affiche les journaux d'un service")
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
    ip_parts = [str(random.randint(10, 100)) for _ in range(4)]
    ip_address = ".".join(ip_parts)

    service_pid = random.randint(3000, 3999)

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="slant")
    print(ascii_banner)
    print("\nBienvenue au niveau 7 (SERVICES ET SYSTEMD) réalisé par (TerminalWarrior)\n")
    print("Un service 'backdoor.service' s'exécute en arrière-plan et ouvre une porte dérobée.")
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
    print("System load: 0.81               Processes:          356")
    print("Usage of /:   42.05% of 49.11GB  Users logged in:     1")
    print(
        f"Memory usage: 1522MB             IP address for eth0: {ip_address}")
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

        if cmd == "systemctl":
            if len(args) < 1:
                print("Usage: systemctl <subcommand> [service]")
                continue

            subcommand = args[0]
            rest = " ".join(args[1:])

            if subcommand == "list-units":
                print("  UNIT                                   LOAD   ACTIVE SUB")
                print("  cron.service                           loaded active running")
                print("  sshd.service                           loaded inactive dead")
                print("  backdoor.service                       loaded active running")
                print("  networking.service                     loaded active running")
                print("  systemd-journald.service               loaded active running")
                print("\nLe service 'backdoor.service' est actif : il est suspect !")
                if not challenge_state[1]:
                    challenge_state[1] = True
                    print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
            elif subcommand == "status":
                if "backdoor.service" in rest:
                    print(f"● backdoor.service - Remote tunnel backdoor")
                    print(f"     Loaded: loaded (/etc/systemd/system/backdoor.service; enabled; vendor preset: enabled)")
                    print(f"     Active: active (running) since Tue 2025-10-0{day} {time1:02d}:{time2:02d}:{time3:02d} UTC; 3 days ago")
                    print(f"   Main PID: {service_pid} (nc)")
                    print(f"     Status: \"Listening on 0.0.0.0:4444\"")
                    print(f"      Tasks: 1 (limit: 4576)")
                    print(f"     Memory: 4.2M")
                    print("     CGroup: /system.slice/backdoor.service")
                    print(f"             └─{service_pid} /bin/nc -lvnp 4444")
                    print("\nCe service écoute sur le port 4444 : c'est une porte dérobée !")
                    if not challenge_state[2]:
                        challenge_state[2] = True
                        print("\nVous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
                elif rest:
                    print(f"● {rest} - Service systemd")
                    print("   Loaded: loaded (/lib/systemd/system/" + rest + "; enabled; vendor preset: enabled)")
                    print("   Active: inactive (dead)")
                else:
                    print("Usage: systemctl status <service>")
            elif subcommand == "stop":
                if "backdoor.service" in rest:
                    print("Removing stop job for service 'backdoor.service'...")
                    print("Stopping 'backdoor.service'...")
                    print("SUCCESS: Le service 'backdoor.service' s'est arrêté.")
                    if not challenge_state[4]:
                        challenge_state[4] = True
                        print("\nVous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
                elif rest:
                    print(f"Stopping service '{rest}'...")
                else:
                    print("Usage: systemctl stop <service>")
            elif subcommand == "disable":
                if "backdoor.service" in rest:
                    print(f"Removed /etc/systemd/system/multi-user.target.wants/backdoor.service.")
                    print("SUCCESS: Le service 'backdoor.service' est désormais désactivé au démarrage.")
                    if not challenge_state[5]:
                        challenge_state[5] = True
                        print("\nVous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
                elif rest:
                    print(f"Removed /etc/systemd/system/multi-user.target.wants/{rest}.")
                else:
                    print("Usage: systemctl disable <service>")
            elif subcommand == "enable":
                if "sshd" in rest or "ssh" in rest:
                    print(f"Synchronizing state of ssh.service with SysV service script with /lib/systemd/systemd-sysv-install.")
                    print("Executing: /lib/systemd/systemd-sysv-install enable ssh")
                    print("Created symlink /etc/systemd/system/multi-user.target.wants/ssh.service → /lib/systemd/system/ssh.service.")
                    print("SUCCESS: Le service SSH est activé et démarrera au prochain démarrage.")
                    if not challenge_state[6]:
                        challenge_state[6] = True
                        print("\nVous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
                elif rest:
                    print(f"Created symlink /etc/systemd/system/multi-user.target.wants/{rest}.")
                else:
                    print("Usage: systemctl enable <service>")
            elif subcommand == "start":
                if rest:
                    print(f"Starting service '{rest}'...")
                    print(f"Job for {rest} started successfully.")
                else:
                    print("Usage: systemctl start <service>")
            else:
                print(f"systemctl: unknown subcommand '{subcommand}'")
            continue

        if cmd == "journalctl":
            if len(args) >= 1 and args[0] == "-u":
                unit = " ".join(args[1:]) if len(args) > 1 else ""
                if "backdoor.service" in unit:
                    print("-- Logs begin at Mon 2025-09-29 08:00:00 UTC, end at Thu 2025-10-03 12:00:00 UTC --")
                    print("Oct 01 22:14:03 ubuntu systemd[1]: Started Remote tunnel backdoor.")
                    print("Oct 01 22:14:03 ubuntu nc[3121]: listening on [any] 4444 ...")
                    print("Oct 02 03:42:11 ubuntu nc[3121]: connect to [10.0.2.15:4444] from [185.220.101.4:56012]")
                    print("Oct 02 03:42:11 ubuntu nc[3121]: user:root password:toor")
                    print("Oct 02 03:42:11 ubuntu nc[3121]: session: sender -> host (see shell)")
                    print("\nLes journaux montrent des connexions entrantes suspectes depuis une IP étrangère.")
                    if not challenge_state[3]:
                        challenge_state[3] = True
                        print("\nVous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
                elif unit:
                    print(f"-- Logs for unit {unit} --")
                    print("No entries")
                else:
                    print("Usage: journalctl -u <service>")
            else:
                print("Usage: journalctl -u <service>")
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