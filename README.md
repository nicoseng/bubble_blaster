# Jeu de Bubble Blaster 

Dépot Github : https://github.com/nicoseng/bubble_blaster
Programme rédigé sous Python3 et avec le module Pygame (version 1.9.6)
Projet sous Virtual Env et Git 

Ce document a pour objectif de guider l’utilisateur étape par étape afin de lui permettre de lancer le jeu depuis son ordinateur.

## I°) Préparer l’environnement virtuel de développement
    1.	Installer un environnement virtuel de développement depuis votre terminal. (python3 –m venv env)
    2.	Activer l’environnement virtuel en tapant source env/bin/activate. Une mention (env) s’affiche à gauche de votre console.

## II°) Activer le jeu 
    Dans le terminal, entrer python3 test.py. Ce dernier correspond au fichier principal du jeu. 

## III°) Jouer au jeu 

L’objectif du jeu est d'attraper un maximum de bulles bleues afin de battre son propre record ! Les bulles rouges font perdre des points. Il faut donc les éviter au maximum !

* Se déplacer dans l'océan
   Appuyer au choix sur les flèches directionnelles. 
   
* Récupérer une bulle
   Se déplacer à l'endroit où se trouve la bulle bleue. L’objet ramassé disparaît du labyrinthe et le compteur inventaire indique le nombre d’objet ramassé. 

* Gagner/Perdre le jeu 
   Le jeu se termine lorque le score du joueru atteint zéro A défaut la partie continue. Un message de défaite s’affiche en cas de perte. 
   
* Rejouer au jeu 
	A tout moment, le joueur peut quitter le jeu. Pour ce faire, appuyer sur la touche r du clavier.

* Quitter le jeu 
	A tout moment, le joueur peut quitter le jeu. Pour ce faire, cliquer directement sur la croix pour fermer la fenêtre.
