import random
import time
from .utils import (
    print_header,
    print_objectives,
    print_success,
    print_objective_done,
    generic_cmd_handler,
    CURRENT_DIR,
    print_windows_motd,
    build_prompt,
)


def run_level():
    title = "NIVEAU 20 : PORTS ET SERVICES RÉSEAU"
    objectives = [
        "Trouver le service inconnu en écoute sur le port 31337.",
        "Identifier le processus (nc.exe), l'interroger, puis l'arrêter."
    ]
    Guide = [
        "netstat -ano — Lister toutes les connexions et ports en écoute pour repérer le port 31337.",
        "netstat -ano | findstr 31337 — Filtrer les résultats pour isoler le PID du processus écoutant sur 31337.",
        "tasklist /fi \"PID eq <PID>\" — Identifier le processus associé au PID trouvé : il s'agit de nc.exe.",
        "curl http://localhost:31337 — Sonder le service suspect pour confirmer qu'il propose un shell distant (backdoor).",
        "taskkill /pid <PID> /f — Terminer de force le processus malveillant.",
        "netstat -ano | findstr 31337 — Vérifier que le port 31337 est désormais fermé.",
        "Remplacez <PID> par la valeur affichée par netstat dans ce niveau ; le fichier guidé par tests utilise 3141.",
    ]
    hint = "Essayez : netstat -ano, puis netstat -ano | findstr 31337"

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    done = set()
    evil_pid = random.randint(3000, 4999)
    web_pid = random.randint(500, 999)
    http_pid = random.randint(1000, 1999)
    listener_alive = True

    while True:
        try:
            user_input = input(build_prompt(CURRENT_DIR)).strip()
            parts = user_input.split()
            cmd = parts[0].lower() if parts else ""
            args = parts[1:]
            arg_str = " ".join(args)
            low = user_input.lower()

            common = generic_cmd_handler(cmd, arg_str, Guide)
            if common == "EXIT":
                return False
            if common:
                continue

            if cmd == "netstat":
                if "findstr" in low and "31337" in low:
                    if not listener_alive:
                        print("\n")
                        print("\nAucune ligne ne mentionne le port 31337 : le service est arrêté.")
                        if 6 not in done:
                            done.add(6)
                            time.sleep(1)
                            print_success("Port fermé pour de bon. Niveau 20 terminé. FLAG=TW_PORTS_20")
                            return True
                    else:
                        print("\n  TCP    0.0.0.0:31337   0.0.0.0:0    LISTENING        %d" % evil_pid)
                        print("\nLe PID %d écoute sur 31337 : service suspect !" % evil_pid)
                        if 2 not in done:
                            done.add(2)
                            print("Vous avez terminé l'objectif 2 ! Identifiez ce processus avec tasklist.\n")
                elif "listening" in low:
                    print("\n  Proto  Local Address          Foreign Address        State          PID")
                    print("  TCP    0.0.0.0:22             0.0.0.0:0              LISTENING      %d" % web_pid)
                    print("  TCP    0.0.0.0:80             0.0.0.0:0              LISTENING      %d" % http_pid)
                    if listener_alive:
                        print("  TCP    0.0.0.0:31337          0.0.0.0:0              LISTENING      %d" % evil_pid)
                    print("\nLe port 31337 est en écoute : service inconnu !")
                    if 1 not in done:
                        done.add(1)
                        print_objective_done(1)
                else:
                    print("\n  Proto  Local Address          Foreign Address        State          PID")
                    print("  TCP    0.0.0.0:22             0.0.0.0:0              LISTENING      %d" % web_pid)
                    print("  TCP    0.0.0.0:80             0.0.0.0:0              LISTENING      %d" % http_pid)
                    if listener_alive:
                        print("  TCP    0.0.0.0:31337          0.0.0.0:0              LISTENING      %d" % evil_pid)
                    print("\nLe port 31337 est en écoute : identifiez le processus.")
                    if 1 not in done:
                        done.add(1)
                        print_objective_done(1)
            elif cmd == "tasklist":
                if "312" in low or "min" in low:
                    print("\nImage Name                    PID     Session Name        Session#    Mem Usage")
                    print("==========================  ======  ================  ==========  ============")
                    print(f"nc.exe                         {evil_pid}    Console                 1     4,120 K")
                    if 3 not in done:
                        done.add(3)
                        print("Vous avez terminé l'objectif 3 ! Interrogez le service avec curl.\n")
                elif "eq" in low and "pid" in low:
                    print("\nImage Name                    PID     Session Name        Session#    Mem Usage")
                    print("==========================  ======  ================  ==========  ============")
                    print(f"nc.exe                         {evil_pid}    Console                 1     4,120 K")
                    if 3 not in done:
                        done.add(3)
                        print("Vous avez terminé l'objectif 3 ! Interrogez le service avec curl.\n")
                else:
                    print("\nImage Name                    PID     Session Name        Session#    Mem Usage")
                    print("==========================  ======  ================  ==========  ============")
                    print("svchost.exe                   %d    Services              0        22,400 K" % web_pid)
                    print("System Idle Process             4    Services              0         8 K")
                    print(f"nc.exe                         {evil_pid}    Console                 1     4,120 K")
                    if 3 not in done:
                        done.add(3)
                        print("Vous avez terminé l'objectif 3 ! Interrogez le service avec curl.\n")
            elif cmd == "curl" and "31337" in low:
                if listener_alive:
                    print("\nBienvenue sur le service 31337.")
                    print("Tapez 'shell' pour obtenir un shell...")
                    print("\nCe service propose un shell distant : c'est une backdoor !")
                else:
                    print("\ncurl: (7) Failed to connect to localhost port 31337: Connection refused")
                if 4 not in done:
                    done.add(4)
                    print("Vous avez terminé l'objectif 4 ! Arrêtez le processus avec taskkill.\n")
            elif cmd == "taskkill":
                target = None
                for arg in args:
                    if arg.lower().startswith("/pid"):
                        continue
                    if arg.lower().startswith("/f"):
                        continue
                    if arg.lower().startswith("/t"):
                        continue
                    if arg.isdigit():
                        target = int(arg)
                if target == evil_pid:
                    print(f"SUCCESS: Terminated the process with PID {target}.")
                    listener_alive = False
                    print("\nPort 31337 libéré. Vérifiez avec netstat -ano | findstr 31337.")
                    if 5 not in done:
                        done.add(5)
                        print("Vous avez terminé l'objectif 5 ! Vérifiez que le port est fermé.\n")
                elif target is not None:
                    print(f"ERROR: The process with PID {target} could not be terminated.")
                else:
                    print("Usage: taskkill /pid <PID> /f")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()