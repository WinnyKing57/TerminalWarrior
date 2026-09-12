import importlib
import importlib.util
import random
from pathlib import Path

import pytest

from conftest import REPO

LINUX_DIR = REPO / "cli_lab" / "levels" / "linux"

USERS = ["JoeBiden", "DonaldTrump", "JeremyClarkson", "RichardHammond",
         "JamesMay", "GordonRamsay", "ColdPlay", "JeffreyDahmer", "HarryPotter", "KimJongUn"]
PWDS = ["DumbassLeftHisPassword", "Password123!", "ILeftMyKeysAgain", "Admin1234", "qwerty_is_bad",
        "LetMeInPlease", "Eggcellent123", "Passw0rd!", "ThisIsNotASecurePass", "ForgottenPassword69"]


def load_linux(fname):
    spec = importlib.util.spec_from_file_location(fname[:-3], str(LINUX_DIR / fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_windows(name):
    return importlib.import_module("cli_lab.levels.windows." + name)


def drive_linux(monkeypatch, mod, seq, expected):
    captured = []
    it = iter(seq)
    monkeypatch.setattr("builtins.input", lambda prompt="": next(it, "exit"))
    monkeypatch.setattr("builtins.print", lambda *a, **k: captured.append(" ".join(str(x) for x in a)))
    try:
        result = mod.main()
    except StopIteration:
        result = None
    out = "\n".join(captured)
    assert result is True, "level did not report completion (main() returned %r)" % (result,)
    missing = [e for e in expected if e not in out]
    assert not missing, "missing: %s" % missing


def drive_windows(monkeypatch, mod, seq, expected):
    captured = []
    queue = list(seq)

    def fake_input(prompt=""):
        if not queue:
            raise StopIteration("end of inputs")
        return queue.pop(0)

    monkeypatch.setattr("builtins.input", fake_input)
    monkeypatch.setattr("builtins.print", lambda *a, **k: captured.append(" ".join(str(x) for x in a)))
    try:
        result = mod.run_level()
    except StopIteration:
        result = None
    out = "\n".join(captured)
    assert result is True, "level did not report completion (run_level() returned %r)" % (result,)
    missing = [e for e in expected if e not in out]
    assert not missing, "missing: %s" % missing


# ---------------------------------------------------------------------------
# Linux : niveaux 1-5 (originaux) et 6-19 (ajoutés), + bonus 20
# ---------------------------------------------------------------------------

def level1_inputs():
    random.seed(3)
    random.randint(100, 200); random.randint(100, 800); random.randint(1, 24)
    random.randint(10, 59); random.randint(10, 59); random.randint(1, 28)
    ip = ".".join(str(random.randint(1, 254)) for _ in range(4))
    u = random.choice(USERS)
    p = random.choice(PWDS)
    random.seed(3)
    return ["", "challenge", "help", "ls", "cd Flag", "cat Flag.txt", "cd ..",
            "cd Documents", "cat ssh_Username.txt", "cat ssh_Password.txt",
            "cd ..", "cat notes.txt", f"ssh {u}@{ip}", p,
            "ls", "ls -la", "cat hidden.txt", "challenge", "exit", "exit"]


def test_linux_level1(monkeypatch):
    seq = level1_inputs()
    random.seed(3)
    drive_linux(monkeypatch, load_linux("level1_linux_intro.py"), seq,
                ["Défi 6 terminé", "Au revoir"])


def test_linux_level2(monkeypatch):
    drive_linux(monkeypatch, load_linux("level2_linux_permissions.py"),
                ["", "ls -la", "read hidden_data.txt", "su root", "toor",
                 "chown user hidden_data.txt", "su user", "read hidden_data.txt",
                 "ls", "read HelloWorld.exe", "su root", "toor",
                 "chmod 777 HelloWorld.exe", "read HelloWorld.exe", "challenge", "exit"],
                ["Vous avez terminé le défi 7"])


def test_linux_level3(monkeypatch):
    drive_linux(monkeypatch, load_linux("level3_linux_searching.py"),
                ["", "ls -la", "find . -name .security.log", "locate .security.log",
                 "which grep", "whereis grep", "grep FAILED .security.log",
                 "grep sshd .security.log", "challenge", "exit"],
                ["Vous avez terminé le défi 6"])


def test_linux_level4(monkeypatch):
    drive_linux(monkeypatch, load_linux("level4_linux_networking.py"),
                ["", "ping 8.8.8.8", "traceroute google.com", "ifconfig",
                 "netstat -tuln", "nslookup google.com", "ssh user@localhost", "user",
                 "nmap localhost", "challenge", "exit"],
                ["Vous avez terminé le défi 7"])


def test_linux_level5(monkeypatch):
    drive_linux(monkeypatch, load_linux("level5_linux_cryptography.py"),
                ["", "md5sum secret.txt",
                 "openssl enc -aes-256-cbc -in secret.txt -out encrypted.bin -e -k pass",
                 "openssl enc -aes-256-cbc -d -in encrypted.bin -out decrypted.txt -k pass",
                 "sha256sum secret.txt", "openssl rand -hex 32",
                 "gpg --symmetric secret.txt", "gpg --decrypt secret.txt.gpg",
                 "challenge", "exit"],
                ["Vous avez terminé le défi 7"])


LINUX_6_19 = [
    ("level6_linux_processes.py", 4321, ["", "help", "challenge",
                                         "uname -a", "uptime", "free -h", "df -h",
                                         "ps aux", "pgrep -f cryptominer", "kill -9 4321"],
     ["Vous avez terminé le défi 7", "Au revoir"]),
    ("level7_linux_services.py", None, ["", "systemctl list-units --type=service",
                                        "systemctl status backdoor.service",
                                        "journalctl -u backdoor.service",
                                        "systemctl stop backdoor.service",
                                        "systemctl disable backdoor.service",
                                        "systemctl enable sshd"],
     ["Vous avez terminé le défi 6", "Au revoir"]),
    ("level8_linux_apt.py", None, ["", "sudo apt update", "apt list --upgradable", "sudo apt upgrade -y",
                                   "apt search nmap", "sudo apt install nmap -y",
                                   "sudo apt remove telnet -y", "apt list --installed | grep nmap"],
     ["Vous avez terminé le défi 7", "Au revoir"]),
    ("level9_linux_ufw.py", None, ["", "sudo ufw status", "sudo ufw enable", "sudo ufw default deny incoming",
                                   "sudo ufw allow 22", "sudo ufw deny 8080", "sudo ufw status verbose"],
     ["Vous avez terminé le défi 6", "Au revoir"]),
    ("level10_linux_users.py", None, ["", "id", "groups", "cat /etc/passwd",
                                      "sudo groupadd ops", "sudo useradd -m agent -g ops",
                                      "sudo usermod -aG sudo agent", "sudo userdel -r invader"],
     ["Vous avez terminé le défi 7", "Au revoir"]),
    ("level11_linux_logs.py", None, ["", "tail -n 50 /var/log/syslog", "head -n 20 /var/log/syslog",
                                     "grep sshd /var/log/auth.log", "journalctl -xe", "dmesg",
                                     "cat /var/log/syslog"],
     ["Vous avez terminé le défi 6", "Au revoir"]),
    ("level12_linux_archives.py", None, ["", "file backup.tar.gz", "tar -tzf backup.tar.gz",
                                         "tar -xzf backup.tar.gz", "ls", "gzip -d data.log.gz",
                                         "cat extracted_flag.txt"],
     ["Vous avez terminé le défi 6", "Au revoir"]),
    ("level13_linux_cron.py", None, ["", "crontab -l", "cat /etc/crontab", "ls /etc/cron.d",
                                     "cat /etc/cron.d/pwn", "systemctl list-timers", "rm /etc/cron.d/pwn"],
     ["Vous avez terminé le défi 6", "Au revoir"]),
    ("level14_linux_env_vars.py", None, ["", "echo $PATH", "env", "which ls", "echo $LD_PRELOAD",
                                         "export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                                         "unset LD_PRELOAD", "set"],
     ["Vous avez terminé le défi 7", "Au revoir"]),
    ("level15_linux_ports_services.py", 3141, ["", "netstat -tulpn", "ss -tulpn", "lsof -i :31337",
                                               "nmap localhost", "curl http://localhost:31337",
                                               "kill -9 3141", "netstat -tulpn"],
     ["Vous avez terminé le défi 7", "Au revoir"]),
    ("level16_linux_integrity.py", None, ["", "sha256sum /usr/bin/agent", "cat /usr/bin/agent.expected",
                                          "cmp /usr/bin/agent /usr/bin/agent.orig", "md5sum /usr/bin/agent",
                                          "cp /usr/bin/agent.orig /usr/bin/agent", "sha256sum /usr/bin/agent"],
     ["Vous avez terminé le défi 6", "Au revoir"]),
    ("level17_linux_links_mounts.py", None, ["", "ls -la", "readlink backup_link", "file backup_link",
                                             "lsblk", "mount", "df -h", "rm backup_link",
                                             "ln -s /home/user/real_backup backup_link"],
     ["Vous avez terminé le défi 6", "Au revoir"]),
    ("level18_linux_scripts.py", None, ["", "touch cleanup.sh", "echo '#!/bin/bash' > cleanup.sh",
                                        "cat cleanup.sh", "chmod +x cleanup.sh", "./cleanup.sh",
                                        "ls -la cleanup.sh"],
     ["Vous avez terminé le défi 6", "Au revoir"]),
    ("level19_linux_ssh_hardening.py", None, ["", "cat /etc/ssh/sshd_config",
                                              "grep -E \"PermitRootLogin|PasswordAuthentication\" /etc/ssh/sshd_config",
                                              "sudo sed -i \"s/PermitRootLogin yes/PermitRootLogin no/\" /etc/ssh/sshd_config",
                                              "ssh-keygen -t ed25519", "sudo systemctl restart ssh",
                                              "grep PasswordAuthentication /etc/ssh/sshd_config"],
     ["Vous avez terminé le défi 6", "Au revoir"]),
]


@pytest.mark.parametrize("fname,pid,seq,expected", LINUX_6_19, ids=[c[0] for c in LINUX_6_19])
def test_linux_levels_6_19(monkeypatch, fname, pid, seq, expected):
    mod = load_linux(fname)
    if pid is not None:
        mod.random.randint = lambda a, b: pid
    drive_linux(monkeypatch, mod, seq, expected)


def test_linux_level20_bonus(monkeypatch):
    mod = load_linux("level20_linux_bonus_flag.py")
    mod._TEST_FLAG = "TW_BONUS_LNX_TEST01"
    mod._TEST_NAMES = ("flag_t.enc", "r.bin", "clean.txt")
    drive_linux(monkeypatch, mod,
                ["", "cat flag_t.enc", "xxd -r -p flag_t.enc r.bin", "cat r.bin",
                 "base64 -d r.bin clean.txt", "cat clean.txt", "echo TW_BONUS_LNX_TEST01"],
                ["Vous avez terminé le défi 1", "Vous avez terminé le défi 6"])


# ---------------------------------------------------------------------------
# Windows : niveaux 1-10 (originaux) et 11-24 (ajoutés), + bonus 25
# ---------------------------------------------------------------------------

WINDOWS_1_10 = [
    ("level1_windows_recon", ["dir", "cd Intel", "dir /a", "type notes.txt", ""],
     ["SUCCESS: Fichier caché récupéré. Niveau 1 terminé."]),
    ("level2_windows_permissions", ["dir /a", "attrib secret.txt", "takeown /f secret.txt",
                                    "icacls secret.txt /grant user:(F)", "type secret.txt", ""],
     ["SUCCESS: Permissions corrigées. Niveau 2 terminé."]),
    ("level3_windows_searching", ["where /r . audit.log", "findstr FLAG audit.log", ""],
     ["SUCCESS: Drapeau trouvé dans les journaux. Niveau 3 terminé."]),
    ("level4_windows_networking", ["ipconfig", "ping 10.10.5.23", "netstat -an",
                                   "curl http://10.10.5.23:8080/", ""],
     ["SUCCESS: Jeton du service capturé. Niveau 4 terminé."]),
    ("level5_windows_cryptography", ["dir", "type message.b64", "certutil -decode message.b64 message.txt",
                                     "type message.txt", "rot13 SVANY_SYNT: JVAQBJF_ZNFGRE_UNPXRE", ""],
     ["SUCCESS: Chiffrement résolu. Niveau 5 terminé."]),
    ("level6_windows_registry", [r"reg query HKCU\Software\TerminalWarrior\Hidden /v Secret", ""],
     ["SUCCESS: Clé de registre localisée. Niveau 6 terminé."]),
    ("level7_windows_tasks_services", ["schtasks /query /fo list /v", "sc query", ""],
     ["SUCCESS: Persistance identifiée. Flag : TW_TASK_PERSISTENCE_7"]),
    ("level8_Windows_event_logs", ["wevtutil qe Security /c:10 /rd:true", ""],
     ["SUCCESS: Incident retracé. Flag : TW_EVENT_TRACE_8"]),
    ("level9_windows_disk_forensics", ["list volume", "dir /a C:\\$Recycle.Bin", "type d3l3t3d.txt", ""],
     ["SUCCESS: Fichier supprimé récupéré. Niveau 9 terminé."]),
    ("level10_windows_powershell", ["dir", "type tasks.txt",
                                    'powershell -command "Get-Content tasks.txt | Select-String FLAG"', ""],
     ["SUCCESS: Automatisation terminée. Niveau 10 terminé."]),
]


@pytest.mark.parametrize("name,seq,expected", WINDOWS_1_10, ids=[c[0] for c in WINDOWS_1_10])
def test_windows_levels_1_10(monkeypatch, name, seq, expected):
    drive_windows(monkeypatch, load_windows(name), seq, expected)


WINDOWS_11_24 = [
    ("level11_windows_processes", 4321,
     ["systeminfo", "wmic cpu get loadpercentage", "tasklist",
      'tasklist /fi "imagename eq min.exe"', "taskkill /pid 4321 /f", ""],
     ["Niveau 11 terminé", "FLAG=TW_PROCESSES_11"]),
    ("level12_windows_services", None,
     ["sc query", 'sc query "pwnsvc"', 'sc stop "pwnsvc"', 'sc config "pwnsvc" start= disabled',
      "net start sshd", "sc query OpenSSHd", ""],
     ["Niveau 12 terminé", "FLAG=TW_SERVICES_12"]),
    ("level13_windows_updates", None,
     ["winget source update", "winget upgrade", "winget upgrade --all", "winget search nmap",
      "winget install nmap", "dism /online /disable-feature /featurename:TelnetClient",
      "winget list --id Insecure.Nmap", ""],
     ["Niveau 13 terminé", "FLAG=TW_UPDATES_13"]),
    ("level14_windows_firewall", None,
     ["netsh advfirewall show allprofiles state", "netsh advfirewall set allprofiles state on",
      "netsh advfirewall set allprofiles firewallpolicy blockinbound,allowoutbound",
      'netsh advfirewall firewall add rule name=SSH dir=in action=allow protocol=TCP localport=22',
      'netsh advfirewall firewall add rule name=Block8080 dir=in action=block protocol=TCP localport=8080',
      "netsh advfirewall firewall show rule name=all", ""],
     ["Niveau 14 terminé", "FLAG=TW_FIREWALL_14"]),
    ("level15_windows_users_groups", None,
     ["whoami", "net user", "net user invader", "net localgroup Operations /add",
      "net user agent /add", "net localgroup Administrators agent /add", "net user invader /delete", ""],
     ["Niveau 15 terminé", "FLAG=TW_USERS_15"]),
    ("level16_windows_event_logs", 4321,
     ["wevtutil el", "wevtutil qe System /f:text /c:20",
      'wevtutil qe Security "*[System/EventID=4625]" /c:10',
      'powershell "Get-WinEvent -FilterHashtable @{LogName=\'Security\';Id=4625} -MaxEvents 3"',
      'powershell "Get-WinEvent -LogName Security -MaxEvents 1 | Format-List"', ""],
     ["Niveau 16 terminé", "FLAG=TW_EVENTLOGS_16"]),
    ("level17_windows_archives", None,
     ["dir", 'powershell "Expand-Archive -Path backup.zip -DestinationPath ."', "dir",
      "tar -xzf data.log.gz", "type extracted_flag.txt", ""],
     ["Niveau 17 terminé", "FLAG=TW_ARCHIVES_17"]),
    ("level18_windows_scheduled_tasks", None,
     ["schtasks /query /fo LIST /v", "schtasks /query /tn SystemMaintenance /fo LIST /v",
      "schtasks /query /tn Beacon /fo LIST /v", "schtasks /query /tn Beacon /xml",
      "schtasks /delete /tn Beacon /f", ""],
     ["Niveau 18 terminé", "FLAG=TW_SCHTASKS_18"]),
    ("level19_windows_env_vars", None,
     ["set", "echo %PATH%", "echo %MALVAR%", "set PATH=%SystemRoot%\\system32;%SystemRoot%",
      "set MALVAR=", "set", ""],
     ["Niveau 19 terminé", "FLAG=TW_ENVVARS_19"]),
    ("level20_windows_ports_services", 3141,
     ["netstat -ano", "netstat -ano | findstr 31337", 'tasklist /fi "PID eq 3141"',
      "curl http://localhost:31337", "taskkill /pid 3141 /f", "netstat -ano | findstr 31337", ""],
     ["Niveau 20 terminé", "FLAG=TW_PORTS_20"]),
    ("level21_windows_integrity", None,
     ["certutil -hashfile C:\\Windows\\System32\\drivers\\etc\\hosts SHA256",
      "type C:\\tools\\hosts.expected",
      "fc /b C:\\Windows\\System32\\drivers\\etc\\hosts C:\\tools\\hosts.orig",
      "copy /y C:\\tools\\hosts.orig C:\\Windows\\System32\\drivers\\etc\\hosts",
      'powershell "Get-FileHash -Algorithm SHA256 -Path C:\\Windows\\System32\\drivers\\etc\\hosts"', ""],
     ["Niveau 21 terminé", "FLAG=TW_INTEGRITY_21"]),
    ("level22_windows_junctions_disks", None,
     ["dir", "fsutil reparsepoint query notes_link", "wmic logicaldisk get", "rmdir notes_link",
      "mklink /D notes_link C:\\Users\\User\\real_notes", "dir", ""],
     ["Niveau 22 terminé", "FLAG=TW_JUNCTIONS_22"]),
    ("level23_windows_scripts", None,
     ["echo @echo off > cleanup.bat", "echo del /f /q C:\\Temp\\malware.exe >> cleanup.bat",
      "type cleanup.bat", "where cleanup.bat", "cleanup.bat", ""],
     ["Niveau 23 terminé", "FLAG=TW_SCRIPTS_23"]),
    ("level24_windows_rdp_hardening", None,
     ['reg query "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server" /v fDenyTSConnections',
      "sc query TermService", "netstat -ano | findstr 3389",
      'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 1 /f',
      'reg query "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server" /v fDenyTSConnections', ""],
     ["Niveau 24 terminé", "FLAG=TW_RDP_HARDEN_24"]),
]


@pytest.mark.parametrize("name,pid,seq,expected", WINDOWS_11_24, ids=[c[0] for c in WINDOWS_11_24])
def test_windows_levels_11_24(monkeypatch, name, pid, seq, expected):
    mod = load_windows(name)
    if pid is not None:
        mod.random.randint = lambda a, b: pid
    drive_windows(monkeypatch, mod, seq, expected)


def test_windows_level25_bonus(monkeypatch):
    mod = load_windows("level25_windows_bonus_flag")
    mod._TEST_FLAG = "TW_BONUS_WIN_TEST01"
    mod._TEST_NAMES = ("flag_t.enc", "r.b64", "clean.txt")
    drive_windows(monkeypatch, mod,
                  ["type flag_t.enc", "certutil -decodehex flag_t.enc r.b64", "type r.b64",
                   "certutil -decode r.b64 clean.txt", "type clean.txt", "echo TW_BONUS_WIN_TEST01", ""],
                  ["Niveau bonus terminé", "FLAG=TW_BONUS_WIN_TEST01"])