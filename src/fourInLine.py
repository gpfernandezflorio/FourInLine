#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import pickle
import sys


def display_board(board, height):
    for j in range(height-1,-1,-1):
        row = "|"
        for i in range(len(board)):
            if j < len(board[i]):
                row += str(board[i][j]) + "|"
            else:
                row += " |"
        print (row)
    row = " "
    for i in range(len(board)):
        row += str(i+1) + " "
    print row

class FourInLine:
    def __init__(self, player1, player2, width, height):
        self.height = height
        self.board = []
        for i in range(width):
            self.board.append([])
        self.red, self.blue = player1, player2
        self.turn = random.choice(['1', '2'])

    def play_game(self, play=False):
        self.red.start_game('1',len(self.board))
        self.blue.start_game('2',len(self.board))

        while True: #yolo
            if self.turn == '1':
                player, char, other_player = self.red, '1', self.blue
            else:
                player, char, other_player = self.blue, '2', self.red
            if player.breed == "human":
                display_board(self.board, self.height)
            column = player.move(self.board,self.height)
            self.board[column].append(char)
            if self.player_wins(char,column):
                player.reward(1, self.board, self.height)
                other_player.reward(-1, self.board,self.height)
                if play:
                    display_board(self.board, self.height)
                    print "Jugador " + self.turn + " GANA! (" + player.breed + ")"
                return self.turn
            if self.board_full(): # tie game
                player.reward(0.5, self.board, self.height)
                other_player.reward(0.5, self.board,self.height)
                if play:
                    display_board(self.board, self.height)
                    print "EMPATE!"
                return "0"
            other_player.reward(0, self.board,self.height)
            if self.turn == '1':
                self.turn = '2'
            else:
                self.turn = '1'

    def board_full(self):
        return not any([len(column) < self.height for column in self.board])

    def player_wins(self, char, column):
        pos_y = len(self.board[column])-1
        pos_x = column
        if(self.check_vertically(char, pos_x, pos_y)):
            return True
        if(self.check_horizontally(char, pos_x, pos_y)):
            return True
        if(self.check_identity_diagonal(char, pos_x, pos_y)):
            return True
        if(self.check_not_identity_diagonal(char, pos_x, pos_y)):
            return True
        return False

    def check_vertically(self, char, pos_x, pos_y):
        if len(self.board[pos_x]) < 4:
            return False
        column = self.board[pos_x]
        if char == column[pos_y-1] == column[pos_y-2] == column[pos_y-3]:
            return True
        return False

    def check_horizontally(self, char, pos_x, pos_y):
        result = False
        for a,b,c in [(-1,-2,-3), (-1,-2,1), (-1,1,2), (1,2,3)]:
            result = result or self.check_horizontally_aux(char, pos_x, pos_y, a, b, c)
        # result = False
        # if pos_x >= 3:
        #     result = result or check_horizontally_aux(self, char, pos_x, pos_y, -1, -2, -3)
        # if pos_x >= 2 and len(self.board)-pos_x >= 1:
        #     result = result or check_horizontally_aux(self, char, pos_x, pos_y, -1, -2, 1)
        # if pos_x >= 1 and len(self.board)-pos_x >= 2:
        #     result = result or check_horizontally_aux(self, char, pos_x, pos_y, -1, 1, 2)
        # if len(self.board)-pos_x >= 3:
        #     result = result or check_horizontally_aux(self, char, pos_x, pos_y, 1, 2, 3)
        return result

    def check_horizontally_aux(self, char, pos_x, pos_y, offset_1, offset_2, offset_3):
        if (pos_x+offset_1 < 0 or pos_x+offset_2 < 0 or pos_x+offset_3 < 0):
            return False
        try:
            if char == self.board[pos_x+offset_1][pos_y] == self.board[pos_x+offset_2][pos_y] == self.board[pos_x+offset_3][pos_y]:
                return True
            return False
        except:
            return False

    def check_identity_diagonal(self, char, pos_x, pos_y):
        result = False
        for a,b,c in [(-1,-2,-3), (-1,-2,1), (-1,1,2), (1,2,3)]:
            result = result or self.check_identity_diagonal_aux(char, pos_x, pos_y, a, b, c)
        return result

    def check_identity_diagonal_aux(self, char, pos_x, pos_y, offset_1, offset_2, offset_3):
        if (pos_x+offset_1 < 0 or pos_x+offset_2 < 0 or pos_x+offset_3 < 0):
            return False
        if (pos_y+offset_1 < 0 or pos_y+offset_2 < 0 or pos_y+offset_3 < 0):
            return False
        try:
            if char == self.board[pos_x+offset_1][pos_y+offset_1] == self.board[pos_x+offset_2][pos_y+offset_2] == self.board[pos_x+offset_3][pos_y+offset_3]:
                return True
            return False
        except:
            return False

    def check_not_identity_diagonal(self, char, pos_x, pos_y):
        result = False
        for a,b,c in [(-1,-2,-3), (-1,-2,1), (-1,1,2), (1,2,3)]:
            result = result or self.check_not_identity_diagonal_aux(char, pos_x, pos_y, a, b, c)
        return result

    def check_not_identity_diagonal_aux(self, char, pos_x, pos_y, offset_1, offset_2, offset_3):
        if (pos_x+offset_1 < 0 or pos_x+offset_2 < 0 or pos_x+offset_3 < 0):
            return False
        if (pos_y-offset_1 < 0 or pos_y-offset_2 < 0 or pos_y-offset_3 < 0):
            return False
        try:
            if char == self.board[pos_x+offset_1][pos_y-offset_1] == self.board[pos_x+offset_2][pos_y-offset_2] == self.board[pos_x+offset_3][pos_y-offset_3]:
                return True
            return False
        except:
            return False

