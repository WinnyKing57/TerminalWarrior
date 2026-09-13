import time
from .utils import (
    print_header,
    print_objectives,
    print_success,
    generic_cmd_handler,
    CURRENT_DIR,
    print_windows_motd,
    build_prompt,
)


LOG_CONTENT = (
    "12:01:05 SYSTEM Starting service logon.\n"
    "12:01:10 ERROR Failed connection attempt from 10.0.0.1.\n"
    "12:01:15 SYSTEM Audit success for user guest.\n"
    "12:01:20 ALERT FLAG_KEY:HUNT3R_L0G_TRACER\n"
    "12:01:25 SYSTEM Service shutdown complete.\n"
)


def run_level():
    title = "NIVEAU 3 : RECHERCHE SUR LE SYSTÈME"
    objectives = [
        "Localiser le fichier journal d'audit suspect.",
        "Chercher le drapeau caché dans le journal."
    ]
    Guide = [
        "tree — visualisez l'arborescence et repérez le dossier Logs.",
        "dir — listez le dossier Logs : le fichier audit.log s'y trouve.",
        "where /r . audit.log — localisez le fichier audit.log depuis la racine du système.",
        "type audit.log — prévisualisez le journal et repérez la ligne ALERT suspecte.",
        "findstr FLAG audit.log — cherchez le drapeau marqué FLAG dans le journal d'audit.",
    ]
    hint = "Utilisez 'tree' pour visualiser les dossiers, 'where /r . audit.log' pour le localiser, et 'findstr FLAG audit.log'."

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    current_dir = CURRENT_DIR
    log_found = False

    while True:
        try:
            user_input = input(build_prompt(current_dir)).strip()
            parts = user_input.split()
            cmd = parts[0].lower() if parts else ""
            args = parts[1:]
            arg_str = " ".join(args)

            common = generic_cmd_handler(cmd, arg_str, Guide)
            if common == "EXIT":
                return False
            if common:
                continue

            if cmd == "tree":
                print(f"Folder PATH listing for volume OS")
                print(f"{CURRENT_DIR}")
                print("├── Intel")
                print("├── Logs")
                print("└── Public\n")
            elif cmd == "where":
                if "audit.log" in user_input.lower():
                    log_found = True
                    print(f"C:\\Users\\User\\Logs\\audit.log")
                else:
                    print("INFO: Could not find files for the given pattern(s).")
            elif cmd in ["dir", "ls"]:
                print(f" Directory of {CURRENT_DIR}\\Logs\n")
                print("02/20/2026  10:15 AM             1,200 audit.log")
                print()
            elif cmd in ["type", "cat"]:
                if "audit.log" in user_input.lower():
                    print("\n[LOG FILE PREVIEW]")
                    print("-" * 30)
                    print(LOG_CONTENT)
                    print("-" * 30)
                else:
                    print("The system cannot find the file specified.")
            elif cmd == "findstr":
                if "flag" in user_input.lower() and "audit.log" in user_input.lower():
                    print("\n[SEARCH RESULTS]")
                    print("12:01:20 ALERT FLAG_KEY:HUNT3R_L0G_TRACER")
                    time.sleep(1)
                    print_success("Drapeau trouvé dans les journaux. Niveau 3 terminé.")
                    return True
                else:
                    print("findstr: Search string or file name not specified.")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()
