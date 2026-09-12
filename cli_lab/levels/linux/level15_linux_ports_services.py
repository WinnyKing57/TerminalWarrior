import random
import pyfiglet

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Exécuter 'netstat -tulpn' pour lister les ports en écoute.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Exécuter 'ss -tulpn' pour afficher les sockets d'écoute.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Exécuter 'lsof -i :31337' pour identifier le processus suspect.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Exécuter 'nmap localhost' pour scanner les ports locaux.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Exécuter 'curl http://localhost:31337' pour interagir avec le service.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Exécuter 'kill -9 <PID>' pour terminer le processus suspect.",
        "",
        f"{'✅' if state[7] else '◻️'} 7) Exécuter 'netstat -tulpn' pour vérifier que le port 31337 est fermé.",
        "",
    ]

def print_help():
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche les défis en cours")
    print(" exit - Quitte le terminal")
    print(" netstat -tulpn - Affiche les ports en écoute")
    print(" ss -tulpn - Affiche les sockets d'écoute")
    print(" lsof -i :<port> - Identifie le processus sur un port")
    print(" nmap <cible> - Scanne les ports ouverts")
    print(" curl http://<hote>:<port> - Interroge un service")
    print(" kill -9 <PID> - Termine un processus")
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
    evil_pid = random.randint(2500, 3999)

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="slant")
    print(ascii_banner)
    print("\nBienvenue au niveau 15 (PORTS ET SERVICES RÉSEAU) réalisé par (TerminalWarrior)\n")
    print("Un service inconnu écoute sur le port 31337. Identifiez-le et mettez-y fin.")
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
    print(f"System load: 0.29               Processes:          {random.randint(280, 380)}")
    print("Usage of /:   39.88% of 49.11GB  Users logged in:     1")
    print("Memory usage: 1322MB             IP address for eth0: 10.0.2.15")
    print("Swap usage:   0%\n")
    print("0 updates can be applied immediately\n")
    print("Last Login: Thu Oct 3 12:00:00 UTC 2025\n")

    current_directory = "~"
    listener_alive = True

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

        if cmd == "netstat":
            if not listener_alive:
                print("Active Internet connections (servers and established)")
                print("Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name")
                print("tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      sshd")
                print("tcp6       0      0 :::80                    :::*                    LISTEN      apache2")
                print("\nLe port 31337 n'apparaît plus : le service suspect a été arrêté.")
                if not challenge_state[7]:
                    challenge_state[7] = True
                    print("\nVous avez terminé le défi 7 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print("Active Internet connections (servers and established)")
                print("Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name")
                print("tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      sshd")
                print("tcp6       0      0 :::80                    :::*                    LISTEN      apache2")
                print(f"tcp        0      0 0.0.0.0:31337            0.0.0.0:*               LISTEN      {evil_pid}/nc")
                if not challenge_state[1]:
                    challenge_state[1] = True
                    print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
                print("\nLe service nc (netcat) en écoute sur 31337 est suspect !")
            continue

        if cmd == "ss":
            print("Netid State  Recv-Q Send-Q  Local Address:Port  Peer Address:Port  Process")
            print(f"tcp   LISTEN 0      10     0.0.0.0:31337         0.0.0.0:*          users:((\"nc\",pid={evil_pid},fd=3))")
            if not challenge_state[2]:
                challenge_state[2] = True
                print("\nVous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "lsof" and ":31337" in low:
            print(f"COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME")
            print(f"nc      {evil_pid} user   3u   IPv4 12345      0t0  TCP *:31337 (LISTEN)")
            if not challenge_state[3]:
                challenge_state[3] = True
                print("\nVous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "nmap":
            print("Starting Nmap 7.80 ( https://nmap.org ) at 2025-10-03 12:00 UTC")
            print("Nmap scan report for localhost (127.0.0.1)")
            print("Host is up (0.00042s latency).")
            print("Not shown: 996 closed ports")
            print("PORT      STATE SERVICE")
            print("22/tcp    open  ssh")
            print("80/tcp    open  http")
            if listener_alive:
                print("31337/tcp open  Elite  ← service inconnu !")
            print("\nNmap done: 1 IP address (1 host up) scanned in 0.06 seconds")
            if not challenge_state[4]:
                challenge_state[4] = True
                print("\nVous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "curl" and "31337" in low:
            if listener_alive:
                print("Bienvenue sur le service 31337.")
                print("Tapez 'shell' pour obtenir un shell...")
                print("\nCe service propose un shell distant : c'est une backdoor !")
            else:
                print("curl: (7) Failed to connect to localhost port 31337: Connection refused")
            if not challenge_state[5]:
                challenge_state[5] = True
                print("\nVous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
            continue

        if cmd == "kill":
            target = None
            for arg in args:
                if arg.lstrip("-").isdigit():
                    target = int(arg.lstrip("-"))
            if target == evil_pid:
                listener_alive = False
                print(f"Signal envoyé au processus {evil_pid} (nc)")
                print("SUCCESS: le service backdoor a été arrêté.")
                if not challenge_state[6]:
                    challenge_state[6] = True
                    print("\nVous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
            elif target is not None:
                print(f"kill: ({target}) - No such process")
            else:
                print("Usage: kill -9 <PID>")
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