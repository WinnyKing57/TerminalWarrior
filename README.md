<p align="center">
<img src="logo.gif">
</p>

Défi de cybersécurité en ligne de commande conteneurisé, développé en Python, simulant un terminal Linux/Windows où les joueurs résolvent des énigmes de style hacking en utilisant de vraies commandes Linux/Windows.

> **ℹ️ À propos de ce dépôt** : il s'agit d'un **fork en français** du projet
> [TerminalWarrior](https://github.com/diversionsec/TerminalWarrior) (contenu
> original en anglais). Les textes du jeu (menus, défis, indices, aide,
> messages de progression) ont été traduits en français. Pour rester jouable,
> les **commandes à saisir**, les noms de fichiers et les sorties simulant un
> vrai terminal sont conservées en anglais.

##  Vue d'ensemble ![Python](https://img.shields.io/badge/python-3.9%2B-blue) ![License](https://img.shields.io/badge/licence-MIT-green) [![CI](https://github.com/WinnyKing57/TerminalWarrior/actions/workflows/ci.yml/badge.svg)](https://github.com/WinnyKing57/TerminalWarrior/actions/workflows/ci.yml) [![GitHub Stars](https://img.shields.io/github/stars/WinnyKing57/TerminalWarrior?style=social)](https://github.com/WinnyKing57/TerminalWarrior)
**TerminalWarrior** est un jeu d'entraînement interactif en ligne de commande où les joueurs explorent un système de fichiers Linux/Windows simulé pour découvrir des drapeaux (flags), mots de passe et secrets en utilisant de vraies commandes de terminal.

## ✨ Fonctionnalités
- 🟦 **Simulation de terminal style Linux/Windows** (Python uniquement)
- 🧩 **Niveaux à difficulté croissante** (19 Linux + 24 Windows + 2 bonus)
- 💻 **Commandes réalistes** (`ls`, `cat`, `cd`, `chmod`, `sudo`, etc.)
- 📌 **Suivi de progression avec liste de défis**
- 💾 **Sauvegarde de progression automatique** (fichier JSON + horodatage des niveaux terminés, stocké dans `~/.terminal_warrior_progress.json`)
- 🏆 **Compteur de score** (points gagnés par niveau terminé)
- 📊 **Menu « Progression »** : score total, temps par niveau et pourcentage complété
- 🥷 **Niveaux bonus** avec drapeaux (flags) encodés en deux couches (hexadécimal + base64)
- 🎲 **Scénarios aléatoires** à chaque partie (PID, adresses IP, noms de fichiers)
- 🐳 **Support Docker complet** (aucune installation requise)
- 🧪 **Suite de tests** (pytest) exécutée automatiquement en CI
- 🖥️ **Multi-plateforme** — Windows, macOS, Linux

## Vue d'ensemble des niveaux