class Player(object):
    def __init__(self):
        self.breed = "human"

    def start_game(self, char, width):
        pass

    def move(self, board, height):
        x = len(board)
        while (x < 0 or x >= len(board) or len(board[x]) >= height):
            i = raw_input("Your move? ")
            if (i):
              try:
                x = int(i)-1
                if (x < 0 or x >= len(board) or len(board[x]) >= height):
                  print u"Número inválido"
              except ValueError:
                print("That's not an int!")
            else:
              print u"Poné un número capo!"
        return x

    def reward(self, value, board, height):
        pass

    def available_moves(self, board, height):
        return [i for i in range(len(board)) if len(board[i]) < height]


class RandomPlayer(Player):
    def __init__(self):
        self.breed = "random"

    def reward(self, value, board, height):
        pass

    def start_game(self, char, width):
        pass

    def move(self, board, height):
        return random.choice(self.available_moves(board,height))

class QLearningPlayer(Player):
    def __init__(self, epsilon=0.2, alpha=0.3, gamma=0.9):
        self.breed = "Qlearner"
        self.q = {} # (state, action) keys: Q values
        self.epsilon = epsilon # e-greedy chance of random exploration
        self.alpha = alpha # learning rate
        self.gamma = gamma # discount factor for future rewards
        self.me = "?"

    def start_game(self, char, width):
        self.last_board = []
        for i in range(width):
            self.last_board.append([])
        self.last_move = None
        self.mm = ""
        self.me = char

    def getQ(self, state, action):
        # encourage exploration; "optimistic" 1.0 initial values
        if self.q.get((state, action)) is None:
            self.q[(state, action)] = 1.0
        return self.q.get((state, action))

    def move(self, board, height):
        self.last_board = board
        self.mm = self.make_matrix(board, height)
        actions = self.available_moves(board, height)

        if random.random() < self.epsilon: # explore!
            self.last_move = random.choice(actions)
            return self.decide()

        qs = [self.getQ(self.mm, a) for a in actions]
        maxQ = max(qs)

        if qs.count(maxQ) > 1:
            # more than 1 best option; choose among them randomly
            best_options = [i for i in range(len(actions)) if qs[i] == maxQ]
            i = random.choice(best_options)
        else:
            i = qs.index(maxQ)

        self.last_move = actions[i]
        return self.decide()

    def decide(self):
        return self.last_move

    def reward(self, value, board, height):
        if self.last_move:
            self.learn(self.last_board, self.last_move, value, board, height)

    def learn(self, state, action, reward, result_state, height):
        prev = self.getQ(self.mm, action)
        if len(self.available_moves(result_state, height)) == 0:
            maxqnew = 0
        else:
            result_mm = self.make_matrix(result_state, height)
            maxqnew = max([self.getQ(result_mm, a) for a in self.available_moves(result_state, height)])
        self.q[(self.mm, action)] = prev + self.alpha * ((reward + self.gamma*maxqnew) - prev)

    def make_matrix(self, board, height):
      m = ""
      for i in board:
        for j in i:
          m += str(j)
        m+=";"
      return m[0:-1]

