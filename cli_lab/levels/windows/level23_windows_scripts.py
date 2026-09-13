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
    title = "NIVEAU 23 : SCRIPTS BATCH ET POWERSHELL"
    objectives = [
        "Créer un script batch cleanup.bat qui supprime les fichiers malveillants.",
        "Le localiser, puis l'exécuter pour nettoyer C:\\Temp."
    ]
    Guide = [
        "echo @echo off > cleanup.bat — Créer le script batch avec l'en-tête @echo off.",
        "echo del /f /q C:\\Temp\\malware.exe >> cleanup.bat — Ajouter la ligne de suppression du malware à la fin du script.",
        "type cleanup.bat — Vérifier le contenu du script avant de l'exécuter.",
        "where cleanup.bat — Localiser le script dans le système de fichiers.",
        "cleanup.bat — Exécuter le script pour purger les fichiers malveillants.",
        "L'opérateur > crée un fichier en l'écrasant ; >> ajoute une ligne à la fin d'un fichier existant.",
    ]
    hint = "Essayez : echo @echo off > cleanup.bat"

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    done = set()
    script_ready = False

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

            if cmd == "echo":
                if "cleanup.bat" in low and ">" in low:
                    if "@echo off" in low:
                        script_ready = True
                        print("\ncleanup.bat créé avec l'en-tête @echo off.")
                        if 1 not in done:
                            done.add(1)
                            print("Vous avez terminé l'objectif 1 ! Ajoutez la commande de suppression.\n")
                    elif "del" in low and "malware" in low:
                        script_ready = True
                        print("\nLigne de suppression ajoutée à cleanup.bat.")
                        if 2 not in done:
                            done.add(2)
                            print("Vous avez terminé l'objectif 2 ! Inspectez le script avec type.\n")
                else:
                    print(args)
            elif cmd in ["type", "cat"] and "cleanup.bat" in low:
                print("\n@echo off")
                print("echo Suppression des fichiers malveillants...")
                print("del /f /q C:\\Temp\\malware.exe")
                print("del /f /q C:\\Temp\\beacon.ps1")
                print("echo Nettoyage terminé")
                if 3 not in done:
                    done.add(3)
                    print("Vous avez terminé l'objectif 3 ! Localisez le script avec where.\n")
            elif cmd == "where" and "cleanup.bat" in low:
                print("\nC:\\Users\\User\\cleanup.bat")
                if 4 not in done:
                    done.add(4)
                    print("Vous avez terminé l'objectif 4 ! Exécutez le script.\n")
            elif cmd == "cleanup.bat" or command.strip().lower() == "cleanup.bat":
                script_ready = True
                print("\nC:\\Users\\User>cleanup.bat")
                print("Suppression des fichiers malveillants...")
                print("C:\\Temp\\malware.exe supprimé.")
                print("C:\\Temp\\beacon.ps1 supprimé.")
                print("Nettoyage terminé")
                print("\nSUCCESS: Les fichiers malveillants ont été purgés.")
                if 4 in done and 5 not in done:
                    done.add(5)
                    time.sleep(1)
                    print_success("Nettoyage effectué. Niveau 23 terminé. FLAG=TW_SCRIPTS_23")
                    return True
                elif 5 not in done:
                    print("Localisez d'abord le script avec where cleanup.bat.")
            elif cmd in ["powershell", "pwsh"] and "cleanup" in low:
                print("\nRemove-Item C:\\Temp\\malware.exe, C:\\Temp\\beacon.ps1 -Force")
                print("Nettoyage terminé via PowerShell.")
                if 4 in done and 5 not in done:
                    done.add(5)
                    time.sleep(1)
                    print_success("Nettoyage effectué. Niveau 23 terminé. FLAG=TW_SCRIPTS_23")
                    return True
                elif 5 not in done:
                    print("Localisez d'abord le script avec where cleanup.bat.")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()