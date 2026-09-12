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


KEY = "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server"


def run_level():
    title = "NIVEAU 24 : DURCISSEMENT RDP"
    objectives = [
        "Constater que RDP est actif (reg query) et que le service écoute sur 3389.",
        "Désactiver RDP via la clé fDenyTSConnections et vérifier la configuration."
    ]
    hint = "Essayez : reg query \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server\" /v fDenyTSConnections"

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    done = set()
    rdp_disabled = False

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

            if cmd == "reg":
                if "query" in low and "fdeny" in low:
                    print("\nHKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server")
                    print("    fDenyTSConnections    REG_DWORD    0x%d" % (1 if rdp_disabled else 0))
                    if rdp_disabled:
                        print("\nRDP est désormais désactivé (1 interdit les connexions).")
                        if 4 in done and 5 not in done:
                            done.add(5)
                            time.sleep(1)
                            print_success("RDP désactivé. Niveau 24 terminé. FLAG=TW_RDP_HARDEN_24")
                            return True
                    else:
                        print("\nfDenyTSConnections=0 : les connexions RDP sont autorisées !")
                        print("\nVérifiez le service avec sc query TermService.")
                        if 1 not in done:
                            done.add(1)
                            print_objective_done(1)
                elif "add" in low and "fdeny" in low and ("/d 1" in low or "/d1" in low):
                    rdp_disabled = True
                    print("\nL'opération a réussi.")
                    print("SUCCESS: RDP désactivé (fDenyTSConnections=1).")
                    print("Vérifiez avec reg query ... /v fDenyTSConnections.")
                    if 4 not in done:
                        done.add(4)
                        print("Vous avez terminé l'objectif 4 ! Vérifiez la modification.\n")
                elif "query" in low and "fdeny" in low:
                    print("\nHKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server")
                    print("    fDenyTSConnections    REG_DWORD    0x%d" % (1 if rdp_disabled else 0))
                    if 1 not in done:
                        done.add(1)
                        print_objective_done(1)
                else:
                    print("\nUsage: reg query \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server\" /v fDenyTSConnections")
            elif cmd == "sc" and "query" in low and "termservice" in low:
                print("\nSERVICE_NAME: TermService")
                print("        TYPE               : 30  WIN32")
                print("        STATE              : 4  RUNNING")
                print("        START_TYPE         : 2   AUTO_START")
                print("\nTermService est RUNNING : le service RDP est actif !")
                if 2 not in done:
                    done.add(2)
                    print("Vous avez terminé l'objectif 2 ! Repérez le port 3389.\n")
            elif cmd == "netstat" and "findstr" in low and "3389" in low:
                print("\n  TCP    0.0.0.0:3389   0.0.0.0:0    LISTENING        654")
                print("\nLe port 3389 est ouvert : RDP est exposé !")
                if 3 not in done:
                    done.add(3)
                    print("Vous avez terminé l'objectif 3 ! Désactivez RDP avec reg add.\n")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()