class QQLearningPlayer(QLearningPlayer):
    def start_game(self, char, width):
        self.last_board = []
        for i in range(width):
            self.last_board.append([])
        self.last_move = None
        self.mm = ""
        self.me = char
        self.myLines = []
        self.enLines = []

    def decide(self):
      try:
        x = int(self.last_move)
        return x
      except ValueError:
        if self.last_move[0] == "M":
          return self.myLines[int(self.last_move[1:])][1]
        else:
          return self.enLines[int(self.last_move[1:])][1]

    def available_moves(self, board, height):
        if (len(self.myLines)==0):
          return [i for i in range(len(board))]
        result = []
        for i in range(len(self.myLines)):
          if self.myLines[i][1] + self.myLines[i][0] < height:
            result.append("M"+str(i))
        for i in range(len(self.enLines)):
          if self.enLines[i][1] + self.enLines[i][0] < height:
            result.append("E"+str(i))
        return result

    def make_matrix(self, board, height):
      myLines = []
      enLines = []
      for j in range(len(board)):
        column = board[j]
        if (len(column) > 0):
          start = column[0]
          line = [1,j,0]
          for i in range(1,len(column)):
            if column[i]==start:
              line[0] += 1
            else:
              line = [1,j,i]
              start = column[i]
          if start==self.me:
            myLines.append(line)
          else:
            enLines.append(line)
      if board==self.last_board:
        self.myLines = myLines
        self.enLines = enLines
      m = ""
      #TODO!
      return m


if __name__ == "__main__":
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    if len(sys.argv) < 3:
        print "Error: expected at least 2 arguments"
        exit()
    print 'Argument List:', str(sys.argv)#p1 = RandomPlayer()
    key1 = sys.argv[1]
    key2 = sys.argv[2]
    if len(sys.argv) < 4:
        iterations = -1
    else:
        iterations = int(sys.argv[3])
    players1 = {'q': QLearningPlayer(), 'r': RandomPlayer(), 'qq':QQLearningPlayer()}
    players2 = {'q': QLearningPlayer(), 'r': RandomPlayer(), 'qq':QQLearningPlayer()}
    p1 = players1[key1] 
    #epsilon, gamma, alpha
    p2 = players2[key2]#QQLearningPlayer(0.9,0.3,0.9)

    size = (6, 7)
    print "#iter", str(iterations)

    f1 = open('A-1('+p1.breed + ')vs2-(' + p2.breed + ').dat','w')
    f2 = open('A-2('+p2.breed + ')vs1-(' + p1.breed + ').dat','w')
    f1.write("")
    f2.write("")

    f1.close()
    f2.close()


    try:
        i=0
        res = ["",""]
        win = [0,0.0,0.0]
        tot = 0
        while (i != iterations):
            t = FourInLine(p1, p2, size[0], size[1])
            winner = t.play_game(False)
            if winner==0:
                self.tot += 1
                res[0] += str(self.tot) + "\t" + str(self.win[1] / self.tot) + "\n"
                res[1] += str(self.tot) + "\t" + str(self.win[2] / self.tot) + "\n"
            else:
                tot += 1
                win[int(winner)] += 1
                res[0] += str(win[1] / tot) + "\n"
                res[1] += str(win[2] / tot) + "\n"
            if i % 1000 == 0:
                print "Entrenando ..." + str(i) + ". Presione Ctrl+C para dejar de entrenar."
                f1 = open('A-1('+p1.breed + ')vs2-(' + p2.breed + ').dat','a')
                f2 = open('A-2('+p2.breed + ')vs1-(' + p1.breed + ').dat','a')
                f1.write(res[0])
                f2.write(res[1])
                f1.close()
                f2.close()
                res = ["",""]
            i += 1
    except KeyboardInterrupt:
        print "\nGuardando jugador entrenado. Espere por favor..."

    if key1 == "q" or key1 == "qq":
        f = open("1-"+key1.upper()+".dic",'wb')
        pickle.dump(p1.q,f)
        f.close()
    if key2 == "q" or key2 == "qq":
        f = open("2-"+key2.upper()+".dic",'wb')
        pickle.dump(p2.q,f)
        f.close()

    print "Listo!"

    #f = open('Q0.dic','rb')
    #p2.q = pickle.load(f)

    p1 = Player()
    #p2 = Player()
    p2.epsilon = 0

    while True:
        t = FourInLine(p1, p2, size[0], size[1])
        t.play_game(True)
