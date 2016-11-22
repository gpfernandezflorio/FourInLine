#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import cPickle as pickle
import sys
import signal
import os.path

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

def board_full(board, height):
    return not any([len(column) < height for column in board])

def board_empty(board):
    return all([len(column) == 0 for column in board])

def player_wins(char, column, board):
    pos_y = len(board[column])-1
    pos_x = column
    if(check_vertically(char, pos_x, pos_y, board)):
        return True
    if(check_horizontally(char, pos_x, pos_y, board)):
        return True
    if(check_identity_diagonal(char, pos_x, pos_y, board)):
        return True
    if(check_not_identity_diagonal(char, pos_x, pos_y, board)):
        return True
    return False

def check_vertically(char, pos_x, pos_y, board):
    if len(board[pos_x]) < 4:
        return False
    column = board[pos_x]
    if char == column[pos_y-1] == column[pos_y-2] == column[pos_y-3]:
        return True
    return False

def check_horizontally(char, pos_x, pos_y, board):
    result = False
    for a,b,c in [(-1,-2,-3), (-1,-2,1), (-1,1,2), (1,2,3)]:
        result = result or check_horizontally_aux(char, pos_x, pos_y, a, b, c, board)
    return result

def check_horizontally_aux(char, pos_x, pos_y, offset_1, offset_2, offset_3, board):
    if (pos_x+offset_1 < 0 or pos_x+offset_2 < 0 or pos_x+offset_3 < 0):
        return False
    try:
        if char == board[pos_x+offset_1][pos_y] == board[pos_x+offset_2][pos_y] == board[pos_x+offset_3][pos_y]:
            return True
        return False
    except:
        return False

def check_identity_diagonal(char, pos_x, pos_y, board):
    result = False
    for a,b,c in [(-1,-2,-3), (-1,-2,1), (-1,1,2), (1,2,3)]:
        result = result or check_identity_diagonal_aux(char, pos_x, pos_y, a, b, c, board)
    return result

def check_identity_diagonal_aux(char, pos_x, pos_y, offset_1, offset_2, offset_3, board):
    if (pos_x+offset_1 < 0 or pos_x+offset_2 < 0 or pos_x+offset_3 < 0):
        return False
    if (pos_y+offset_1 < 0 or pos_y+offset_2 < 0 or pos_y+offset_3 < 0):
        return False
    try:
        if char == board[pos_x+offset_1][pos_y+offset_1] == board[pos_x+offset_2][pos_y+offset_2] == board[pos_x+offset_3][pos_y+offset_3]:
            return True
        return False
    except:
        return False

def check_not_identity_diagonal(char, pos_x, pos_y, board):
    result = False
    for a,b,c in [(-1,-2,-3), (-1,-2,1), (-1,1,2), (1,2,3)]:
        result = result or check_not_identity_diagonal_aux(char, pos_x, pos_y, a, b, c, board)
    return result

def check_not_identity_diagonal_aux(char, pos_x, pos_y, offset_1, offset_2, offset_3, board):
    if (pos_x+offset_1 < 0 or pos_x+offset_2 < 0 or pos_x+offset_3 < 0):
        return False
    if (pos_y-offset_1 < 0 or pos_y-offset_2 < 0 or pos_y-offset_3 < 0):
        return False
    try:
        if char == board[pos_x+offset_1][pos_y-offset_1] == board[pos_x+offset_2][pos_y-offset_2] == board[pos_x+offset_3][pos_y-offset_3]:
            return True
        return False
    except:
        return False

class FourInLine:
    def __init__(self, player1, player2, width, height):
        self.height = height
        self.board = []
        for i in range(width):
            self.board.append([])
        self.red, self.blue = player1, player2
        self.turn = random.choice(['1', '2'])
        #self.turn = '1'
        self.rWin = 1
        self.rLoss = -1
        self.rTie = 0.5
        self.rTurn = 0

    def set_reward_win(self, x):
        self.rWin = x
    def set_reward_loss(self, x):
        self.rLoss = x
    def set_reward_tie(self, x):
        self.rTie = x
    def set_reward_turn(self, x):
        self.rTurn = x

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
            if player_wins(char,column, self.board):
                player.reward(self.rWin, self.board, self.height)
                other_player.reward(self.rLoss, self.board,self.height)
                if play:
                    display_board(self.board, self.height)
                    print "Jugador " + self.turn + " GANA! (" + player.breed + ")"
                return self.turn
            if board_full(self.board, self.height): # tie game
                player.reward(self.rTie, self.board, self.height)
                other_player.reward(self.rTie, self.board,self.height)
                if play:
                    display_board(self.board, self.height)
                    print "EMPATE!"
                return "0"
            other_player.reward(self.rTurn, self.board,self.height)
            if self.turn == '1':
                self.turn = '2'
            else:
                self.turn = '1'

