This project has been created as part of the 42 curriculum by bbeaurai, fcaval

# 🏰 A-MAZE-ING

## 👥 Auteurs

Ce projet a été créé dans le cadre du programme 42 par Fleur Caval 🌸 et Benjamin Beaurain 🥕.

## 📝​ Description

Un générateur de labyrinthes interactif en Python utilisant l'algorithme Growing Tree. Le programme génère des labyrinthes parfaits ou imparfaits et permet de visualiser le chemin de l'entrée à la sortie.

## 🪼​ Rôles

Benjamin Beaurain : Implémentation de l'algorithme Growing Tree et logique des labyrinthes imparfaits.
Fleur Caval : Système de configuration, interface utilisateur (menu) et visualisation ASCII.

### 🔥 Rétrospective

* **Planning** : Initialement prévu sur 2 semaines, nous avons respecté notre délai personnel. Bien que nous avons dû laisser les bonus de côté.
* **Améliorations** : une visualisation MLX a été envisagé pour un meilleur rendu visuel. Mais celui ci a été abandonné pour le débuggage plus efficace de l'ASCII.

## 🧩 Réutilisabilité

Les modules situés dans `maze_algorithm/` sont totalement indépendants de l'interface. Ils peuvent être réutilisés dans n'importe quel projet Python en important la classe `MazeGenerator`. De même, `bfs_algorithm.py` est un solveur de grille générique.

---

## 📋 Table des matières

