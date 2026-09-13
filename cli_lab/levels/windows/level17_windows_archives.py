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
    title = "NIVEAU 17 : ARCHIVAGE ET EXTRACTION"
    objectives = [
        "Identifier une archive suspecte et l'extraire.",
        "Décompresser le journal et lire la trace cachée dans l'archive."
    ]
    Guide = [
        "dir — Lister les fichiers du répertoire pour repérer backup.zip et data.log.gz.",
        "powershell \"Expand-Archive -Path backup.zip -DestinationPath .\" — Extraire le contenu de l'archive ZIP dans le répertoire courant.",
        "tar -xzf data.log.gz — Décompresser le journal.gz pour obtenir le fichier data.log.",
        "type extracted_flag.txt — Lire le drapeau extrait ; cette commande doit être exécutée après avoir décompressé data.log.gz.",
        "L'ordre compte : extrayez d'abord backup.zip, puis décompressez data.log.gz avant de lire le flag.",
    ]
    hint = r"Essayez : powershell \"Expand-Archive -Path backup.zip -DestinationPath .\""

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    done = set()
    extracted = False

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

            if cmd in ["dir", "ls"]:
                print(f"\n Directory of {CURRENT_DIR}\n")
                print("10/02/2025  10:14 PM         2,310,861 backup.zip")
                print("10/02/2025  10:15 PM             4,502 data.log.gz")
                if not extracted:
                    print("\nbackup.zip et data.log.gz : aucune trace de fichiers extraits pour l'instant.")
                    print("Extrayez backup.zip avec PowerShell (Expand-Archive).")
                    if 1 not in done:
                        done.add(1)
                        print_objective_done(1)
                else:
                    print("10/02/2025  10:15 PM               412 extracted_flag.txt")
                    print("10/02/2025  10:15 PM            22,904 stolen_data.db")
                    print("10/02/2025  10:15 PM             1,208 notes.txt")
                    print("10/02/2025  10:15 PM               310 data.log")
                    print("\nLes fichiers ont bien été extraits dans le répertoire courant.")
                    if 3 not in done:
                        done.add(3)
                        print("Vous avez terminé l'objectif 3 ! Décompressez data.log.gz avec tar.\n")
            elif cmd in ["powershell", "pwsh"] and "expand-archive" in low:
                print("\n    Récupération de : C:\\backup.zip")
                print("    Destination      : C:\\Users\\User")
                print("\n    Extraction de : backup.zip")
                print("    OK  - backup\\stolen_data.db")
                print("    OK  - backup\\notes.txt")
                print("    OK  - backup\\extracted_flag.txt")
                print("    OK  - backup\\data.log.gz")
                print("    OK  - backup\\")
                extracted = True
                if 2 not in done:
                    done.add(2)
                    print("Vous avez terminé l'objectif 2 ! Faites un dir pour voir les fichiers extraits.\n")
            elif cmd == "tar" and "xzf" in low and "data.log.gz" in low:
                print("\nLe fichier data.log.gz a été décompressé en data.log.")
                if 4 not in done:
                    done.add(4)
                    print("Vous avez terminé l'objectif 4 ! Lisez extracted_flag.txt avec type.\n")
            elif cmd in ["type", "cat"] and "extracted_flag.txt" in low:
                print("\nExfiltration vers 185.220.101.4 — c'est la preuve de l'attaque !")
                if 4 in done and 5 not in done:
                    done.add(5)
                    time.sleep(1)
                    print_success("Traces extraites. Niveau 17 terminé. FLAG=TW_ARCHIVES_17")
                    return True
                elif 5 not in done:
                    print("Décompressez d'abord data.log.gz avec tar -xzf.")
            elif cmd in ["type", "cat"] and "data.log" in low:
                print("\nOct 02 21:58:12 backup: dump du fichier C:\\inetpub\\wwwroot\\app\\web.config OK")
                print("Oct 02 22:14:02 backup: compression de backup.zip OK")
            elif cmd == "tar" and "t" in low and "backup.zip" in low:
                print("\nbackup/stolen_data.db")
                print("backup/notes.txt")
                print("backup/extracted_flag.txt")
                print("backup/data.log.gz")
                if 2 not in done and 1 in done:
                    print("Vous avez terminé l'objectif 2 ! Extrayez avec Expand-Archive.\n")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()