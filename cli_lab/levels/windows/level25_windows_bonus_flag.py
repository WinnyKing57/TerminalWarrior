import base64
import random
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
    title = "NIVEAU BONUS : DÉCRYPTAGE DE FLAG"
    objectives = [
        "Décoder le drapeau chiffré en deux couches (hexadécimal puis base64).",
        "Lire le drapeau en clair et le soumettre avec echo."
    ]
    hint = "Essayez : type <fichier>, puis certutil -decodehex"

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    done = set()

    test_flag = globals().get("_TEST_FLAG")
    test_names = globals().get("_TEST_NAMES")
    if test_flag and test_names:
        enc, b64, txt = test_names
        final_flag = test_flag
    else:
        num1 = random.randint(1000, 9999)
        num2 = random.randint(1000, 9999)
        enc = f"flag_{num1}_{num2}.enc"
        b64 = f"recovered_{num1}.b64"
        txt = "flag_clean.txt"
        final_flag = "TW_BONUS_WIN_" + "".join(random.choice("0123456789ABCDEF") for _ in range(8))

    layer_b64 = base64.b64encode(final_flag.encode()).decode()
    layer_hex = layer_b64.encode().hex()

    while True:
        try:
            user_input = input(build_prompt(CURRENT_DIR)).strip()
            parts = user_input.split()
            cmd = parts[0].lower() if parts else ""
            args = parts[1:]
            arg_str = " ".join(args)
            low = user_input.lower()

            if cmd == "echo":
                submitted = " ".join(args).strip()
                if submitted == final_flag:
                    print()
                    print(f"Flag valide : {final_flag}")
                    print("SUCCESS: Niveau BONUS terminé ! Réussite totale, le drapeau est capturé.")
                    if 6 not in done:
                        done.add(6)
                        time.sleep(1)
                        print_success("Niveau bonus terminé. FLAG=" + final_flag)
                        return True
                elif submitted.lower().startswith("tw_bonus"):
                    print("\nFlag incorrect, réessayez.")
                    print(f"Indice : lisez {txt} puis soumettez la valeur exacte.")
                else:
                    print(submitted)
                continue

            common = generic_cmd_handler(cmd, arg_str)
            if common == "EXIT":
                return False
            if common:
                continue

            if cmd in ["type", "cat"]:
                if enc in low:
                    print()
                    print(layer_hex)
                    print("\nUne longue chaîne hexadécimale : premières données chiffrées.")
                    if 1 not in done:
                        done.add(1)
                        print_objective_done(1)
                elif b64 in low:
                    print()
                    print(layer_b64)
                    print("\nLa base64 révèle la couche suivante du message.")
                    if 3 not in done:
                        done.add(3)
                        print_objective_done(3)
                elif txt in low:
                    print()
                    print(final_flag)
                    print("\nC'est le drapeau en clair ! Soumettez-le avec echo.")
                    if 5 not in done:
                        done.add(5)
                        print_objective_done(5)
                else:
                    print(f"'{user_input}' is not recognized.")
            elif cmd == "certutil":
                if "decodehex" in low and enc in low and b64 in low:
                    print()
                    print(f"Le fichier binaire '{b64}' a été créé à partir de l'hexadécimal.")
                    print("SUCCESS: hexadécimal décodé (couche base64).")
                    if 2 not in done:
                        done.add(2)
                        print_objective_done(2)
                elif "decode" in low and b64 in low and txt in low:
                    print()
                    print(f"Le fichier '{txt}' a été créé : contenu base64 déchiffré.")
                    print(f"SUCCESS: base64 décodée, le drapeau est dans {txt}.")
                    if 4 not in done:
                        done.add(4)
                        print_objective_done(4)
                else:
                    print("\nUsage: certutil -decodehex <entree> <sortie>  ou  certutil -decode <entree> <sortie>")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()