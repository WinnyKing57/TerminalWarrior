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
    title = "NIVEAU 11 : PROCESSUS ET PERFORMANCE"
    objectives = [
        "Identifier le processus min.exe qui consomme l'essentiel du CPU.",
        "Obtenir son PID via tasklist, puis le terminer avec taskkill."
    ]
    hint = "Essayez : tasklist, puis taskkill /pid <PID> /f"

    print_header(title)
    print_objectives(objectives, hint)
    print_windows_motd()

    done = set()
    min_pid = random.randint(3000, 4999)
    min_cpu = random.randint(60, 98)

    while True:
        try:
            user_input = input(build_prompt(CURRENT_DIR)).strip()
            parts = user_input.split()
            cmd = parts[0].lower() if parts else ""
            args = parts[1:]
            arg_str = " ".join(args)
            low = user_input.lower()

            if cmd == "whoami" or cmd == "exit":
                common = generic_cmd_handler(cmd, arg_str)
                if common == "EXIT":
                    return False
                continue

            common = generic_cmd_handler(cmd, arg_str)
            if common == "EXIT":
                return False
            if common:
                continue

            if cmd == "systeminfo":
                print("\nHost Name:                 WS-OPS-01")
                print("OS Name:                   Microsoft Windows 10 Pro")
                print("OS Version:                10.0.19045 N/A Build 19045")
                print("System Type:               x64-based PC")
                print("Total Physical Memory:     8,192 MB")
                print("Available Physical Memory: 2,356 MB")
                print("Processor:                 Intel(R) Core(TM) i7-8700K CPU @ 3.70GHz")
                print("Boot Device:               \\Device\\HarddiskVolume2")
                if 1 not in done:
                    done.add(1)
                    print_objective_done(1)
            elif cmd == "tasklist" and "min.exe" in low and "fi" in low:
                print("\nImage Name                     PID Session Name        Session#    Mem Usage")
                print("========================= ======== ================ =========== ============")
                print(f"min.exe                       {min_pid}  Console                   1     612,240 K")
                print(f"\nLe PID du processus min.exe est {min_pid}.")
                if 4 not in done:
                    done.add(4)
                    print("Vous avez terminé l'objectif 4 ! Terminez min.exe avec taskkill /pid <PID> /f.\n")
            elif cmd == "tasklist":
                print("\nImage Name                     PID Session Name        Session#    Mem Usage")
                print("========================= ======== ================ =========== ============")
                print("System Idle Process              0  Services                   0          8 K")
                print("System                           4  Services                   0      1,024 K")
                print("svchost.exe                    912  Services                   0     22,400 K")
                print("explorer.exe                  3324  Console                   1     88,120 K")
                print(f"min.exe                       {min_pid}  Console                   1     612,240 K")
                print(f"\nmin.exe consomme {min_cpu}% du CPU et propose une grosse empreinte mémoire : il est suspect !")
                if 3 not in done:
                    done.add(3)
                    print_objective_done(3)
            elif cmd == "wmic" and "loadpercentage" in low:
                print("\nLoadPercentage")
                print(f"{min_cpu}")
                if 2 not in done:
                    done.add(2)
                    print_objective_done(2)
            elif cmd == "taskkill":
                target = None
                for arg in args:
                    if arg.lower().startswith("/pid"):
                        continue
                    if arg.lower().startswith("/f"):
                        continue
                    if arg.lower().startswith("/t"):
                        continue
                    if arg.isdigit():
                        target = int(arg)
                if target == min_pid:
                    print(f"SUCCESS: Sent termination signal to the process with PID {target}.\n")
                    print(f"{target}")
                    time.sleep(1)
                    print_success(f"Processus min.exe (PID {target}) arrêté. Niveau 11 terminé. FLAG=TW_PROCESSES_11")
                    return True
                elif target is not None:
                    print(f"ERROR: The process with PID {target} could not be terminated.")
                else:
                    print("Usage: taskkill /pid <PID> /f")
            else:
                print(f"'{user_input}' is not recognized.")

        except KeyboardInterrupt:
            return False


def main():
    return run_level()


if __name__ == "__main__":
    main()