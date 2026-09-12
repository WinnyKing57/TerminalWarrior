import random
import pyfiglet

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Exécuter 'uname -a' pour identifier le système.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Exécuter 'uptime' pour vérifier la charge et la durée de fonctionnement.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Exécuter 'free -h' pour vérifier la mémoire disponible.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Exécuter 'df -h' pour vérifier l'espace disque.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Exécuter 'ps aux' pour lister les processus en cours et repérer le processus suspect.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Exécuter 'pgrep -f cryptominer' pour obtenir son PID.",
        "",
        f"{'✅' if state[7] else '◻️'} 7) Exécuter 'kill -9 <PID>' pour arrêter le processus malveillant.",
        "",
    ]

def print_help():
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche les défis en cours")
    print(" exit - Quitte le terminal")
    print(" uname -a - Affiche les informations du noyau")
    print(" uptime - Affiche la durée de fonctionnement et la charge")
    print(" free -h - Affiche la mémoire en format lisible")
    print(" df -h - Affiche l'espace disque en format lisible")
    print(" ps aux - Liste tous les processus en cours")
    print(" top - Affiche les processus en temps réel")
    print(" pgrep -f <motif> - Recherche un processus par nom")
    print(" kill -9 <PID> - Termine un processus")
    print(" pwd - Affiche le répertoire courant (Print Working Directory)")
    print(" whoami - Affiche l'utilisateur courant")

def print_challenges(state):
    for line in build_challenge_list(state):
        print(line)

def main():
    challenge_state = {i: False for i in range(1, 8)}

    processes = random.randint(400, 700)
    memoryusage = random.randint(4000, 8000)
    time1 = random.randint(1, 24)
    time2 = random.randint(10, 59)
    time3 = random.randint(10, 59)
    day = random.randint(1, 28)
    ip_parts = [str(random.randint(10, 100)) for _ in range(4)]
    ip_address = ".".join(ip_parts)

    miner_pid = random.randint(4000, 4999)
    miner_cpu = random.randint(60, 98)
    miner_mem = random.randint(100, 500)

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="slant")
    print(ascii_banner)
    print("\nBienvenue au niveau 6 (PROCESSUS ET SURVEILLANCE) réalisé par (TerminalWarrior)\n")
    print("Un mineur de cryptomonnaie s'exécute en secret sur cette machine.")
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
    print(f"System load: 4.72               Processes:          {processes}")
    print("Usage of /:   68.13% of 49.11GB  Users logged in:     1")
    print(
        f"Memory usage: {memoryusage}MB             IP address for eth0: {ip_address}")
    print("Swap usage:   12%\n")
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

        if cmd == "uname":
            print(f"Linux ubuntu 5.15.0-91-generic #{{101-Ubuntu SMP Tue Nov 12 14:48:03 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux")
            if not challenge_state[1]:
                challenge_state[1] = True
                print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "uptime":
            print(f"  {time1:02d}:{time2:02d}:{time3:02d} up 14 days,  3:42,  1 user,  load average: 4.72, 3.51, 2.08")
            if not challenge_state[2]:
                challenge_state[2] = True
                print("\nVous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "free":
            print("              total        used        free      shared  buff/cache   available")
            print("Mem:        7.7Gi       6.1Gi       268Mi        12Mi       1.4Gi       1.1Gi")
            print("Swap:       2.0Gi       512Mi       1.5Gi")
            if not challenge_state[3]:
                challenge_state[3] = True
                print("\nVous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "df":
            print("Filesystem     1K-blocks    Used Available Use% Mounted on")
            print("tmpfs            2954728    1456   2953272   1% /run")
            print("/dev/sda5      102640652 49103048  48314500  71% /")
            print("tmpfs           14773596       0  14773596   0% /dev/shm")
            if not challenge_state[4]:
                challenge_state[4] = True
                print("\nVous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "ps":
            print("USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND")
            print("root         1  0.0  0.1 169932 14344 ?        Ss   Oct02   0:08 /sbin/init")
            print("root       320  0.0  0.0  27520  3508 ?        S    Oct02   0:00 /usr/sbin/sshd -D")
            print("user       1010  0.2  0.3 263304 16412 ?        S    09:10   0:05 python3 /usr/local/bin/agent.py")
            print(f"user      {miner_pid} {miner_cpu}  6.5 3210004 612240 ?     Sl    Oct02 481:32 ./cryptominer --pool xmr-eu")
            print("user       1911  0.0  0.1 185332 10988 tty1     S    09:11   0:00 bash")
            print("\nUn processus 'cryptominer' consomme énormément de CPU, il est suspect !")
            if not challenge_state[5]:
                challenge_state[5] = True
                print("\nVous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "top":
            print("top - 13:44:10 up 14 days,  3:42,  1 user,  load average: 4.72, 3.51, 2.08")
            print(f"Tasks: 231 total,   2 running, 228 sleeping,   0 stopped,   1 zombie")
            print(f"%Cpu(s): {miner_cpu} us,  1.2 sy,  0.0 ni, 20.5 id,  0.0 wa,  0.0 hi,  0.0 si")
            print(f"  PID USER      PR  NI    VIRT    RES  %CPU %MEM     TIME+ COMMAND")
            print(f" {miner_pid} user      20   0 3210004 612240  {miner_cpu}  6.5 481:32.14 cryptominer")
            print(" 1234 user      20   0  263304 16412  0.2  0.3   0:05.11 agent.py")
            print("\nLe processus 'cryptominer' domine le haut de la liste : il est suspect !")
            if not challenge_state[5]:
                challenge_state[5] = True
                print("\nVous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "pgrep":
            match_name = " ".join(args)
            if "cryptominer" in match_name:
                print(miner_pid)
                if not challenge_state[6]:
                    challenge_state[6] = True
                    print("\nVous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print(f"pgrep: no process found for '{match_name}'")
            continue

        if cmd == "kill":
            target = None
            for arg in args:
                if arg.lstrip("-").isdigit():
                    target = int(arg.lstrip("-"))
            if target is None:
                print("Usage: kill [-9 <PID>] <PID>")
                continue
            if target == miner_pid:
                print(f"Signal sent to process {miner_pid} (cryptominer)")
                print("SUCCESS: Le processus malveillant a été arrêté, la charge CPU revient à la normale.")
                if not challenge_state[7]:
                    challenge_state[7] = True
                    print("\nVous avez terminé le défi 7 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print(f"kill: ({target}) - No such process")
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