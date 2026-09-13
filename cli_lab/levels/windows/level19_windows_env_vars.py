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
    title = "NIVEAU 19 : VARIABLES D'ENVIRONNEMENT"
    objectives = [
        "Repérer le PATH détourné et la variable MALVAR ajoutée par l'attaquant.",
        "Réparer le PATH et purger la variable malveillante."
    ]
    Guide = [
        "set — Afficher toutes les variables d'environnement pour repérer le PATH suspect et la variable MALVAR.",
        "echo %PATH% — Vérifier le PATH : un dossier non système (Temp, Tools) en tête est un signe de détournement.",
        "echo %MALVAR% — Vérifier la variable malveillante qui pointe vers C:\\Tools\\evil.dll.",
        "set PATH=%SystemRoot%\\system32;%SystemRoot% — Réparer le PATH en ne gardant que les chemins système légitimes.",
        "set MALVAR= — Vider la variable MALVAR pour supprimer la référence à la DLL malveillante.",
        "set — Vérifier que le PATH est réparé et que MALVAR est vide.",
        "Le PATH hijacking place le dossier de l'attaquant devant les chemins système pour exécuter une fausse commande.",
    ]
    hint = "Essayez : set, puis echo %PATH%"

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    done = set()
    path_fixed = False
    malvar_cleared = False

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
                target = user_input[4:].strip().lower() if len(user_input) > 4 else ""
                if target.startswith("%path%"):
                    print("%SystemRoot%\\system32;%SystemRoot%\\Tools;%SystemRoot%\\Temp;%SystemRoot%" if not path_fixed else "%SystemRoot%\\system32;%SystemRoot%;%SystemRoot%\\System32\\Wbem")
                    if not path_fixed:
                        print("\nEnvPath %SystemRoot%\\Temp est en tête du PATH : un dossier inattendu !")
                        if 2 not in done:
                            done.add(2)
                            print_objective_done(2)
                elif target.startswith("%malvar%"):
                    print("C:\\Tools\\evil.dll" if not malvar_cleared else "")
                    if not malvar_cleared:
                        print("\nMALVAR charge une DLL depuis C:\\Tools : code malveillant !")
                        if 3 not in done:
                            done.add(3)
                            print("Vous avez terminé l'objectif 3 ! Videz-la avec set MALVAR=.\n")
                else:
                    print(args)
            elif cmd == "set":
                if "path=" in low and "%systemroot%" in low:
                    path_fixed = True
                    print("PATH=%SystemRoot%\\system32;%SystemRoot%")
                    print("SUCCESS: le PATH ne pointe plus vers Temp ou Tools.")
                    if 4 not in done:
                        done.add(4)
                        print("Vous avez terminé l'objectif 4 ! Videz MALVAR avec set MALVAR=.\n")
                elif low.startswith("set malvar"):
                    malvar_cleared = True
                    print("MALVAR=")
                    print("SUCCESS: la variable MALVAR a été vidée.")
                    if 5 not in done:
                        done.add(5)
                        print("Vous avez terminé l'objectif 5 ! Vérifiez avec set.\n")
                else:
                    print("PATH=%SystemRoot%\\system32;%SystemRoot%\\Tools;%SystemRoot%\\Temp;%SystemRoot%" if not path_fixed else "PATH=%SystemRoot%\\system32;%SystemRoot%")
                    print("TEMP=C:\\Users\\User\\AppData\\Local\\Temp")
                    if malvar_cleared:
                        print("MALVAR=")
                    else:
                        print("MALVAR=C:\\Tools\\evil.dll")
                    if not path_fixed:
                        print("\nMALVAR pointe vers C:\\Tools\\evil.dll et PATH contient Temp : compromission !")
                        if 1 not in done:
                            done.add(1)
                            print_objective_done(1)
                    else:
                        print("\nL'environnement est propre : plus de variable malveillante.")
                        if 4 in done and 5 in done and 6 not in done:
                            done.add(6)
                            time.sleep(1)
                            print_success("Environnement réparé. Niveau 19 terminé. FLAG=TW_ENVVARS_19")
                            return True
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()