- [Auteurs](#auteurs)
- [Fonctionnalités](##fonctionnalités)
- [Installation](##installation)
- [Utilisation](##utilisation)
- [Configuration](##configuration)
- [Architecture](##architecture)
- [Algorithmes](#algorithmes)

---

## ✨ Fonctionnalités

- ✅ Génération aléatoire de labyrinthes
- ✅ Algorithme Growing Tree pour labyrinthes parfaits
- ✅ Support des labyrinthes imparfaits (défectueux)
- ✅ Affichage interactif du labyrinthe
- ✅ Visualisation du chemin de l'entrée à la sortie
- ✅ Système de couleurs personnalisable
- ✅ Gestion des configurations via fichier `config.txt`

---

## 🚀 Installation

### Prérequis

```Contenu du requirement.txt
- Python 3.10+
- pydantic>=2.12.5
- flake8>=7.3.0
- numpy>=1.26
- typing-extensions>=4.12
```

### Étapes

1. **Cloner le repository**
   ```bash
   git clone <URL_DU_REPO>
   cd A-MAZE-ING
   ```

2. **Lancement**
   ```bash
   make
   ```

Le MakeFile vérifie que les dépendances présentent dans le requirement.txt sont bien installées. Elle permet aussi de lancer la venv. 
Après cela, make lance python3 a-maze-ing config.txt

## 🧪 Commandes utiles

### Développement

```bash
make install       # Installer les dépendances
make lint          # Vérifier le code avec flake8 et mypy
make lint-strict   # Vérifier le code avec flake8 et mypy en mode strict
make debug         # Lancer en mode débogage
make clean         # Nettoyer les fichiers __pycache__
```

---

## 💻 Utilisation

### Menu interactif

Lors du lancement, vous verrez le menu suivant :

```
1 - Show a maze
2 - Re-generate a new maze
3 - Show/Hide path from entry to exit
4 - Rotate maze colors
5 - Quit
```

1. **Show a maze**
   ```bash
   1
   Montre le labyrinthe.
   ```

2. **Re-generate a new maze**
   ```bash
   2
   Génère un nouveau labyrinthe. Si la seed est remplie, le labyrinthe restera le même que généré     au début
   ```

3. **Show/Hide path from entry to exit**
   ```bash
   3
   Montre le chemin entre l'entrée et la sortie. L'entrée est caractérisé par "🟢". La sortie par     "🏁". Le chemin quant à lui par "⭐".
   Le mode d'affichage choisi reste actif dans les autres fonctionnalités.
   Si l'entrée ou la sortie se trouve sur l'affichage du 42, ils seront déplacés.
   ```

4. **Rotate maze colors**
   ```bash
   4
   Permet de changer la couleur des murs du labyrinthe. Le menu affiche les 7 couleurs                disponibles. Par défaut, au lancement, le labyrinthe est blanc. Si la couleur est changée, elle    persistera dans les autres paramètres.
   ```
   
5. **Quit**
   ```bash
   5
   Quitte le programme.
   ```

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

1. **WIDTH**
   ```bash
   Largeur du labyrinthe. Le minimum est de 2. Le maximum est de 50.
   ```
   
2. **HEIGHT**
   ```bash
   Longueur du labyrinthe. Le minimum est de 2. Le maximum est de 50.
   ```

3. **ENTRY**
   ```bash
   L'entrée du chemin. Elle ne peut être en dehors de la taille du labyrinthe.
   ```

4. **EXIT**
   ```bash
   La sortie du chemin. Elle ne peut être en dehors de la taille du labyrinthe.
   ```

5. **OUTPUT_FILE**
   ```bash
   Fichier de sortie de l'algorithme. Elle doit se terminer par ".txt"
   ```

6. **PERFECT**
   ```bash
   Se personnalise par un True ou False.
   True = labyrinthe parfait, c'est-à-dire qu'il n'existe qu'un seul chemin entre l'entrée            et la sortie.
   False = labyrinthe imparfait, c'est-à-dire qu'il existe plusieurs chemins entre l'entrée et la     sortie. L'algorithme affichera le chemin le plus court.
   ```

7. **SEED**
   ```bash
   Paramètre optionnel. Si cette variable est remplie. Le labyrinthe sera le même, grâce à            l'identité apposé avec cette valeur, même si nous le régénérons. 
   ```

---

## 📁 Architecture

```
A-MAZE-ING/
├── maze_algorithm/
│   ├── __init__.py             # Rend le dossier importable
│   ├── maze.py                 # Classe de base MazeGenerator (à créer/renommer)
│   ├── growing_tree.py         # Algorithme Growing Tree
│   └── defective_maze.py       # Génération de labyrinthes imparfaits
├── tools1/
│   ├── __init__.py             # Rend le dossier importable
│   ├── bfs_algorithm.py        # Algorithme BFS pour trouver le chemin
│   └── gen_output.py           # Génération de fichiers de sortie
├── visualize/
│   ├── __init__.py             # Rend le dossier importable
│   ├── draw.py                 # Affichage ASCII du labyrinthe
│   ├── parsing.py              # Parsing des configurations
│   └── utils.py                # Utilitaires
├── .gitignore                  # Exclusion des fichiers inutiles (__pycache__, .whl)
├── a_maze_ing.py               # Fichier principal (Point d'entrée)
├── config.txt                  # Fichier de configuration par défaut
├── Makefile                    # Automatisation (build, clean, test)
├── maze.txt                    # Fichier de sortie (généré par le programme)
├── pyproject.toml              # Configuration du packaging et des dépendances
├── README.md                   # Documentation du projet
└── requirement.txt             # Liste des bibliothèques Python
```

---

## 🧮 Algorithmes

### Intergration 42 patterns

<img width="3000" height="2000" alt="42patern" src="https://github.com/user-attachments/assets/eeb3b248-880f-4e96-b2a9-a0c0b6578380" />

### Patterns des cellules

<img width="3000" height="2000" alt="grille" src="https://github.com/user-attachments/assets/617de130-5c3c-412c-9a85-169eed5546f8" />

### Growing Tree (Croissance d'arbre)

<img width="3000" height="2000" alt="1036 8" src="https://github.com/user-attachments/assets/160e18a4-819a-4801-b2f9-5ef0eb3fabe1" />

Choix : cet algorithme a été choisi pour sa flexibilité et pour la qualité "organique" des labyrinthes produits. Nous l'avons trouvé inspirant. 

Explication de l'algorithme Growing Tree en détail:

1. Partir d'une cellule de départ...
2. Choisis des directions aléatoires
3. Dans le cas où aucune direction n'est possible, cul de sac
4. L'algorithme revient sur ses pas jusqu'à retrouver une direction
5. L'algorithme s'arrête quand le chemin revient à sa position initiale

---

### Recherche du chemin (BFS)
![bfs-gif](https://github.com/user-attachments/assets/b721a985-2e0a-4488-b9f5-8cf6f77b71a7)


Explication de l'algorithme BFS (Breadth-First Search) en détail:

1. **Initialisation** : Placer la cellule de départ dans une file d'attente (queue) et marquer cette cellule comme visitée.
2. **Exploration niveau par niveau** : Tant que la file n'est pas vide :
   - Retirer la cellule en tête de file (cellule actuelle).
   - Si cette cellule est la sortie, reconstruire le chemin en remontant les parents.
   - Sinon, explorer les quatre voisins possibles (haut, droite, bas, gauche) si ils sont valides (dans les limites du labyrinthe et sans mur).
   - Pour chaque voisin non visité, le marquer comme visité, l'ajouter à la file, et enregistrer la cellule actuelle comme parent avec la direction.
3. **Fin** : Si la file se vide sans avoir atteint la sortie, aucun chemin n'existe. Sinon, le chemin est reconstruit en utilisant les données de parent stockées.

---

## 📊 Format de sortie

Le fichier de sortie `maze.txt` contient: l'hexadécimal du labyrinthe avec l'entrée, la sortie et le chemin de résolution du labyrinthe
```
d5513913953951555553
9552eaaac3c6ba95553e
ad5696ac3c392ac553c3
83956969696eac513c3a
aac396ba96914396e96a
ac52ab86abaad2a956ba
abbeac47ac2c3ec6916a
aac3c553c3c7c1552a96
c43c53f83afff857aec3
93c17afec057fa95293a
ae9696fffafffac3eac2
a947ad13fafd507c3c3e
8695696afafffe952bc3
a96d543c3ad1516d4292
ac5539696c5696953aae
8579683c553d47abaec3
a93abaa953c3956ac53a
aac6c6ac7a96853853c2
aa93956956c3c7a83c7a
ec6c6d545554556ec556

2,6
19,19
SESEESSWSSWWSWSEEESWSSWNWSSSENESENEENNNWNENWNENESS....
```
---

## 📂​ Fichier .whl

1. **Creez un environnement virtuelle :**
```bash
python3 -m venv venv
```

2. **Activez l'environnement :**
```bash
source venv/bin/activate
```
3. **Installez UV :**
```bash
pip install uv
```
4. **Compressez les fichiers :**
```bash
uv build
```
Une fois cela fait, des fichiers devraient apparaître, dans dist vous trouverez mazegen-1.0.1-py3-none-any.whl. Depuis n'importe quel environnement vous pourrez installer mazegen via pip en mettant le chemin d'accès.

**Exemple**
```
pip install dist/mazegen-1.0.1-py3-none-any.whl
```
Depuis un programme vous pouvez utiliser le module de cette manière:
```bash
from mazegen.visualize.parsing import extract_config, MazeConfig, get_tuple
from mazegen.tools1.gen_output import output

cfg = extract_config("config.txt")
config = MazeConfig.model_validate(cfg)

entry_exit = get_tuple(config.ENTRY, config.EXIT)

output(
    config.WIDTH,
    config.HEIGHT,
    entry_exit[0],
    entry_exit[1],
    config.PERFECT,
    config.OUTPUT_FILE,
    config.SEED or None
)
print("Fichier généré :", config.OUTPUT_FILE)
```
Vous pouvez récuprer tous les attributs du labyrinthe via l'objet maze retourné par create_maze. Vous pouvez tout supprimer une fois l'opération terminée 👍

## 🩼 Utilisation de l'IA

L'IA a été utilisé pour aider dans la réalisation des docsting et des typing, ainsi que pour générer le squelette de ce README.md. Dans certains cas, elle a pu être utilisé pour débugger. 

## ​​📚 Ressources

Growing tree: https://weblog.jamisbuck.org/2011/1/27/maze-generation-growing-tree-algorithm
bfs: https://www.datacamp.com/tutorial/breadth-first-search-in-python
Compréhension binaire affichage : https://stackoverflow.com/questions/57610416/how-to-read-a-maze-from-an-image-and-convert-it-to-binary-values-in-python + https://realpython.com/videos/python-maze-binary-file/
Couleurs ASCII : https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
Dessin ASCII Pacman : https://www.asciiart.eu/art/a7c9e36489bc23e9
