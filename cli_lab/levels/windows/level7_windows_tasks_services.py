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


def run_level():
    title = "NIVEAU 7 : PLANIFICATEUR DE TÂCHES ET SERVICES"
    objectives = [
        "Inspecter les tâches planifiées pour détecter des entrées suspectes.",
        "Inspecter les services pour détecter des signes de persistance."
    ]
    hint = "Utilisez 'schtasks /query /fo list /v' et 'sc query'."

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    tasks_checked = False
    services_checked = False

    while True:
        try:
            user_input = input(build_prompt(CURRENT_DIR)).strip()
            parts = user_input.split()
            cmd = parts[0].lower() if parts else ""
            args = parts[1:]
            arg_str = " ".join(args)

            common = generic_cmd_handler(cmd, arg_str)
            if common == "EXIT":
                return False
            if common:
                continue

            if cmd == "schtasks":
                if "/query" in user_input.lower():
                    tasks_checked = True
                    print("\nTaskName: \\WindowsUpdateCache")
                    print("Next Run Time: 2/20/2026 11:00:00 AM")
                    print("Status: Ready")
                    print("Task To Run: C:\\ProgramData\\svchost_cache.exe\n")
                else:
                    print("ERROR: Invalid parameters.")
            elif cmd == "sc":
                if "query" in user_input.lower():
                    services_checked = True
                    print("\nSERVICE_NAME: WinDefendCache")
                    print("        TYPE               : 10  WIN32_OWN_PROCESS")
                    print("        STATE              : 4  RUNNING")
                    print("        BINARY_PATH_NAME   : C:\\ProgramData\\defender_cache.exe\n")
                else:
                    print("ERROR: Invalid parameters.")
            else:
                print(f"'{user_input}' is not recognized.")

            if tasks_checked and services_checked:
                time.sleep(1)
                print_success("Persistance identifiée. Flag : TW_TASK_PERSISTENCE_7")
                return True

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()
