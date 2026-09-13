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
    title = "NIVEAU 14 : PARE-FEU WINDOWS DEFENDER"
    objectives = [
        "Activer le pare-feu et refuser le trafic entrant par défaut.",
        "Autoriser SSH (port 22), bloquer le port 8080 et vérifier les règles."
    ]
    Guide = [
        "netsh advfirewall show allprofiles state — Vérifie l'état actuel du pare-feu sur tous les profils.",
        "netsh advfirewall set allprofiles state on — Active le pare-feu sur tous les profils.",
        "netsh advfirewall set allprofiles firewallpolicy blockinbound,allowoutbound — Bloque le trafic entrant par défaut.",
        "netsh advfirewall firewall add rule name=SSH dir=in action=allow protocol=TCP localport=22 — Autorise SSH.",
        "netsh advfirewall firewall add rule name=Block8080 dir=in action=block protocol=TCP localport=8080 — Bloque le port 8080.",
        "netsh advfirewall firewall show rule name=all — Vérifie toutes les règles configurées.",
        "Suivez l'ordre : vérifier état → activer → politique → règle SSH → règle 8080 → vérifier.",
    ]
    hint = "Essayez : netsh advfirewall show allprofiles state"

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    done = set()
    fw_on = False

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

            if cmd == "netsh":
                if "show allprofiles state" in low:
                    if not fw_on:
                        print("\nProfile  : Domain Profile")
                        print("State    : OFF")
                        print("\\nProfile  : Private Profile")
                        print("State    : OFF")
                        print("\\nProfile  : Public Profile")
                        print("State    : OFF")
                        print("\nLe pare-feu est désactivé sur tous les profils.")
                        if 1 not in done:
                            done.add(1)
                            print("Vous avez terminé l'objectif 1 ! Activez-le : netsh advfirewall set allprofiles state on\n")
                    else:
                        print("\nProfile  : Domain Profile")
                        print("State    : ON")
                        print("\\nProfile  : Private Profile")
                        print("State    : ON")
                        print("\\nProfile  : Public Profile")
                        print("State    : ON")
                        if 2 in done and 6 not in done:
                            print("\nL'état du pare-feu est correct.")
                elif "set allprofiles state on" in low:
                    print("\nOk.")
                    print("SUCCESS: Le pare-feu est maintenant actif sur tous les profils.")
                    fw_on = True
                    if 2 not in done:
                        done.add(2)
                        print("Vous avez terminé l'objectif 2 ! Appliquez la politique par défaut : deny inbound, allow outbound.\n")
                elif "set allprofiles firewallpolicy" in low:
                    print("\nOk.")
                    print("SUCCESS: Inbound par défaut refusé, outbound autorisé.")
                    if 3 not in done:
                        done.add(3)
                        print("Vous avez terminé l'objectif 3 ! Autorisez le port 22 avec netsh advfirewall firewall add rule.\n")
                elif "add rule" in low and "localport=22" in low.replace(" ", ""):
                    print("\nOk.")
                    print("SUCCESS: Règle d'entrée 'SSH Allowed' créée pour le port 22.")
                    if 4 not in done:
                        done.add(4)
                        print("Vous avez terminé l'objectif 4 ! Blaquez le port 8080 avec une règle de blocage.\n")
                elif "add rule" in low and "localport=8080" in low.replace(" ", ""):
                    print("\nOk.")
                    print("SUCCESS: Règle de blocage créée pour le port 8080.")
                    if 5 not in done:
                        done.add(5)
                        print("Vous avez terminé l'objectif 5 ! Vérifiez avec netsh advfirewall firewall show rule.\n")
                elif "show rule" in low:
                    print("\nRule Name:                            Action  Enabled")
                    print("------------------------------------  ------  -------")
                    print("SSH Allowed                            Allow   Yes")
                    print("Block 8080                             Block   Yes")
                    print("\nLe pare-feu est actif et la configuration est correcte.")
                    if 5 in done and 1 in done and 6 not in done:
                        done.add(6)
                        time.sleep(1)
                        print_success("Pare-feu configuré. Niveau 14 terminé. FLAG=TW_FIREWALL_14")
                        return True
                    elif 6 not in done:
                        print("Terminez d'abord la configuration (état ON, politique, règles).")
                else:
                    print("ERR: Commande netsh advfirewall non reconnue.")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()