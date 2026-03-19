def maze_data_extract(file: str) -> List[str]:
    maze = []
    path = []

    try:
        with open(file, 'r', encoding="utf-8") as lines:
            all_lines = lines.readlines()
            path = all_lines[-1].strip()  # Dernière ligne
            
            for line in all_lines[:-1]:  # Toutes sauf la dernière
                line = line.strip()
                if not line:
                    continue

                if "," in line:
                    pass  # On ignore les coordonnées
                elif "S" or "W" or "N" in line:
                    pass  # On ignore
                else:
                    maze.append(line)

            return maze, path

    except FileNotFoundError:
        print(f"Error : The file {file} has not been generated")
        sys.exit()