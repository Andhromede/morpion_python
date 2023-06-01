import random


class Morpion:
    """ Le constructeur de la classe Morpion est définis par __init__ """
    def __init__(self):
        self.grid = []


    # CREATION DE LA GRILLE
    """ 
    crée les row une par une (3 lignes) par ex :
    row: ['_', '_', '_'] OU row: ['X', '_', '_'] 
    """
    def create_grid(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('_')
            self.grid.append(row)


    # RAN ALEATOIRE DU 1ER JOUEUR
    def ran_first_player(self):
        return random.randint(0, 1)


    # ENREGISTRE L'EMPLACEMENT
    def save_spot(self, row, col, player):
        self.grid[row][col] = player


    # CHERCHE SI LE JOUEUR GAGNE
    def check_if_win(self, player):
        win = None
        gridLen = len(self.grid)

        # vérifie les lignes
        for i in range(gridLen):
            win = True
            for j in range(gridLen):
                if self.grid[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # vérifie les colones
        for i in range(gridLen):
            win = True
            for j in range(gridLen):
                if self.grid[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # vérifie les diagonales
        win = True
        for i in range(gridLen):
            if self.grid[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(gridLen):
            if self.grid[i][gridLen - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False


    # DEFINIE COMMENT SONT REMPLIES LES CASES (_ ou X ou O)
    def is_grid_filled(self):
        for row in self.grid:
            for item in row:
                if item == '_':
                    return False
        return True


    # CHANGE LE TOUR DES JOUEURS
    def switch_turn(self, player):
        return 'X' if player == 'O' else 'O'


    # AFFICHE LA GRILLE COMPLETE
    """
    grid = [0:['_', '_', '_'], 
            1:['_', '_', '_'], 
            2:['_', '_', '_']
            ]
    row = ['_', '_', '_']
    item = '_'
    """
    def show_grid(self):
        for row in self.grid:
            for item in row:
                print(item, end=" ")
            print()


    # LANCE LE JEUX
    def start(self):
        self.create_grid()

        player = 'X' if self.ran_first_player() == 1 else 'O'
        while True:
            print(f"Au joueur {player} de jouer : ")
            self.show_grid()

            # Récupère l'input du joueur
            """
            si le joueur tappe "2 3" alors :
            row: 2
            col: 3
            """
            row, col = list(
                map(int, input("Entrez un numero de ligne puis de colone : ").split()))
            print()

            # enregistre l'emplacement dans la grid
            """ grid: [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']] """
            self.save_spot(row - 1, col - 1, player)

            if self.check_if_win(player):
                print(f"Le joueur {player} à gagné !")
                break

            if self.is_grid_filled():
                print("Match Nul!")
                break

            player = self.switch_turn(player)

        print()
        self.show_grid()

Morpion().start()