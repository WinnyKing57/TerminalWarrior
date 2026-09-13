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
    title = "NIVEAU 13 : MISES À JOUR ET LOGICIELS"
    objectives = [
        "Actualiser les dépôts et mettre à jour les logiciels installés.",
        "Installer nmap, supprimer Telnet et vérifier l'installation."
    ]
    Guide = [
        "winget source update — Actualise les dépôts de logiciels disponibles.",
        "winget upgrade — Affiche les logiciels à mettre à jour et leurs versions disponibles.",
        "winget upgrade --all — Installe toutes les mises à jour disponibles d'un coup.",
        "winget search nmap — Recherche le paquet nmap dans les dépôts winget.",
        "winget install nmap — Installe Nmap (identifiant : Insecure.Nmap).",
        "dism /online /disable-feature /featurename:TelnetClient — Désactive le client Telnet pour sécuriser le système.",
        "winget list --id Insecure.Nmap — Vérifie que Nmap est bien installé.",
        "Suivez l'ordre : mise à jour → installation nmap → suppression Telnet → vérification.",
    ]
    hint = "Essayez : winget source update, puis winget upgrade --all"

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

            common = generic_cmd_handler(cmd, arg_str, Guide)
            if common == "EXIT":
                return False
            if common:
                continue

            if cmd == "winget":
                if low.startswith("winget source update"):
                    print("\nSuccessfully updated all configured sources.")
                    print("Done. 3 sources updated.")
                    if 1 not in done:
                        done.add(1)
                        print_objective_done(1)
                elif low.startswith("winget upgrade") and "--all" in low:
                    print("\nFound 34 upgrades available.")
                    print("Downloading: https://download.software.com/openvpn-2.6.5.msi")
                    print("Installing:  OpenVPN 2.6.5")
                    print("Successfully installed 34 of 34 upgrades.")
                    if 3 not in done:
                        done.add(3)
                        print("Vous avez terminé l'objectif 3 ! Installez nmap avec winget.\n")
                elif low.startswith("winget upgrade"):
                    print("\nName                              Id                                Version  Available")
                    print("------------------------------------------------------------------------------------------")
                    print("OpenVPN                           OpenVPN.OpenVPN                   2.5.9    2.6.5")
                    print("Git                               Git.Git                          2.39.2   2.43.0")
                    print("Nmap                              Insecure.Nmap                     7.80     7.94")
                    if 2 not in done:
                        done.add(2)
                        print("Vous avez terminé l'objectif 2 ! Mettez tout à jour avec winget upgrade --all.\n")
                elif low.startswith("winget search nmap"):
                    print("\nName                         Id                   Version  Source")
                    print("--------------------------------------------------------------")
                    print("Nmap                         Insecure.Nmap         7.94     winget")
                    if 4 not in done:
                        done.add(4)
                        print_objective_done(4)
                elif "install" in low and "nmap" in low:
                    print("\nFound Nmap [Insecure.Nmap] Version 7.94")
                    print("This application is licensed to you by its owner.")
                    print("Downloading: https://nmap.org/dist/nmap-7.94-setup.exe")
                    print("Successfully installed")
                    print("SUCCESS: Nmap a été installé.")
                    if 5 not in done:
                        done.add(5)
                        print("Vous avez terminé l'objectif 5 ! Désactivez Telnet avec dism.\n")
                elif low.startswith("winget list") and "nmap" in low:
                    print("\nName              Id             Version  Source   Available")
                    print("----------------------------------------------------------------")
                    print("Nmap              Insecure.Nmap  7.94     winget")
                    print("\nSUCCESS: Nmap est bien installé.")
                    if 7 not in done:
                        done.add(7)
                        time.sleep(1)
                        print_success("Installation vérifiée. Niveau 13 terminé. FLAG=TW_UPDATES_13")
                        return True
                elif low.startswith("winget list"):
                    print("\nName                              Id                                 Version  Source")
                    print("----------------------------------------------------------------------------------------")
                    print("Nmap                              Insecure.Nmap                        7.94    winget")
                    print("Microsoft Telnet Client           Microsoft.TelnetClient                6.2    msstore")
                    print("OpenVPN                           OpenVPN.OpenVPN                      2.5.9   winget")
                else:
                    print("Commande winget non reconnue. Utilisez 'winget source update'.")
            elif cmd == "dism" and "disable-feature" in low and "telnetclient" in low:
                print("\nDeployment Image Servicing and Management tool")
                print("Version: 10.0.19045.4046\n")
                print("Image Version: 10.0.19045.4046\n")
                print("Enabling feature(s)")
                print("[==========================100.0%==========================]")
                print("The operation completed successfully.")
                print("SUCCESS: TelnetClient a été désactivé.")
                if 6 not in done:
                    done.add(6)
                    print("Vous avez terminé l'objectif 6 ! Vérifiez avec winget list --id Insecure.Nmap.\n")
            elif cmd == "dism" and "get-features" in low:
                print("\nFeatures listing for : C:\\")
                print("                                                            State")
                print("---------------------------------------------------------------------")
                print("TelnetClient                                             : Enabled")
                print("Microsoft-Windows-Subsystem-Linux                        : Disabled")
                print("\nTelnetClient est toujours actif : désactivez-le avec dism.")
                if 6 not in done and 5 in done:
                    print("Vous avez terminé l'objectif 6 ! Désactivez TelnetClient avec dism.\n")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()