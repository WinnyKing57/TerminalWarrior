"""Aides au terminal : tab-complétion et historique des commandes.

Le jeu simule un vrai terminal, il est donc agréable que ``Tab`` complète la
commande en cours et que la flèche ``↑`` rappelle les commandes déjà saisies.

L'implémentation s'appuie sur le module standard ``readline`` (Linux/macOS).
Sur les plateformes où il est indisponible (Windows), le jeu retombe
silencieusement sur un simple ``input()`` sans dégradation de fonctionnalité.

Usage :
    from cli_lab import terminal
    terminal.install()          # à appeler une seule fois au démarrage
    cmd = terminal.input_line() # remplace input(prompt).strip()
"""

import atexit
import os

HISTORY_FILE = os.path.expanduser("~/.terminal_warrior_history")
HISTORY_LENGTH = 500

# Commandes "métier" du jeu : les libellés reconnus par les niveaux, qui
# servent de vocabulaire de prédiction pour la touche Tab.
GAME_COMMANDS = [
    # Meta / navigation
    "help", "challenge", "exit", "clear",
    "pwd", "whoami", "id", "groups", "env", "set",
    # Niveau 1 - introduction
    "ls", "ls -a", "ls -al", "ls -l", "ls -la", "ls -lha",
    "cd Flag", "cd Documents", "cd ..", "cd Intel",
    "cat", "cat Flag.txt", "cat notes.txt", "cat Bin.txt",
    "cat birthday.txt", "cat something.txt",
    "cat ssh_Username.txt", "cat ssh_Password.txt", "cat hidden.txt",
    "ssh", "su root", "su user", "toor",
    # Niveau 2 - permissions
    "ls -la hidden_data.txt", "read hidden_data.txt", "read HelloWorld.exe",
    "chown user hidden_data.txt", "chmod 777 HelloWorld.exe",
    # Niveau 3 - recherche
    "find . -name .security.log", "locate .security.log",
    "which grep", "which ls", "whereis grep",
    "grep FAILED .security.log", "grep sshd .security.log",
    "grep sshd /var/log/auth.log",
    "grep -E \"PermitRootLogin|PasswordAuthentication\" /etc/ssh/sshd_config",
    "grep PasswordAuthentication /etc/ssh/sshd_config",
    # Niveau 4 - réseau
    "ping 8.8.8.8", "ping 10.10.5.23", "traceroute google.com",
    "ifconfig", "netstat -tuln", "netstat -tulpn", "netstat -an",
    "ss -tulpn", "nslookup google.com", "nmap localhost",
    "ssh user@localhost", "lsof -i :31337",
    "curl http://localhost:31337", "curl http://10.10.5.23:8080/",
    # Niveau 5 - cryptographie
    "md5sum secret.txt", "sha256sum secret.txt",
    "openssl enc -aes-256-cbc -in secret.txt -out encrypted.bin -e -k pass",
    "openssl enc -aes-256-cbc -d -in encrypted.bin -out decrypted.txt -k pass",
    "openssl rand -hex 32",
    "gpg --symmetric secret.txt", "gpg --decrypt secret.txt.gpg",
    "base64", "base64 -d r.bin clean.txt",
    # Niveau 6 - processus
    "uname -a", "uptime", "free -h", "df -h", "ps aux",
    "pgrep -f cryptominer", "kill -9 4321",
    # Niveau 7 - services / systemd
    "systemctl list-units --type=service", "systemctl status backdoor.service",
    "journalctl -u backdoor.service", "journalctl -xe",
    "systemctl stop backdoor.service", "systemctl disable backdoor.service",
    "systemctl enable sshd", "systemctl list-timers", "systemctl restart ssh",
    # Niveau 8 - apt
    "sudo apt update", "apt list --upgradable", "sudo apt upgrade -y",
    "apt search nmap", "sudo apt install nmap -y",
    "sudo apt remove telnet -y", "apt list --installed | grep nmap",
    # Niveau 9 - ufw
    "sudo ufw status", "sudo ufw enable", "sudo ufw default deny incoming",
    "sudo ufw allow 22", "sudo ufw deny 8080", "sudo ufw status verbose",
    # Niveau 10 - utilisateurs
    "cat /etc/passwd",
    "sudo groupadd ops", "sudo useradd -m agent -g ops",
    "sudo usermod -aG sudo agent", "sudo userdel -r invader",
    # Niveau 11 - journaux
    "tail -n 50 /var/log/syslog", "head -n 20 /var/log/syslog",
    "dmesg", "cat /var/log/syslog",
    # Niveau 12 - archives
    "file backup.tar.gz", "tar -tzf backup.tar.gz", "tar -xzf backup.tar.gz",
    "gzip -d data.log.gz",
    # Niveau 13 - cron
    "crontab -l", "cat /etc/crontab", "ls /etc/cron.d",
    "cat /etc/cron.d/pwn", "rm /etc/cron.d/pwn",
    # Niveau 14 - variables d'environnement
    "echo $PATH", "echo $LD_PRELOAD",
    "export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    "unset LD_PRELOAD",
    # Niveau 15 - ports / services
    "netstat -tulpn", "ss -tulpn", "lsof -i :31337",
    "curl http://localhost:31337",
    # Niveau 16 - intégrité
    "cat /usr/bin/agent.expected",
    "cmp /usr/bin/agent /usr/bin/agent.orig",
    "cp /usr/bin/agent.orig /usr/bin/agent",
    "sha256sum /usr/bin/agent", "md5sum /usr/bin/agent",
    # Niveau 17 - liens / montages
    "readlink backup_link", "file backup_link", "lsblk", "mount",
    "rm backup_link", "ln -s /home/user/real_backup backup_link",
    # Niveau 18 - scripts
    "touch cleanup.sh", "echo '#!/bin/bash' > cleanup.sh", "cat cleanup.sh",
    "chmod +x cleanup.sh", "./cleanup.sh", "ls -la cleanup.sh",
    # Niveau 19 - durcissement SSH
    "cat /etc/ssh/sshd_config",
    "sudo sed -i \"s/PermitRootLogin yes/PermitRootLogin no/\" /etc/ssh/sshd_config",
    "ssh-keygen -t ed25519",
    # Niveau 20 - bonus
    "cat flag_t.enc", "xxd -r -p flag_t.enc r.bin", "cat r.bin",
    "cat clean.txt",
    # Niveaux Windows - base
    "dir", "dir /a", "type", "cls", "tree", "ipconfig", "tracert",
    "type notes.txt", "type tasks.txt", "type message.b64",
    "type d3l3t3d.txt", "type extracted_flag.txt",
    "attrib secret.txt", "takeown /f secret.txt",
    "icacls secret.txt /grant user:(F)",
    "where /r . audit.log", "findstr FLAG audit.log",
    "net user", "net localgroup Operations /add", "net user agent /add",
    "certutil -decode message.b64 message.txt", "certutil -hashfile",
    "reg query", "reg add", "sc query", "schtasks /query /fo list /v",
    "wevtutil", "list volume",
    "systeminfo", "wmic cpu get loadpercentage", "tasklist",
    "taskkill /pid 4321 /f",
    "winget source update", "winget upgrade", "winget search nmap",
    "winget install nmap",
    "netsh advfirewall show allprofiles state",
    "echo %PATH%", "set PATH=%SystemRoot%\\system32;%SystemRoot%",
    "powershell",
    "curl http://10.10.5.23:8080/",
    "fc /b", "copy /y", "mklink /D", "rmdir notes_link",
    "fsutil reparsepoint query notes_link",
    "echo @echo off > cleanup.bat",
    "cleanup.bat",
]

