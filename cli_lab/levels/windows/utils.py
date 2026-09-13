import os
import random
import time

# Shared Game State
CURRENT_DIR = "C:\\Users\\User"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    clear_screen()
    banner_width = 70
    print("*" * banner_width)
    print(f"** {title} **".center(banner_width))
    print("*" * banner_width)
    print("| PLATEFORME : Windows CTF par Therootexec")
    print("| STATUT :    État du système nominal.")
    print("| ASTUCE :    Tapez 'help' pour voir les commandes disponibles.")
    print("+" + "-" * banner_width + "+")
    print()

def print_objectives(objectives, hint=None):
    print(":: OBJECTIFS DE MISSION ACTUELS ::")
    for idx, obj in enumerate(objectives, start=1):
        print(f" [{idx}] {obj}")
    if hint:
        print(f"\n >> INDICE : {hint}")
    print(f"\n Objectifs : {len(objectives)} | Statut : EN COURS")
    print("-" * 50)
    print()

def print_success(message):
    print("\n" + "="*60)
    print(f" SUCCESS: {message}")
    print("="*60)
    input(" Appuyez sur ENTRÉE pour continuer...")

def print_objective_done(number):
    print(f"\nVous avez terminé l'objectif {number} ! Continuez avec la commande suivante.\n")

def print_windows_motd():
    build = random.choice(["10.0.19045.4046", "10.0.22621.2861", "10.0.19045.3930"])
    uptime_days = random.randint(0, 12)
    uptime_hours = random.randint(0, 23)
    uptime_minutes = random.randint(1, 59)
    processes = random.randint(95, 180)
    memory = random.randint(420, 2048)
    ip_address = ".".join(str(random.randint(1, 254)) for _ in range(4))

    print("=" * 60)
    print(f"Microsoft Windows [Version {build}]")
    print("(c) Microsoft Corporation. All rights reserved.")
    print("-" * 60)
    print("System information as of:", time.strftime("%a %b %d %H:%M:%S %Y"))
    print(f"System uptime: {uptime_days}d {uptime_hours}h {uptime_minutes}m")
    print(f"Processes: {processes}")
    print(f"Memory usage: {memory}MB")
    print(f"IPv4 Address: {ip_address}")
    print("=" * 60)
    print()

def build_prompt(current_dir):
    return f"User@WS-OPS-01:{current_dir}> "
def generic_cmd_handler(cmd, args, level_guide=None):
    if cmd in ["cls", "clear"]:
        clear_screen()
        return True
    elif cmd == "help" or cmd == "?":
        print("\n=== AIDE DES COMMANDES ===")
        print(" CORE:   help  cls  exit  whoami  pwd  echo")
        print(" FILE:   dir  cd  type  findstr  where  tree")
        print(" PERM:   attrib  takeown  icacls")
        print(" NET:    ipconfig  ping  tracert  netstat  arp  curl")
        print(" SYS:    reg  schtasks  sc  wevtutil  diskpart  wmic")
        print("\n EXPLICATIONS DES COMMANDES CLÉS :")
        print("  dir            - Liste les fichiers du dossier courant (ajoutez /a pour")
        print("                   révéler les fichiers cachés ou de système).")
        print("  cd <dossier>   - Change de dossier (cd .. revient au dossier parent).")
        print("  type <fichier> - Affiche le contenu d'un fichier texte.")
        print("  findstr ...    - Recherche une chaîne de caractères dans des fichiers.")
        print("  attrib <f>     - Affiche/modifie les attributs (H=caché, S=système).")
        print("  takeown /f <f> - Prend la propriété d'un fichier (nécessite des droits).")
        print("  icacls <f> /grant user:(F) - Octroie le contrôle total sur un fichier.")
        print("  ipconfig       - Affiche la configuration IP de la machine.")
        print("  ping <hôte>    - Teste la connectivité réseau.")
        print("  netstat -an    - Affiche les ports ouverts et les connexions actives.")
        print("  reg query ...  - Interroge le registre Windows.")
        print("  schtasks ...   - Gère les tâches planifiées (persistance).")
        print("  sc query ...   - Interroge l'état des services.")
        print("  wevtutil qe ...- Interroge les journaux d'événements.")
        print("  powershell \"...\" - Exécute une commande PowerShell.")
        if level_guide:
            print("\n--- CONSEILS DU NIVEAU EN COURS ---")
            for line in level_guide:
                print(" " + line)
        print("\nAstuce : utilisez 'dir /a' pour révéler les fichiers cachés.")
        return True
    elif cmd == "whoami":
        print("user\\desktop-pc234")
        return True
    elif cmd == "pwd":
        print(CURRENT_DIR)
        return True
    elif cmd == "echo":
        print(args)
        return True
    elif cmd == "exit" or cmd == "quit":
        return "EXIT"
    return False
