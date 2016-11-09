import random


class FourInLine:
    def __init__(self, playerX, playerO, width, height):
        self.height = height
        self.board = []
        for i in range(width):
            self.board.append([])
        self.red, self.blue = playerX, playerO
        self.turn = random.choice(['B', 'Y'])

    def play_game(self):
        self.red.start_game('Y')
        self.blue.start_game('B')
        while True: #yolo
            if self.turn == 'Y':
                player, char, other_player = self.red, 'Y', self.blue
            else:
                player, char, other_player = self.blue, 'B', self.red
            if player.breed == "human":
                self.display_board()
            column = player.move(self.board,self.height)
            self.board[column].append(char)
            if self.player_wins(char,column):
                player.reward(1, self.board)
                other_player.reward(-1, self.board)
                break
            if self.board_full(): # tie game
                player.reward(0.5, self.board)
                other_player.reward(0.5, self.board)
                break
            other_player.reward(0, self.board)
            if self.turn == 'Y':
                self.turn = 'B'
            else:
                self.turn = 'Y'

    def player_wins(self, char, column):
        #TODO: hacer!
#        for a,b,c in [(0,1,2), (3,4,5), (6,7,8),
#                      (0,3,6), (1,4,7), (2,5,8),
#                      (0,4,8), (2,4,6)]:
#            if char == self.board[a] == self.board[b] == self.board[c]:
#                return True
        return False

    def board_full(self):
        return not any([len(column) < self.height for column in self.board])

    def display_board(self):
        for j in range(self.height-1,-1,-1):
            row = "|"
            for i in range(len(self.board)):
                if j < len(self.board[i]):
                    row += str(self.board[i][j]) + "|"
                else:
                    row += " |"
            print (row)

class Player(object):
    def __init__(self):
        self.breed = "human"

    def start_game(self, char):
        print "\nNew game!"

    def move(self, board,height):
        x = len(board)
        while (x < 0 or x >= len(board) or len(board[x]) >= height):
            x = int(raw_input("Your move? "))-1
        return x

    def reward(self, value, board):
        print "{} rewarded: {}".format(self.breed, value)

    def available_moves(self, board, height):
        return [i for i in range(len(board)) if len(board[i]) < height]


class RandomPlayer(Player):
    def __init__(self):
        self.breed = "random"

    def reward(self, value, board):
        pass

    def start_game(self, char):
        pass

    def move(self, board,height):
        return random.choice(self.available_moves(board,height))

# p1 = RandomPlayer()
# p1 = MinimaxPlayer()
# p1 = MinimuddledPlayer()
# p1 = QLearningPlayer()
# p2 = QLearningPlayer()



#for i in xrange(0,200):
#    t = TicTacToe(p1, p2)
#    t.play_game()

#p1 = Player()
#p2.epsilon = 0

p1 = Player()
p2 = Player()

while True:
    t = FourInLine(p1, p2, 5, 2)
    t.play_game()
