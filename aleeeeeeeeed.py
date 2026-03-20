def draw_walls(mlx_ptr, win, grid: List[str], config: MazeConfig, p_size: int) -> None:
    # On parcourt chaque ligne (y)
    for y, row in enumerate(grid):
        # On parcourt chaque colonne (x)
        for x, char_hex in enumerate(row):
            # Calcul du coin supérieur gauche de la case en pixels
            x_p = x * p_size
            y_p = y * p_size
            
            # Décodage du caractère hexadécimal
            walls = decode_walls(char_hex)

            # Couleur des murs (blanc par exemple)
            color = 0xFFFFFF 

            # Dessin des segments de mur
            if walls["N"]: # Mur du haut
                mlx_ptr.line(win, x_p, y_p, x_p + p_size, y_p, color)
            if walls["S"]: # Mur du bas
                mlx_ptr.line(win, x_p, y_p + p_size, x_p + p_size, y_p + p_size, color)
            if walls["E"]: # Mur de droite
                mlx_ptr.line(win, x_p + p_size, y_p, x_p + p_size, y_p + p_size, color)
            if walls["W"]: # Mur de gauche
                mlx_ptr.line(win, x_p, y_p, x_p, y_p + p_size, color)

if main

                # On extrait les données du fichier généré
        # maze_data[0] contient la grille de caractères
        maze_data = maze_data_extract(config.OUTPUT_FILE)
        grid = maze_data[0] 
        
        # Initialisation MLX
        mlx_ptr = mlx.Mlx() # Selon ton wrapper, l'appel peut varier
        
        pixel_size = 64
        win_width = config.WIDTH * pixel_size
        win_height = config.HEIGHT * pixel_size
        win = mlx_ptr.new_window(win_width, win_height, "A-MAZE-ING")

        # APPEL DU DESSIN
        draw_walls(mlx_ptr, win, grid, config, pixel_size)

        # On lance la boucle pour que la fenêtre reste ouverte
        mlx_ptr.loop()