class Player(object):
    def __init__(self):
        self.breed = "human"

    def start_game(self, char, width):
        pass
    def set_epsilon(self, e):
        pass
    def set_gamma(self, g):
        pass
    def set_alpha(self, a):
        pass
    def other(self, char):
        return '1' if char == '2' else '2'

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
    def __init__(self, epsilon=0.2, alpha=0.3, gamma=0.9): #epsilon=0.2, alpha=0.3, gamma=0.9
        self.breed = "Qlearner"
        self.q = {} # (state, action) keys: Q values
        self.epsilon = epsilon # e-greedy chance of random exploration
        self.alpha = alpha # learning rate
        self.gamma = gamma # discount factor for future rewards
        self.me = "?"
    def set_epsilon(self, e):
        self.epsilon = e
    def set_gamma(self, g):
        self.gamma = g
    def set_alpha(self, a):
        self.alpha = a

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

class SmartQLearningPlayer(QLearningPlayer):
    def __init__(self, epsilon=0.2, alpha=0.3, gamma=0.9): #epsilon=0.2, alpha=0.3, gamma=0.9
        self.breed = "SmartQlearner"
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
        self.enemy = self.other(char)

    def move(self, board, height):
        self.last_board = board
        self.mm = self.make_matrix(board, height)
        actions = self.available_moves(board, height)

        for a in actions:
            board[a].append(self.me)
            if player_wins(self.me, a, board):
                board[a].pop()
#                print "Voy a ganar si pongo en " + str(a+1)
                return a
            board[a].pop()
        for a in actions:
            board[a].append(self.enemy)
            if player_wins(self.enemy, a, board):
                board[a].pop()
#                print "Voy a perder si no pongo en " + str(a+1)
                return a
            board[a].pop()

        #RABDOM!
        self.last_move = random.choice(actions)
        return self.decide()

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


class MinimaxPlayer(Player):
    def __init__(self):
        self.breed = "minimax"
        self.best_moves = {}

    def start_game(self, char, width):
        self.me = char
        self.enemy = self.other(char)

    def move(self, board, height):
        # print board
        asd = tuple([tuple(column) for column in board])
        if asd in self.best_moves:
            return random.choice(self.best_moves[asd])
        if board_empty(board):
            return len(board)/2
        best_yet = -2
        choices = []
        for move in self.available_moves(board, height):
            board[move].append(self.me)
            optimal = self.minimax(board, self.enemy, -2, 2, move, height)
            board[move].pop()
            if optimal > best_yet:
                choices = [move]
                best_yet = optimal
            elif optimal == best_yet:
                choices.append(move)
        self.best_moves[asd] = choices
        return random.choice(choices)

    def minimax(self, board, char, alpha, beta, column, height):
        # print alpha
        # print beta
        if player_wins(self.me, column, board):
            return 1
        if player_wins(self.enemy, column, board):
            return -1
        if board_full(board, height):
            return 0
        # print self.available_moves(board, height)
        for move in self.available_moves(board, height):
            board[move].append(char)
            val = self.minimax(board, self.other(char), alpha, beta, column, height)
            board[move].pop()
            if char == self.me:
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        if char == self.me:
            return alpha
        else:
            return beta

    def reward(self, value, board, height):
        pass

p1 = None
p2 = None
key1 = '-'
key2 = '-'

to_save = False


def save_player(key,player,whichplayer,other):
    if key == "q" or key == "s":
        print "Guardando el modelo entrenado de " + whichplayer + ". Espere por favor..."
        f = open(key.upper()+whichplayer+"vs"+other+".dic",'wb')
        pickle.dump(player.q,f,2)
        f.close()
    elif os.path.isfile(key):
        print "Guardando el modelo entrenado de " + whichplayer + ". Espere por favor..."
        f = open(key,'wb')
        pickle.dump(player.q,f,2)
        f.close()

def load_player(key,players):
    if key in ('q','r','s','h','m'):
        player = players[key]
    elif os.path.isfile(key):
        print "Cargando el modelo entrenado de " + key + ". Espere por favor..."
        player = players[key[0].lower()]
        f = open(key,'rb')
        player.q = pickle.load(f)
        f.close()
    else:
        print "error: parámetro " + key + " inválido"
        exit()
    return player

def save_players(x):
    save_player(key1,p1,"1",p2.breed)
    save_player(key2,p2,"2",p1.breed)
    print "Listo!"
    f = open('done.txt','w')
    f.write('done '+str(x)+'\n')
    f.close()

