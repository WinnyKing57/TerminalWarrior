# Politique de sécurité

## Jeu d'entraînement (CTF)

**TerminalWarrior** est une application d'entraînement à la cybersécurité qui *simule*
des vulnérabilités dans un terminal fictif. Les drapeaux `TW_*` et les scénarios des
niveaux sont des **éléments de gameplay**, pas de vrais secrets.

## Signaler un problème

Si vous découvrez une vulnérabilité réelle dans le code du dépôt (et non dans les
scénarios simulés), merci de respecter une divulgation coordonnée :

1. **Ne partagez pas publiquement** le détail tant qu'il n'est pas corrigé.
2. Ouvrez une issue GitHub avec la mention `[Sécurité]` dans le titre (ou un email
   privé si l'information est sensible).
3. Décrivez le problème, les étapes de reproduction et l'impact estimé.

## Ce qui n'est PAS une vulnérabilité

Les éléments suivants sont volontaires et simulés :

- Commandes « exécutables » qui ne font que simuler une sortie de terminal ;
- Flags `TW_*`, mots de passe et secrets présents dans les scénarios de jeu ;
- Niveaux « faillibles » décrivant des systèmes compromis ou mal configurés.

Seuls les défauts du code d'exécution réel (exécution de commandes sur l'hôte, fuite
de données, mauvaise gestion des entrées, dépendances compromises) sont concernés.