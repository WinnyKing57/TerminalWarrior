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


TASKS_CONTENT = (
    "alpha: ok\n"
    "beta: ok\n"
    "gamma: FLAG=TW_POWERSHELL_10\n"
    "delta: ok\n"
)


def run_level():
    title = "NIVEAU 10 : DÉFI DE SCRIPTS POWERSHELL"
    objectives = [
        "Utiliser PowerShell pour filtrer le texte et extraire le drapeau.",
        "Automatiser la recherche au lieu de tout lire manuellement."
    ]
    Guide = [
        "dir — Listez le répertoire courant pour trouver le fichier de tâches.",
        "type tasks.txt — Affiche le contenu brut du fichier pour repérer les lignes.",
        "powershell -command \"Get-Content tasks.txt | Select-String FLAG\" — Filtre automatiquement les lignes contenant FLAG.",
        "Vous pouvez aussi utiliser Where-Object à la place de Select-String pour filtrer.",
        "Le drapeau se trouve dans la ligne contenant gamma du fichier tasks.txt.",
        "L'objectif est d'automatiser la recherche plutôt que de lire manuellement.",
    ]
    hint = "Essayez : powershell -command \"Get-Content tasks.txt | Select-String FLAG\""

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    while True:
        try:
            user_input = input(build_prompt(CURRENT_DIR)).strip()
            parts = user_input.split()
            cmd = parts[0].lower() if parts else ""
            args = parts[1:]
            arg_str = " ".join(args)

            common = generic_cmd_handler(cmd, arg_str, Guide)
            if common == "EXIT":
                return False
            if common:
                continue

            if cmd in ["dir", "ls"]:
                print(f"\n Directory of {CURRENT_DIR}\n")
                print("02/20/2026  12:05 PM               256 tasks.txt")
                print()
            elif cmd in ["type", "cat"]:
                if args and args[0].lower() == "tasks.txt":
                    print("\n[TASKS]")
                    print(TASKS_CONTENT)
                else:
                    print("The system cannot find the file specified.")
            elif cmd in ["powershell", "pwsh"]:
                lower = user_input.lower()
                if "tasks.txt" in lower and ("select-string" in lower or "where-object" in lower):
                    print("\nMatchInfo: gamma: FLAG=TW_POWERSHELL_10\n")
                    time.sleep(1)
                    print_success("Automatisation terminée. Niveau 10 terminé.")
                    return True
                else:
                    print("PowerShell: Command executed. No matches found.")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()