def save_train_data(res,m):
    f1 = open('A-1('+p1.breed + ')vs2-(' + p2.breed + ').dat',m)
    f2 = open('A-2('+p2.breed + ')vs1-(' + p1.breed + ').dat',m)
    f1.write(res[0])
    f2.write(res[1])
    f1.close()
    f2.close()

def signal_handler(signal, frame):
    global to_save
    print "SIGNAL RECIEVED!"
    to_save = True

if __name__ == "__main__":
    print 'Number of arguments:', (len(sys.argv)-1), 'arguments.'
    if len(sys.argv) < 3:
        print "Error: expected at least 2 arguments"
        exit()
    print 'Argument List:', str(sys.argv)
    modo = sys.argv[1]
    if modo == 'p':
        #MODO PARÁMETROS
        if len(sys.argv) < 14:
            print "Error: expected at least 14 arguments"
            print "Modo de Uso: python fourInLine.py p k1 k2 alpha1 gamma1 epsilon1 alpha2 gamma2 epsilon2 win tie loss turn saveDict [iterations]"
            exit()
        key1 = sys.argv[2]
        key2 = sys.argv[3]
        if len(sys.argv) < 16:
            iterations = -1
        else:
            iterations = int(sys.argv[15])
    else:
        key1 = sys.argv[1]
        key2 = sys.argv[2]
        if len(sys.argv) < 4:
            iterations = -1
        else:
            iterations = int(sys.argv[3])

    players1 = {'q': QLearningPlayer(), 'r': RandomPlayer(), 's':SmartQLearningPlayer(), 'h':Player(), 'm':MinimaxPlayer()}
    players2 = {'q': QLearningPlayer(), 'r': RandomPlayer(), 's':SmartQLearningPlayer(), 'h':Player(), 'm':MinimaxPlayer()}

    p1 = load_player(key1,players1)
    p2 = load_player(key2,players2)

    if modo == 'p':
        p1.set_alpha(float(sys.argv[4]))
        print "Alpha Jugador 1",sys.argv[4]
        p1.set_gamma(float(sys.argv[5]))
        print "Gamma Jugador 1",sys.argv[5]
        p1.set_epsilon(float(sys.argv[6]))
        print "Epsilon Jugador 1",sys.argv[6]
        p2.set_alpha(float(sys.argv[7]))
        print "Alpha Jugador 2",sys.argv[7]
        p2.set_gamma(float(sys.argv[8]))
        print "Gamma Jugador 2",sys.argv[8]
        p2.set_epsilon(float(sys.argv[9]))
        print "Epsilon Jugador 2",sys.argv[9]
        print "Reward Win",sys.argv[10]
        print "Reward Tie",sys.argv[11]
        print "Reward Loss",sys.argv[12]
        print "Reward Turn",sys.argv[13]

    if p1.breed == "human" or p2.breed == "human":
        train_or_play =  "play"
    else:
        train_or_play =  "train"
        print "#iter", str(iterations)

    #size = (4, 4)
    size = (7, 6)

    if train_or_play == 'train':
        save_train_data(["0\t0\n","0\t0\n"],'w')
        res = ["",""]
        win = [0,0.0,0.0]
        tot = 0
        c1 = 1
        c2 = 100
        k = 0
        signal.signal(signal.SIGINT, signal_handler)
        while (tot != iterations):
            if to_save:
              save_players(tot)
              to_save = False
            k+=1
            t = FourInLine(p1, p2, size[0], size[1])
            if modo == 'p':
                t.set_reward_win(float(sys.argv[10]))
                t.set_reward_tie(float(sys.argv[11]))
                t.set_reward_loss(float(sys.argv[12]))
                t.set_reward_turn(float(sys.argv[13]))
            winner = t.play_game(False)
            tot += 1
            if winner!=0:
                win[int(winner)] += 1
            if k==c1:
                res[0] += str(tot) + "\t" + str(win[1] / tot) + "\n"
                res[1] += str(tot) + "\t" + str(win[2] / tot) + "\n"
                k = 0
            if tot >= c2:
                c2*=10
                c1*=10
            if tot % 1000 == 0:
                print "Entrenando ..." + str(tot)
                if tot % 50000 == 0:
                  save_train_data(res,'a')
                  res = ["",""]

        save_train_data(res,'a')
        if modo == 'p':
            if (sys.argv[14]=="1"):
                save_player(key1,p1,"1",p2.breed)
        else:
            save_players(tot)

    else:
        print "A jugar"
        p1.set_epsilon(0.0)
        p2.set_epsilon(0.0)
        try:
            while True:
                t = FourInLine(p1, p2, size[0], size[1])
                t.play_game(True)
        except KeyboardInterrupt:
            print "\nChau!..."