---
### 🐧 Niveaux Linux :
1. **Défi d'introduction** : Explorez les répertoires et trouvez les fichiers cachés | Commandes Linux de base `ls`, `cat`, `cd`, `pwd`, `whoami`
2. **Permissions et propriété** : Apprenez à consulter et modifier les permissions des fichiers | `chmod`, `chown`, `sudo`, `su`
3. **Recherche sur le système** : Trouvez les fichiers cachés et analysez les journaux | `grep`, `find`, `locate`, `which`, `whereis`
4. **Défi réseau** : Découvrez les hôtes et les services | `ping`, `netcat`, `traceroute`, `nmap`
5. **Cryptographie et décodage** : Décodez les messages cachés et les fichiers de hachage | `base64`, hachage, chiffrements simples
6. **Processus et surveillance système** : Repérez et arrêtez un processus de minage malveillant | `uname`, `uptime`, `free`, `df`, `ps`, `pgrep`, `kill`
7. **Services et systemd** : Enquêtez sur un service de porte dérobée | `systemctl`, `journalctl`
8. **Gestion de paquets (APT)** : Mettez à jour le système et gérez les paquets | `apt update`, `apt upgrade`, `apt install`, `apt remove`
9. **Pare-feu (UFW)** : Sécurisez la machine en configurant le pare-feu | `sudo ufw status`, `enable`, `allow`, `deny`, `default`
10. **Utilisateurs et groupes** : Créez des comptes et neutralisez un intrus | `id`, `groups`, `groupadd`, `useradd`, `usermod`, `userdel`
11. **Journaux et surveillance** : Retracez une attaque en analysant les journaux | `tail`, `head`, `grep`, `journalctl -xe`, `dmesg`
12. **Archivage et compression** : Extrayez et analysez une sauvegarde suspecte | `file`, `tar`, `gzip`, `gunzip`
13. **Tâches planifiées (Cron)** : Découvrez et supprimez une tâche cron malveillante | `crontab`, `cat /etc/crontab`, `ls /etc/cron.d`, `rm`
14. **Variables d'environnement** : Repérez et corrigez un PATH détourné | `echo $PATH`, `env`, `which`, `export`, `unset`, `set`
15. **Ports et services réseau** : Découvrez et arrêtez une backdoor sur le port 31337 | `netstat -tulpn`, `ss`, `lsof`, `nmap`, `curl`, `kill`
16. **Intégrité des fichiers** : Repérez et restaurez un binaire altéré | `sha256sum`, `md5sum`, `cmp`, `cp`
17. **Liens symboliques et montages** : Neutralisez un lien symbolique malveillant | `ls -la`, `readlink`, `file`, `lsblk`, `rm`, `ln -s`
18. **Scripts shell** : Créez et exécutez un script de nettoyage | `touch`, `echo`, `cat`, `chmod +x`, `./script.sh`
19. **Durcissement SSH** : Interdisez la connexion root par mot de passe | `grep`, `sudo sed -i`, `ssh-keygen`, `systemctl restart ssh`
20. **🎁 BONUS - Décryptage de flag** : Décodez un drapeau à deux couches | `xxd`, `base64 -d`, `echo`

### 🪟 Niveaux Windows :
1. **Défi d'introduction** : Naviguez dans les dossiers et découvrez les fichiers cachés | Commandes Windows de base `dir`, `cd`, `type`, `cls`, `echo`
2. **Permissions et propriété** : Consultez et modifiez les droits des fichiers | `icacls`, `attrib`, `takeown`
3. **Recherche sur le système** : Traquez les fichiers cachés et lisez les journaux | `findstr`, `where`, `tree`
4. **Défi réseau** : Scannez le réseau et vérifiez les services | `ping`, `tracert`, `netstat`, `curl`, `ipconfig`
5. **Cryptographie et décodage** : Décodez les messages et inspectez les hachages | `base64`, `certutil`, chiffrements simples
6. **Exploration approfondie du registre** : Naviguez dans le registre Windows pour trouver des clés de configuration cachées
7. **Planificateur de tâches et services** : Enquêtez sur les tâches planifiées et les services à la recherche d'activités malveillantes
8. **Forensique des journaux d'événements** : Analysez les journaux d'événements Windows pour retracer les incidents de sécurité
9. **Forensique du disque et récupération de fichiers** : Récupérez les fichiers supprimés et analysez les partitions
10. **Défi de scripts PowerShell** : Utilisez PowerShell pour automatiser des tâches et résoudre des problèmes complexes
11. **Processus et performance** : Repérez et arrêtez un processus de minage malveillant | `systeminfo`, `wmic`, `tasklist`, `taskkill`
12. **Services et démarrage** : Enquêtez sur un service de porte dérobée | `sc query`, `sc stop`, `sc config`, `net start`
13. **Mises à jour et logiciels** : Mettez à jour le système et gérez les logiciels | `winget`, `dism`
14. **Pare-feu Windows Defender** : Sécurisez la machine avec le pare-feu | `netsh advfirewall`
15. **Utilisateurs et groupes** : Créez des comptes et neutralisez un intrus | `net user`, `net localgroup`
16. **Journaux d'événements** : Retracez une attaque dans le journal Security | `wevtutil`, `Get-WinEvent`
17. **Archivage et extraction** : Extrayez et analysez une sauvegarde suspecte | `Expand-Archive`, `tar`, `type`
18. **Tâches planifiées (schtasks)** : Découvrez et supprimez une tâche malveillante | `schtasks /query`, `/delete`
19. **Variables d'environnement** : Repérez et corrigez un PATH détourné | `set`, `echo %PATH%`, `set PATH=...`
20. **Ports et services réseau** : Découvrez et arrêtez une backdoor sur le port 31337 | `netstat -ano`, `findstr`, `tasklist`, `taskkill`, `curl`
21. **Intégrité des fichiers** : Repérez et restaurez un fichier altéré | `certutil -hashfile`, `Get-FileHash`, `fc /b`, `copy /y`
22. **Jonctions et disques** : Neutralisez une jonction malveillante | `dir`, `fsutil reparsepoint query`, `wmic logicaldisk`, `rmdir`, `mklink /D`
23. **Scripts batch et PowerShell** : Créez et exécutez un script de nettoyage | `echo >`, `type`, `where`, `cleanup.bat`
24. **Durcissement RDP** : Désactivez le Bureau à distance exposé | `reg query`, `reg add`, `sc query TermService`, `netstat`
25. **🎁 BONUS - Décryptage de flag** : Décodez un drapeau à deux couches | `type`, `certutil -decodehex`, `certutil -decode`, `echo`

