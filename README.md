# 🏰 A-MAZE-ING

## Description

**À COMPLÉTER** : Écrivez une description du projet ici (2-3 lignes).

Exemple : Un générateur de labyrinthes interactif en Python utilisant l'algorithme Growing Tree. Le programme génère des labyrinthes parfaits ou imparfaits et permet de visualiser le chemin de l'entrée à la sortie.

---

## 📋 Table des matières

- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Configuration](#configuration)
- [Architecture](#architecture)
- [Algorithmes](#algorithmes)
- [Auteurs](#auteurs)

---

## ✨ Fonctionnalités

- ✅ Génération aléatoire de labyrinthes
- ✅ Algorithme Growing Tree pour labyrinthes parfaits
- ✅ Support des labyrinthes imparfaits (défectueux)
- ✅ Affichage interactif du labyrinthe
- ✅ Visualisation du chemin de l'entrée à la sortie
- ✅ Système de couleurs personnalisable
- ✅ Gestion des configurations via fichier `config.txt`

**À COMPLÉTER** : Ajoutez d'autres fonctionnalités si elles existent.

---

## 🚀 Installation

### Prérequis

- Python 3.10+
- pip ou venv

### Étapes

1. **Cloner le repository**
   ```bash
   git clone <URL_DU_REPO>
   cd A-MAZE-ING
   ```

2. **Créer un environnement virtuel**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirement.txt
   ```

**À COMPLÉTER** : Ajoutez des instructions spécifiques si nécessaire.

---

## 💻 Utilisation

### Lancement du programme

```bash
make run
```

ou directement :

```bash
python3 a_maze_ing.py config.txt
```

### Menu interactif

Lors du lancement, vous verrez le menu suivant :

```
1 - Re-generate a new maze
2 - Show/Hide path from entry to exit
3 - Rotate maze colors
4 - Quit
```

**À COMPLÉTER** : Détaillez chaque option du menu.

---

## ⚙️ Configuration

Le fichier `config.txt` permet de personnaliser les paramètres du labyrinthe :

```ini
WIDTH=20              # Largeur du labyrinthe
HEIGHT=20             # Hauteur du labyrinthe
ENTRY=2,6             # Point d'entrée (x,y)
EXIT=6,8              # Point de sortie (x,y)
OUTPUT_FILE=maze.txt  # Fichier de sortie
PERFECT=True          # Labyrinthe parfait (True/False)
SEED=                 # Graine aléatoire (optionnel)
```

**À COMPLÉTER** : Expliquez les impacts de chaque paramètre.

---

## 📁 Architecture

```
A-MAZE-ING/
├── a_maze_ing.py           # Fichier principal
├── config.txt              # Configuration
├── maze.txt                # Sortie du labyrinthe
├── maze_algorithm/
│   ├── maze.py             # Classe de base MazeGenerator
│   ├── growing_tree.py     # Algorithme Growing Tree
│   └── defective_maze.py   # Génération de labyrinthes imparfaits
├── tools1/
│   ├── bfs_algorithm.py    # Algorithme BFS pour trouver le chemin
│   └── gen_output.py       # Génération de fichiers de sortie
└── visualize/
    ├── draw.py             # Affichage ASCII du labyrinthe
    ├── parsing.py          # Parsing des configurations
    └── utils.py            # Utilitaires
```

**À COMPLÉTER** : Ajoutez des explications pour chaque module si nécessaire.

---

## 🧮 Algorithmes

### Growing Tree (Croissance d'arbre)

**À COMPLÉTER** : Expliquez l'algorithme Growing Tree en détail.

Exemple : 
L'algorithme Growing Tree fonctionne en deux phases principales :
1. Partir d'une cellule de départ...
2. Continuer jusqu'à obtenir un labyrinthe complet...

### Recherche du chemin (BFS)

**À COMPLÉTER** : Expliquez l'algorithme de recherche du chemin (Breadth-First Search).

---

## 🧪 Commandes utiles

### Développement

```bash
make lint          # Vérifier le code avec flake8 et mypy
make debug         # Lancer en mode débogage
make clean         # Nettoyer les fichiers __pycache__
make install       # Installer les dépendances
```

### Tests

**À COMPLÉTER** : Ajoutez la commande pour exécuter les tests si vous en avez.

---

## 📊 Format de sortie

Le fichier de sortie `maze.txt` contient **À COMPLÉTER** : Décrivez le format du fichier de sortie (exemple : format binaire, format texte, etc.).

---

## 🐛 Troubleshooting

### Problème 1 : **À COMPLÉTER**
Solution : ...

### Problème 2 : **À COMPLÉTER**
Solution : ...

---

## 👥 Auteurs

- **À COMPLÉTER** : Qui a développé ce projet ?

---

## 📄 Licence

**À COMPLÉTER** : Quelle est la licence du projet ? (MIT, GPL, etc.)

---

## 📞 Support

**À COMPLÉTER** : Comment contacter l'équipe de support ? Où signaler des bugs ?

---

## 🔮 Améliorations futures

- [ ] **À COMPLÉTER** : Ajoutez des fonctionnalités prévues

---

**Dernière mise à jour** : Mars 2026

