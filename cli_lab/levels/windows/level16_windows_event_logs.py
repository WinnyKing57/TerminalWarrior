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
    title = "NIVEAU 16 : JOURNAUX D'ÉVÉNEMENTS"
    objectives = [
        "Retracer la tentative de connexion forcée dans le journal Security.",
        "Prouver l'attaque en retrouvant la ligne de preuve dans les événements."
    ]
    hint = "Essayez : wevtutil qe Security \"*[System/EventID=4625]\" /c:10"

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    done = set()
    attacker = f"{random.randint(101, 250)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"

    while True:
        try:
            user_input = input(build_prompt(CURRENT_DIR)).strip()
            parts = user_input.split()
            cmd = parts[0].lower() if parts else ""
            args = parts[1:]
            arg_str = " ".join(args)
            low = user_input.lower()

            common = generic_cmd_handler(cmd, arg_str)
            if common == "EXIT":
                return False
            if common:
                continue

            if cmd == "wevtutil":
                if low.startswith("wevtutil el"):
                    print("\nApplication")
                    print("Security")
                    print("Setup")
                    print("System")
                    print("Windows PowerShell")
                    if 1 not in done:
                        done.add(1)
                        print_objective_done(1)
                elif low.startswith("wevtutil gl"):
                    print("\nname: Security")
                    print("enabled: true")
                    print("type: Admin")
                    print("logFilePath: %SystemRoot%\\System32\\winevt\\Logs\\Security.evtx")
                    if 1 not in done:
                        done.add(1)
                        print_objective_done(1)
                elif "4625" in low and "qe" in low:
                    print("\nEvent[0]:")
                    print(f"  Event ID: 4625")
                    print(f"  Computer: WS-OPS-01")
                    print("  TimeCreated: 2025-10-03T03:42:11.000Z")
                    print("  Failed Logon:  Logon Type: 3  (Network)")
                    print(f"  Source Network Address: {attacker}")
                    print("  Account Name: Administrator")
                    print("\nPlusieurs échecs de connexion depuis la même adresse : attaque par force brute !")
                    if 3 not in done:
                        done.add(3)
                        print("Vous avez terminé l'objectif 3 ! Consultez les rejets de sécurité (Event ID 4625) avec PowerShell.\n")
                elif "qe" in low and "system" in low:
                    print("\nEvent[0]:   Event ID: 7040")
                    print("  Provider: Service Control Manager")
                    print("  TimeCreated: 2025-10-03T03:40:12.000Z")
                    print("  A service was installed on the system:  name: pwnsvc")
                    if 2 not in done:
                        done.add(2)
                        print("Vous avez terminé l'objectif 2 ! Filtrez les échecs de connexion (Event ID 4625).\n")
                elif "qe" in low and "security" in low:
                    print("\nEvent[0]:   Event ID: 4624")
                    print("  Logon Type: 3 (Network) - Account: user")
                    print("Event[1]:   Event ID: 4625")
                    print(f"  Failed Logon - Source: {attacker} - Account: root")
                    print("Event[2]:   Event ID: 4625")
                    print(f"  Failed Logon - Source: {attacker} - Account: admin")
                    print("\nDes échecs de connexion par bruteforce sont enregistrés dans le journal Security.")
                    if 3 not in done:
                        done.add(3)
                        print("Vous avez terminé l'objectif 3 ! Filtrez l'Event ID 4625.\n")
                else:
                    print("Utilisez wevtutil el puis wevtutil qe <journal>.")
            elif cmd in ["powershell", "pwsh"]:
                wants_final = "format-list" in low or "select-object" in low or "where" in low
                if wants_final and "security" in low:
                    print("\nEvent[0]:   Event ID: 4625")
                    print(f"  Source Network Address: {attacker}")
                    print("  Message: An account failed to log on.")
                    print("  The machine routes the world via a secret tunnel - preuve de compromission !")
                    print("\nLa trace de l'attaque est confirmée, la ligne de preuve est dans le journal.")
                    if 4 in done and 5 not in done:
                        done.add(5)
                        time.sleep(1)
                        print_success("Attaque retracée. Niveau 16 terminé. FLAG=TW_EVENTLOGS_16")
                        return True
                    elif 5 not in done:
                        print("Filtrez d'abord les échecs de connexion (Event ID 4625).")
                elif "4625" in low:
                    print("\nTimeCreated                Id   Message")
                    print("--------                  --   -------")
                    print(f"10/03/2025 03:42:11     4625  An account failed to log on. Source: {attacker}")
                    print(f"10/03/2025 03:41:55     4625  An account failed to log on. Source: {attacker}")
                    print(f"10/03/2025 03:41:40     4625  An account failed to log on. Source: {attacker}")
                    if 4 not in done:
                        done.add(4)
                        print("Vous avez terminé l'objectif 4 ! Lisez le rejet complet du journal Security.\n")
                else:
                    print("PowerShell: aucun événement ne correspond.")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()