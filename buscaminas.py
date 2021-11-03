from random import randint

class Buscaminas:
    def __init__(self, rows, cols, bombs):
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.board = []
        self.show = []

    def create_board(self):
        for i in range(self.rows):
            l = []
            for n in range(self.cols):
                l.append(0)
        for m in range(self.bombs+1):
            self.board[randint(0, rows-1)][randint(0, cols-1)] = 'B' 
        for i in range(self.rows):
            for n in range(self.cols):
                if self.board[i][n] == 'B':
                   pass

    def create_show_board(self):
        for i in range(self.rows):
            l = []
            for n in range(self.cols):
                l.append(' ')

    def show_board(self):
        return self.show

    def question(self, movs):
        return [input('Ingrese el movimiento ', movs, ': '), int(input('Ingrese la fila: ')), int(input('Ingrese la columna: '))]                 

    def win(self):
        b = 0
        for i in range(self.rows):
            for n in range(self.cols):
                if self.board[i][n] == 'B' and self.show[i][n] == 'F':
                    b += 1
        if b == self.bombs:
            return True

    def lose(self):
        for i in range(self.rows):
            for n in range(self.cols):
                if  self.show[i][n] == 'B':
                    return True

    def play(self, mov, rows, cols):
        if mov == 'uncover':
            self.show[rows][cols] = self.board[rows][cols]
        elif mov == 'flag':
            self.show[rows][cols] = 'F'
