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
    title = "NIVEAU 22 : JONCTIONS ET DISQUES"
    objectives = [
        "Repérer la jonction notes_link qui pointe vers un fichier système critique.",
        "La remplacer par une jonction légitime vers le dossier de notes."
    ]
    Guide = [
        "dir — Lister le répertoire pour repérer la jonction notes_link.",
        "fsutil reparsepoint query notes_link — Inspecter la cible de la jonction : elle pointe vers C:\\Windows\\System32\\config\\SAM, c'est dangereux.",
        "wmic logicaldisk get — Lister les disques et volumes disponibles pour comprendre le système.",
        "rmdir notes_link — Supprimer la jonction malveillante (la cible n'est pas affectée).",
        "mklink /D notes_link C:\\Users\\User\\real_notes — Créer une jonction de répertoire légitime vers le dossier de notes.",
        "dir — Vérifier que notes_link pointe désormais vers real_notes.",
        "Une jonction Windows redirige un chemin vers un autre emplacement sans copier les fichiers.",
    ]
    hint = r"Essayez : dir, puis fsutil reparsepoint query notes_link"

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    done = set()
    junction_fixed = False

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
                print(f"\n Volume in drive C has no label.\n Volume Serial Number is 9C33-62FF\n")
                print(f" Directory of {CURRENT_DIR}\n")
                print("10/10/2025  09:00 AM    <DIR>          real_notes")
                if junction_fixed:
                    print("10/10/2025  09:05 AM    <JUNCTION>     notes_link [C:\\Users\\User\\real_notes]")
                    print("\nLa jonction pointe maintenant vers le dossier légitime.")
                    if 4 in done and 5 not in done:
                        done.add(5)
                        time.sleep(1)
                        print_success("Jonction corrigée. Niveau 22 terminé. FLAG=TW_JUNCTIONS_22")
                        return True
                else:
                    print("10/10/2025  09:05 AM    <JUNCTION>     notes_link [C:\\Windows\\System32\\config\\SAM]")
                    print("\nnotes_link pointe vers le fichier SAM (mots de passe) : jonction malveillante !")
                if 1 not in done:
                    done.add(1)
                    print_objective_done(1)
            elif cmd == "fsutil" and "reparsepoint" in low and "notes_link" in low:
                if junction_fixed:
                    print("\n   Print Name Length: 35")
                    print("   Substitute Name Offset: 84")
                    print("   Substitute Name Length: 44")
                    print("   Print Name: C:\\Users\\User\\real_notes")
                    print("\nLa jonction pointe vers le dossier de notes légitime.")
                else:
                    print("\n   Print Name Length: 44")
                    print("   Substitute Name Offset: 84")
                    print("   Substitute Name Length: 55")
                    print("   Print Name: C:\\Windows\\System32\\config\\SAM")
                    print("\nLa jonction expose le registre SAM : c'est dangereux !")
                    if 2 not in done:
                        done.add(2)
                        print("Vous avez terminé l'objectif 2 ! Consultez les disques avec wmic logicaldisk.\n")
            elif cmd == "wmic" and "logicaldisk" in low:
                print("DeviceID FileSystem VolumeName      Size          FreeSpace")
                print("C:      NTFS       System          127504568320   81234821324")
                print("D:      NTFS       Data            53687091200    40000000000")
                if 3 not in done:
                    done.add(3)
                    print("Vous avez terminé l'objectif 3 ! Supprimez la jonction avec rmdir.\n")
            elif cmd == "rmdir" and "notes_link" in low:
                junction_fixed = True
                print("\nLa jonction notes_link a été supprimée (la cible n'est pas affectée).")
                print("SUCCESS: créez une jonction propre avec mklink /D.")
                if 4 not in done:
                    done.add(4)
                    print("Vous avez terminé l'objectif 4 ! Créez la jonction correcte.\n")
            elif cmd == "mklink" and "notes_link" in low:
                junction_fixed = True
                print("\n    junction created for notes_link <<===>> C:\\Users\\User\\real_notes")
                print("SUCCESS: jonction correcte créée.")
                print("Vérifiez avec fsutil reparsepoint query notes_link.")
                if 4 not in done:
                    done.add(4)
                    print("Vous avez terminé l'objectif 4 ! Vérifiez la cible.\n")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()