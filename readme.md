# Titre du Projet

## Description
Ce projet génère un monde virtuel en utilisant des poids pour différents types de terrain. Il permet de simuler l'émergence de terrains variés.

## Table des matières
- [Architecture du code](#architecture-du-code)
- [Explication des modules](#explication-des-modules)
- [Détails des fonctions](#détails-des-fonctions)
- [Instructions d'installation](#instructions-dinstallation)
- [Exemples d'utilisation](#exemples-dutilisation)
- [Contributions](#contributions)
- [Contact](#contact)
- [Licences](#licences)

## Architecture du code
Le projet est structuré en plusieurs modules, chacun ayant un rôle spécifique dans la génération et le dessin du monde.

## Explication des modules
- **world** : Gère la logique de génération du monde.
- **configureWorld** : Contient les configurations nécessaires pour la génération du monde.
- **World_Drawer** : Responsable du rendu graphique du monde.

## Détails des fonctions
### test_generate_world(weights, random_seed)
- **Description** : Génère un monde basé sur des poids spécifiés et un `random_seed`.
- **Paramètres** :
  - `weights` : Liste des poids pour différents types de terrain.
  - `random_seed` : Valeur pour la génération aléatoire.
- **Exemple** :
  ```python
  test_generate_world([5, 3, 2, 1, 0, 0, 0], 42)

  