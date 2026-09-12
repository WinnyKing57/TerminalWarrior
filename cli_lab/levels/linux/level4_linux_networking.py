import random
import pyfiglet

def build_challenge_list(state):
    return [
        "",
        f"{'✅' if state[1] else '◻️'} 1) Exécuter 'ping 8.8.8.8' pour tester la connectivité réseau.",
        "",
        f"{'✅' if state[2] else '◻️'} 2) Exécuter 'traceroute google.com' pour tracer la route vers un hôte.",
        "",
        f"{'✅' if state[3] else '◻️'} 3) Exécuter 'ifconfig' ou 'ip addr' pour voir les interfaces réseau.",
        "",
        f"{'✅' if state[4] else '◻️'} 4) Exécuter 'netstat -tuln' pour afficher les ports en écoute.",
        "",
        f"{'✅' if state[5] else '◻️'} 5) Exécuter 'nslookup google.com' ou 'dig google.com' pour résoudre le DNS.",
        "",
        f"{'✅' if state[6] else '◻️'} 6) Exécuter 'ssh user@localhost' pour tester la connexion SSH (mot de passe : user).",
        "",
        f"{'✅' if state[7] else '◻️'} 7) Utiliser 'nmap localhost' pour scanner les ports ouverts.",
        "",
    ]

def print_help():
    print(" help - Affiche ce menu d'aide")
    print(" challenge - Affiche les défis en cours")
    print(" exit - Quitte le terminal")
    print(" ping <hôte> - Teste la connectivité réseau")
    print(" traceroute <hôte> - Trace la route vers un hôte")
    print(" ifconfig - Affiche les interfaces réseau (obsolète, utiliser 'ip addr')")
    print(" ip addr - Affiche les interfaces réseau")
    print(" netstat -tuln - Affiche les ports en écoute")
    print(" nslookup <hôte> - Résout un nom DNS")
    print(" dig <hôte> - Outil alternatif de résolution DNS")
    print(" ssh <utilisateur@hôte> - Se connecte via SSH")
    print(" nmap <hôte> - Scanne les ports réseau")
    print(" pwd - Affiche le répertoire courant (Print Working Directory)")
    print(" whoami - Affiche l'utilisateur courant")

def print_challenges(state):
    for line in build_challenge_list(state):
        print(line)

