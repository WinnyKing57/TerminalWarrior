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
    title = "NIVEAU 15 : UTILISATEURS ET GROUPES"
    objectives = [
        "Nettoyer les comptes locaux et repérer l'intrus 'invader'.",
        "Créer l'agent 'agent' dans le groupe Administrators, puis supprimer 'invader'."
    ]
    hint = "Essayez : net user, puis net user invader"

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    done = set()

    while True:
        try:
            user_input = input(build_prompt(CURRENT_DIR)).strip()
            parts = user_input.split()
            cmd = parts[0].lower() if parts else ""
            args = parts[1:]
            arg_str = " ".join(args)
            low = user_input.lower()

            if cmd == "whoami":
                print("user\\desktop-pc234")
                if 1 not in done:
                    done.add(1)
                    print_objective_done(1)
                continue

            common = generic_cmd_handler(cmd, arg_str)
            if common == "EXIT":
                return False
            if common:
                continue

            if cmd == "net":
                if low.startswith("net user") and len(args) <= 2:
                    if "invader" in low:
                        print("\nUser name                    invader")
                        print("Full Name")
                        print("Comment")
                        print("User's comment")
                        print("Country/Region code          000 (System Default)")
                        print("Account active               Yes")
                        print("Account expires              Never")
                        print("Password last set            10/02/2025 3:14:42 AM")
                        print("Password expires             Never")
                        print("User may change password     Yes")
                        print("Logon script")
                        print("User profile")
                        print("Home directory")
                        print("Last logon                  10/02/2025 4:05:11 AM")
                        print("Logon hours allowed         All")
                        print("\nCe compte a été créé récemment et connecté de nuit : c'est l'intrus !")
                        if 3 not in done:
                            done.add(3)
                            print("Vous avez terminé l'objectif 3 ! Créez le groupe Operations.\n")
                    else:
                        print("\nUser accounts for \\\\WS-OPS-01")
                        print("-" * 40)
                        print("Administrator            DefaultAccount")
                        print("Guest                    invader")
                        print("user                     WDAGUtilityAccount")
                        print("\nLe compte 'invader' ne fait pas partie des comptes légitimes.")
                        if 2 not in done:
                            done.add(2)
                            print("Vous avez terminé l'objectif 2 ! Inspectez-le : net user invader\n")
                elif "localgroup operations /add" in low:
                    print("\nThe command completed successfully.")
                    print("SUCCESS: le groupe Operations a été créé.")
                    if 4 not in done:
                        done.add(4)
                        print("Vous avez terminé l'objectif 4 ! Créez l'utilisateur agent.\n")
                elif "user agent /add" in low:
                    print("\nThe command completed successfully.")
                    print("SUCCESS: l'utilisateur agent a été créé.")
                    if 5 not in done:
                        done.add(5)
                        print("Vous avez terminé l'objectif 5 ! Ajoutez agent au groupe Administrators.\n")
                elif "localgroup administrators agent /add" in low:
                    print("\nThe command completed successfully.")
                    print("SUCCESS: agent a été ajouté au groupe Administrators.")
                    if 6 not in done:
                        done.add(6)
                        print("Vous avez terminé l'objectif 6 ! Supprimez le compte intrus.\n")
                elif "user invader /delete" in low:
                    print("\nThe command completed successfully.")
                    print("SUCCESS: le compte invader a été supprimé.")
                    print("\nSUCCESS: Tous les comptes locaux sont maintenant propres.")
                    if 6 in done and 7 not in done:
                        done.add(7)
                        time.sleep(1)
                        print_success("Comptes nettoyés. Niveau 15 terminé. FLAG=TW_USERS_15")
                        return True
                    elif 7 not in done:
                        print("Supprimez d'abord l'intrus après avoir créé agent.")
                else:
                    print("NET: la commande n'a pas été reconnue.")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()