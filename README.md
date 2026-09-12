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

##  Vue d'ensemble ![Python](https://img.shields.io/badge/python-3.9%2B-blue) ![License](https://img.shields.io/badge/licence-MIT-green) [![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/WinnyKing57/TerminalWarrior) [![GitHub Stars](https://img.shields.io/github/stars/WinnyKing57/TerminalWarrior?style=social)](https://github.com/WinnyKing57/TerminalWarrior)
**TerminalWarrior** est un jeu d'entraînement interactif en ligne de commande où les joueurs explorent un système de fichiers Linux/Windows simulé pour découvrir des drapeaux (flags), mots de passe et secrets en utilisant de vraies commandes de terminal.

## ✨ Fonctionnalités
- 🟦 **Simulation de terminal style Linux/Windows** (Python uniquement)
- 🧩 **Plusieurs niveaux à difficulté croissante**
- 💻 **Commandes réalistes** (`ls`, `cat`, `cd`, `chmod`, `sudo`, etc.)
- 📌 **Suivi de progression avec liste de défis**
- 🐳 **Support Docker complet** (aucune installation requise)
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
#### Étape 3 : Installer les dépendances
```bash
pip install pyfiglet
```
#### Étape 4 : Lancer le CLI Lab
```bash
python -m cli_lab.main
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
#### Étape 3 : Installer les dépendances
```bash
pip install pyfiglet
```
#### Étape 4 : Lancer le CLI Lab
```bash
python -m cli_lab.main
```