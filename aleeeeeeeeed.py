def draw_walls(coord: List[str], config: 'MazeConfig') -> None:

    height = len(coord)
    width = len(coord[0])
    
    # 1. On crée une grille totalement remplie de murs
    grid = [["██" for _ in range(width * 2 + 1)] for _ in range(height * 2 + 1)]
    
    # 2. On creuse les passages selon les données hexadécimales
    for y, line in enumerate(coord):
        for x, hexa in enumerate(line):
            walls = decode_walls(hexa)
            
            # Coordonnées du centre de la case dans la nouvelle grille
            cx = x * 2 + 1
            cy = y * 2 + 1
            
            # On creuse le centre
            grid[cy][cx] = "  " 
            
            # On creuse les murs adjacents s'ils sont ouverts (False = pas de mur)
            if not walls["N"]: grid[cy - 1][cx] = "  "
            if not walls["S"]: grid[cy + 1][cx] = "  "
            if not walls["E"]: grid[cy][cx + 1] = "  "
            if not walls["W"]: grid[cy][cx - 1] = "  "

    # 3. On place l'Entrée (EE) et la Sortie (XX)
    ent_x, ent_y = map(int, config.ENTRY.split(","))
    end_x, end_y = map(int, config.EXIT.split(","))
    grid[ent_y * 2 + 1][ent_x * 2 + 1] = "EE"
    grid[end_y * 2 + 1][end_x * 2 + 1] = "XX"

    # 4. On affiche le résultat final
    for row in grid:
        print("".join(row))


ef draw_walls(coord: List[str], config: 'MazeConfig') -> None:
    height = len(coord)
    width = len(coord[0])
    
    # --- DESIGN : Codes couleurs ANSI pour le terminal ---
    WALL = "\033[90m██\033[0m"  # Gris foncé pour les murs
    PATH = "  "                 # Espace vide pour les couloirs
    ENT  = "\033[92m██\033[0m"  # Vert fluo pour l'Entrée
    EXT  = "\033[91m██\033[0m"  # Rouge fluo pour la Sortie
    
    # 1. On initialise un bloc de murs massif
    grid = [[WALL for _ in range(width * 2 + 1)] for _ in range(height * 2 + 1)]
    
    # 2. On sculpte les passages à l'intérieur
    for y, line in enumerate(coord):
        for x, hexa in enumerate(line):
            walls = decode_walls(hexa)
            
            # Centre de la cellule courante
            cx, cy = x * 2 + 1, y * 2 + 1
            grid[cy][cx] = PATH 
            
            # On casse les murs s'ils sont ouverts (False = pas de mur)
            if not walls["N"]: grid[cy - 1][cx] = PATH
            if not walls["S"]: grid[cy + 1][cx] = PATH
            if not walls["E"]: grid[cy][cx + 1] = PATH
            if not walls["W"]: grid[cy][cx - 1] = PATH

    # 3. On peint l'Entrée et la Sortie
    ent_x, ent_y = map(int, config.ENTRY.split(","))
    end_x, end_y = map(int, config.EXIT.split(","))
    grid[ent_y * 2 + 1][ent_x * 2 + 1] = ENT
    grid[end_y * 2 + 1][end_x * 2 + 1] = EXT

    # 4. Affichage du chef-d'œuvre
    for row in grid:
        print("".join(row))
