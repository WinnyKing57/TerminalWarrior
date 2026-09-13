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


EXPECTED_HOSTS = "A1B2C3D4E5F60718293A4B5C6D7E8F9A0B1C2D3E4F60718293A4B5C6D7E8F9A0"
ALTERED_HOSTS = "D1E2F3A4B5C60718293A4B5C6D7E8F9A0B1C2D3E4F60718293A4B5C6D7E8F9A0"


def run_level():
    title = "NIVEAU 21 : INTÉGRITÉ DES FICHIERS"
    objectives = [
        "Vérifier l'empreinte du fichier hosts avec certutil et PowerShell.",
        "Comparer avec l'empreinte officielle puis restaurer le fichier."
    ]
    Guide = [
        "certutil -hashfile C:\\Windows\\System32\\drivers\\etc\\hosts SHA256 — Calculer l'empreinte SHA256 actuelle du fichier hosts.",
        "type C:\\tools\\hosts.expected — Afficher l'empreinte officielle connue pour la comparer.",
        "fc /b C:\\Windows\\System32\\drivers\\etc\\hosts C:\\tools\\hosts.orig — Comparer les fichiers en binaire pour confirmer la modification.",
        "copy /y C:\\tools\\hosts.orig C:\\Windows\\System32\\drivers\\etc\\hosts — Restaurer le fichier hosts depuis la version originale.",
        "powershell \"Get-FileHash -Algorithm SHA256 -Path C:\\Windows\\System32\\drivers\\etc\\hosts\" — Recalculer l'empreinte pour vérifier la restauration.",
        "Si l'empreinte calculée ne correspond pas à hosts.expected, le fichier hosts a été altéré : restaurez-le.",
    ]
    hint = "Essayez : certutil -hashfile C:\\Windows\\System32\\drivers\\etc\\hosts SHA256"

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    done = set()
    restored = False

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

            if cmd == "certutil" and "hashfile" in low:
                print("\nSHA256 hash of C:\\Windows\\System32\\drivers\\etc\\hosts:")
                print(EXPECTED_HOSTS if restored else ALTERED_HOSTS)
                print("CertUtil: -hashfile command completed successfully.")
                if not restored:
                    print("\nCette empreinte ne correspond pas à l'empreinte officielle connue.")
                    if 1 not in done:
                        done.add(1)
                        print_objective_done(1)
                else:
                    print("\nL'empreinte correspond à la version officielle : fichier restauré.")
                    if 3 in done and 5 not in done:
                        done.add(5)
                        time.sleep(1)
                        print_success("Intégrité rétablie. Niveau 21 terminé. FLAG=TW_INTEGRITY_21")
                        return True
            elif cmd in ["powershell", "pwsh"] and "get-filehash" in low:
                print("\nAlgorithm       Hash                                                                 Path")
                print("---------       ----                                                                 ----")
                print(f"SHA256          {EXPECTED_HOSTS if restored else ALTERED_HOSTS}  C:\\Windows\\System32\\drivers\\etc\\hosts")
                if restored and 5 not in done:
                    done.add(5)
                    time.sleep(1)
                    print_success("Intégrité rétablie. Niveau 21 terminé. FLAG=TW_INTEGRITY_21")
                    return True
                elif not restored and 4 not in done:
                    done.add(4)
                    print("Vous avez terminé l'objectif 4 ! Comparez avec l'empreinte officielle, puis restaurez.\n")
                elif not restored and 1 not in done:
                    done.add(1)
                    print_objective_done(1)
            elif cmd in ["type", "cat"] and "hosts.expected" in low:
                print(EXPECTED_HOSTS)
                print("\nC'est l'empreinte officielle du fichier hosts. Comparez-la.")
                if 2 not in done:
                    done.add(2)
                    print("Vous avez terminé l'objectif 2 ! Comparez les fichiers avec fc /b.\n")
            elif cmd == "fc" and "hosts.orig" in low:
                print("\nComparaison des fichiers hosts et hosts.orig")
                print("***** CHAINE 1 (hosts)")
                print("127.0.0.1    localhost")
                print("***** CHAINE 2 (hosts.orig)")
                print("127.0.0.1    localhost")
                print("*****")
                print("\nLes fichiers diffèrent : hosts a été modifié (redirection DNS ajoutée) !")
                if 3 not in done:
                    done.add(3)
                    print("Vous avez terminé l'objectif 3 ! Restaurez le fichier avec copy /y.\n")
            elif cmd == "copy" and "hosts.orig" in low:
                restored = True
                print("\n     1 fichier(s) copié(s).")
                print("SUCCESS: hosts restauré depuis hosts.orig.")
                print("Vérifiez avec Get-FileHash pour confirmer l'empreinte officielle.")
                if 4 not in done:
                    done.add(4)
                    print("Vous avez terminé l'objectif 4 ! Vérifiez l'empreinte avec PowerShell.\n")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()