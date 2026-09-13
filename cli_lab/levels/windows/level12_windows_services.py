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
    title = "NIVEAU 12 : SERVICES ET DÉMARRAGE"
    objectives = [
        "Inspecter le service pwnsvc qui écoute une porte dérobée.",
        "L'arrêter, le désactiver au démarrage, puis relancer le service SSH."
    ]
    Guide = [
        "sc query — Liste tous les services installés et leur état (running/stopped).",
        "sc query \"pwnsvc\" — Inspecte le service suspect : vérifiez son PID et son exécutable.",
        "sc stop \"pwnsvc\" — Arrête le service malveillant pwnsvc.",
        "sc config \"pwnsvc\" start= disabled — Désactive le démarrage automatique de pwnsvc.",
        "net start sshd — Relance le service SSH pour sécuriser l'accès distant.",
        "sc query OpenSSHd — Vérifie que le service SSH est bien en état RUNNING.",
        "Suivez l'ordre : inspecter → arrêter → désactiver → relancer SSH → vérifier.",
    ]
    hint = r"Essayez : sc query, puis sc stop \"pwnsvc\""

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    done = set()
    svc_pid = random.randint(3000, 3999)
    ssh_on = False

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

            if cmd == "sc":
                if "query" in low and "openssh" in low:
                    print("\nSERVICE_NAME: OpenSSHd")
                    print("        STATE              : 4 RUNNING")
                    print("\nLe service SSH est bien relancé.")
                    if 5 in done and 6 not in done:
                        done.add(6)
                        time.sleep(1)
                        print_success("Service SSH relancé. Niveau 12 terminé. FLAG=TW_SERVICES_12")
                        return True
                    elif 6 not in done:
                        print("Activez d'abord le service SSH avec net start sshd.")
                elif "query" in low and "pwnsvc" in low:
                    print(f"\nSERVICE_NAME: pwnsvc")
                    print("        TYPE               : 10  WIN32_OWN_PROCESS")
                    print("        STATE              : 4 RUNNING")
                    print(f"        PID                : {svc_pid}")
                    print("        EXECUTABLE PATH    : C:\\Tools\\nc.exe -l -p 4444")
                    print("\nCe service ouvre un shell sur le port 4444 : c'est une porte dérobée !")
                    if 2 not in done:
                        done.add(2)
                        print("Vous avez terminé l'objectif 2 ! Arrêtez-le avec sc stop \"pwnsvc\".\n")
                elif low.startswith("sc query"):
                    print("\nSERVICE_NAME: OpenSSHd")
                    print("        STATE              : 1 STOPPED")
                    print("SERVICE_NAME: pwnsvc")
                    print(f"        STATE              : 4 RUNNING          PID: {svc_pid}")
                    print("\nLe service pwnsvc est actif : il est suspect !")
                    if 1 not in done:
                        done.add(1)
                        print_objective_done(1)
                elif "config" in low and "pwnsvc" in low and "disabled" in low:
                    print("\n[SC] ChangeServiceConfig SUCCESS")
                    print("SUCCESS: pwnsvc ne démarrera plus automatiquement.")
                    if 4 not in done:
                        done.add(4)
                        print("Vous avez terminé l'objectif 4 ! Relancez le service SSH.\n")
                elif "stop" in low and "pwnsvc" in low:
                    print("\n[SC] ControlService SUCCESS")
                    print("SERVICE_NAME: pwnsvc")
                    print("        TYPE               : 10  WIN32_OWN_PROCESS")
                    print("        STATE              : 1 STOPPED")
                    print("\nSUCCESS: le service pwnsvc est arrêté.")
                    if 3 not in done:
                        done.add(3)
                        print("Vous avez terminé l'objectif 3 ! Désactivez-le au démarrage avec sc config \"pwnsvc\" start= disabled.\n")
                else:
                    print("Usage: sc query \"pwnsvc\" | sc stop \"pwnsvc\" | sc config \"pwnsvc\" start= disabled")
            elif cmd in ["net"] and "start" in low:
                if "sshd" in low or "ssh" in low:
                    print("\nThe OpenSSH Secure Shell Server service is starting.")
                    print("The OpenSSH Secure Shell Server service was started successfully.")
                    ssh_on = True
                    print("\nSUCCESS: le service SSH est à nouveau actif.")
                    if 5 not in done:
                        done.add(5)
                        print("Vous avez terminé l'objectif 5 ! Tapez sc query OpenSSHd pour vérifier.\n")
                else:
                    print("The service name is invalid.")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()