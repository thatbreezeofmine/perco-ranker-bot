# Perco Ranker Bot

## Fonctionnalités

* L'utilisateur peut attacher une capture d'écran à la commande "?perco"
  * Le crawler extrait les données du combat
  * ~~Le robot ajoute des points aux participants et leurs guildes respectives~~
  * ~~Le robot confirme que la prédiction est correcte par reaction d'un modérateur~~
  * ~~Le robot notifie l'administrateur pour rajouter les points manuellement en cas de mauvaise prédiction~~
  * ~~Le robot met à jour le leaderboard~~
* ~~Le modérateur peut utiliser la commande "?link @[usermention] @[ingame_name]" pour associer le personnage au compte discord~~
* ~~Le modérateur peut utiliser la commande "?link @[usermention]" pour afficher la liste des personnages attachés au compte discord~~
* ~~Le modérateur peut utiliser la commande "?unlink @[usermention] @[ingame_name]" pour dissocier un personnage du compte dsicord~~
* ~~Le modérateur peut utiliser la commande "?unlink @[usermention]" pour dissocier tous les personnages du compte discord~~
* L'utilisateur peut utiliser la commande "?help" pour afficher la liste des commandes du robot.
* ~~L'utilisateur peut utiliser la commande "?rank @[usermention]" pour afficher le rang du compte discord mentionné~~

## Bug connus

* ~~Inhomogenous shape qui surgit quelques fois~~
* ~~Crash en cas de bug~~
* ~~Un personnage pourrait être détecté comme deux différents (cas Rolls-Roys)~~
* Certains caractères sont confondus par le crawler "I/l -> |"

## Améliorations

* ~~Port de la base de données sur SQLite au lieu de JSON~~