def _tokenize(words):
    """Découpe les commandes en mots (une commande = une ligne du jeu)."""
    return sorted({token for word in words for token in word.split()})


_candidates = sorted(set(GAME_COMMANDS))
_tokens = _tokenize(GAME_COMMANDS)
_readline = None
_original_input = None
_installed = False


def complete(prefix, candidates=None):
    """Retourne les candidats (insensibles à la casse) qui commencent par prefix."""
    words = _candidates if candidates is None else sorted(set(candidates))
    p = prefix.lower()
    return [w for w in words if w.lower().startswith(p)]


def set_completions(words):
    """Restreint le vocabulaire de complétion à la liste donnée."""
    global _candidates, _tokens
    _candidates = sorted(set(words))
    _tokens = _tokenize(words)


def reset_completions():
    """Revient au vocabulaire complet du jeu."""
    global _candidates, _tokens
    _candidates = sorted(set(GAME_COMMANDS))
    _tokens = _tokenize(GAME_COMMANDS)


def _completer(text, state):
    rl = _readline
    if rl is None:
        return None
    matches = complete(text, _tokens)
    if state < len(matches):
        return matches[state]
    return None


def _save_history():
    rl = _readline
    if rl is None:
        return
    try:
        rl.set_history_length(HISTORY_LENGTH)
        rl.write_history_file(HISTORY_FILE)
    except (OSError, TypeError):
        pass


def input_line(prompt="", completions=None):
    """Équivalent de input(prompt).strip() avec complétion par Tab active."""
    if completions is not None:
        set_completions(completions)
    if _original_input is None:
        import builtins
        return builtins.input(prompt).strip()
    return _original_input(prompt).strip()


def _input_wrapper(prompt=""):
    return _original_input(prompt).strip()


def install():
    """Active la complétion Tab et l'historique pour tous les input() du jeu."""
    global _readline, _original_input, _installed
    if _installed:
        return

    import builtins
    _original_input = builtins.input

    try:
        import readline  # noqa: PLC0415
    except ImportError:
        _readline = None
        builtins.input = _input_wrapper
        _installed = True
        return

    _readline = readline
    readline.set_completer(_completer)
    readline.set_completer_delims(" \t\n")
    if "libedit" in getattr(readline, "__doc__", ""):
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")

    try:
        readline.read_history_file(HISTORY_FILE)
    except (OSError, ValueError):
        pass
    try:
        readline.set_history_length(HISTORY_LENGTH)
    except TypeError:
        pass

    builtins.input = _input_wrapper
    atexit.register(_save_history)
    _installed = True