def main():
    challenge_state = {i: False for i in range(1, 8)}
    
    processes = random.randint(100, 200)
    memoryusage = random.randint(50, 150)
    time1 = random.randint(1, 24)
    time2 = random.randint(10, 59)
    time3 = random.randint(10, 59)
    day = random.randint(1, 28)
    ip_parts = [str(random.randint(10, 100)) for _ in range(4)]
    ip_address = ".".join(ip_parts)

    ascii_banner = pyfiglet.figlet_format("TERMINALWARRIOR", font="slant")
    print(ascii_banner)
    print("\nBienvenue au niveau 4 (RÉSEAU) réalisé par (Diversion/diverter)\n")
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
    user_password = "user"
    ssh_port = 22
    open_ports = ["22", "80", "443", "53"]
    network_interfaces = [
        "eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP",
        "lo: <LOOPBACK,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP"
    ]
    
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

        if cmd == "ping":
            if len(args) < 1:
                print("Usage: ping <host>")
                continue
            host = args[0]
            if host in ["8.8.8.8", "google.com"]:
                print("PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.")
                print("64 bytes from 8.8.8.8: icmp_seq=1 ttl=119 time=25.3 ms")
                print("64 bytes from 8.8.8.8: icmp_seq=2 ttl=119 time=24.8 ms")
                if not challenge_state[1]:
                    challenge_state[1] = True
                    print("\nVous avez terminé le défi 1 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print(f"ping: unknown host {host}")
            continue

        if cmd == "traceroute":
            if len(args) < 1:
                print("Usage: traceroute <host>")
                continue
            host = args[0]
            if host == "google.com":
                print("traceroute to google.com (142.250.74.14), 30 hops max, 60 byte packets")
                print(" 1  192.168.1.1  1.234 ms  1.123 ms  1.098 ms")
                print(" 2  10.0.0.1  5.432 ms  5.321 ms  5.210 ms")
                print(" 3  142.250.74.14  25.345 ms  25.678 ms  25.901 ms")
                if not challenge_state[2]:
                    challenge_state[2] = True
                    print("Vous avez terminé le défi 2 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print(f"traceroute: unknown host {host}")
            continue

        if cmd in ["ifconfig", "ip"]:
            if len(args) == 0 or args == ["addr"]:
                print("1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UP")
                print("    inet 127.0.0.1/8 scope host lo")
                print("    inet6 ::1/128 scope host")
                print("2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP")
                print("    inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0")
                print("    inet6 fe80::1234:5678:9abc:def0/64 scope link")
                if not challenge_state[3]:
                    challenge_state[3] = True
                    print("Vous avez terminé le défi 3 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print("Usage: ip addr or ifconfig")
            continue

        if cmd == "netstat":
            if len(args) == 1 and args[0] == "-tuln":
                print("Active Internet connections (only servers)")
                print("Proto Recv-Q Send-Q Local Address           Foreign Address         State")
                print("tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN")
                print("tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN")
                print("tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN")
                print("udp        0      0 0.0.0.0:53              0.0.0.0:*               LISTEN")
                if not challenge_state[4]:
                    challenge_state[4] = True
                    print("Vous avez terminé le défi 4 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print("Usage: netstat -tuln")
            continue

        if cmd in ["nslookup", "dig"]:
            if len(args) < 1:
                print("Usage: nslookup <host> or dig <host>")
                continue
            host = args[0]
            if host == "google.com":
                print("Server:		8.8.8.8")
                print("Address:	8.8.8.8:53")
                print("")
                print("Non-authoritative answer:")
                print("Name:	google.com")
                print("Address: 142.250.74.14")
                print("Name:	google.com")
                print("Address: 2a00:1450:4009:80c::200e")
                if not challenge_state[5]:
                    challenge_state[5] = True
                    print("Vous avez terminé le défi 5 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print(f"nslookup: unable to resolve {host}: Unknown host")
            continue

        if cmd == "ssh":
            if len(args) < 1:
                print("Usage: ssh <user@host>")
                continue
            connection = args[0]
            if connection == "user@localhost":
                password_input = input("user@localhost's password: ").strip()
                if password_input == user_password:
                    print("Linux 5.15.0-91-generic x86_64")
                    print("Last login: Thu Oct 3 12:00:00 2025 from 127.0.0.1")
                    print("user@localhost:~$ ")
                    if not challenge_state[6]:
                        challenge_state[6] = True
                        print("Vous avez terminé le défi 6 ! Tapez 'challenge' pour voir votre progression.")
                else:
                    print("Permission denied")
            else:
                print(f"ssh: connect to host {connection.split('@')[1]} port 22: Connection refused")
            continue

        if cmd == "nmap":
            if len(args) < 1:
                print("Usage: nmap <host>")
                continue
            host = args[0]
            if host == "localhost":
                print("Starting Nmap 7.80 ( https://nmap.org ) at 2025-10-03 12:00 UTC")
                print("Nmap scan report for localhost (127.0.0.1)")
                print("Host is up (0.00012s latency).")
                print("")
                print("PORT   STATE SERVICE")
                print("22/tcp open  ssh")
                print("80/tcp open  http")
                print("443/tcp open https")
                print("53/tcp open  domain")
                if not challenge_state[7]:
                    challenge_state[7] = True
                    print("Vous avez terminé le défi 7 ! Tapez 'challenge' pour voir votre progression.")
            else:
                print(f"Nmap scan report for {host}")
                print("Host is up (0.00012s latency).")
                print("")
                print("PORT   STATE SERVICE")
                print("22/tcp open  ssh")
                if not challenge_state[7]:
                    challenge_state[7] = True
                    print("Vous avez terminé le défi 7 ! Tapez 'challenge' pour voir votre progression.")
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