## Installation et mise en route

----

### 🐧 Exécution locale sous Linux

#### Étape 1 : Cloner le dépôt
```bash
git clone https://github.com/WinnyKing57/TerminalWarrior.git
```
#### Étape 2 : Entrer dans le dossier du projet
```bash
cd TerminalWarrior
```
#### Étape 3 : Installer les prérequis système (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```
#### Étape 4 : Créer et activer un environnement virtuel
Un environnement virtuel isole les dépendances du jeu de celles du système, ce qui évite les conflits (et l'erreur `externally-managed-environment` sur Debian 12+).
```bash
python3 -m venv .venv
source .venv/bin/activate
```
#### Étape 5 : Installer les dépendances dans le venv
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
#### Étape 6 : Lancer le CLI Lab
```bash
python -m cli_lab.main
```

> **💡 Astuce** : à chaque nouvelle session de terminal, réactivez l'environnement virtuel avec `source .venv/bin/activate` avant de revenir à l'étape 6.

### 🐳 Lancement avec Docker

#### Étape 1 : Construire l'image
```bash
docker build -t terminal-warrior .
```
#### Étape 2 : Lancer un conteneur interactif
```bash
docker run -it --rm terminal-warrior
```

### 🧪 Exécution des tests

La suite de tests pytest est exécutée automatiquement en CI (`.github/workflows/ci.yml`).
Pour la lancer en local (environnement virtuel activé) :
```bash
python -m pip install pytest
python -m pytest tests/ -q
```

### 🪟 Exécution locale sous Windows

#### Étape 1 : Cloner le dépôt
```bash
git clone https://github.com/WinnyKing57/TerminalWarrior.git
```
#### Étape 2 : Entrer dans le dossier du projet
```bash
cd TerminalWarrior
```
#### Étape 3 : Créer et activer un environnement virtuel
```powershell
py -m venv .venv
.venv\Scripts\activate
```
#### Étape 4 : Installer les dépendances dans le venv
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
#### Étape 5 : Lancer le CLI Lab
```bash
python -m cli_lab.main
```

> **💡 Astuce** : à chaque nouvelle session, réactivez l'environnement virtuel avec `.venv\Scripts\activate` avant de revenir à l'étape 5.

## 🧑‍💻 Contribuer

La branche `main` est **protégée** (push direct interdit). Pour toute modification :

1. Créez une branche : `git checkout -b feature/ma-modif`
2. Commitez puis poussez : `git push origin feature/ma-modif`
3. Ouvrez une pull request vers `main` : `gh pr create --fill`
4. La CI (`pytest tests/ -q`) doit passer avant le merge.
5. Mergez la PR (merge ou squash), puis supprimez la branche.

Règles appliquées sur `main` :
- Pull request obligatoire (aucun push direct)
- Statut CI `test` requis
- **1 approbation requise** pour les autres contributeurs (le propriétaire est exempté de l'approbation)
- Force-push et suppression de branche interdits