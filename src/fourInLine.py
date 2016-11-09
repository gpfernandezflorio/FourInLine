#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def make_matrix(board, height):
  m = ""
  for i in board:
    for j in i:
      m += str(j)
    m+=";"
  

class FourInLine:
    def __init__(self, playerX, playerO, width, height):
        self.height = height
        self.board = []
        for i in range(width):
            self.board.append([])
        self.red, self.blue = playerX, playerO
        self.turn = random.choice(['B', 'Y'])

    def play_game(self):
        self.red.start_game('Y',len(self.board))
        self.blue.start_game('B',len(self.board))
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
                player.reward(1, self.board,self.height)
                other_player.reward(-1, self.board,self.height)
                break
            if self.board_full(): # tie game
                player.reward(0.5, self.board,self.height)
                other_player.reward(0.5, self.board,self.height)
                break
            other_player.reward(0, self.board,self.height)
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

    def start_game(self, char, width):
        print "\nNew game!"

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
        print "{} rewarded: {}".format(self.breed, value)

    def available_moves(self, board, height):
        return [i for i in range(len(board)) if len(board[i]) < height]


class RandomPlayer(Player):
    def __init__(self):
        self.breed = "random"

    def reward(self, value, board, height):
        pass

    def start_game(self, char):
        pass

    def move(self, board, height):
        return random.choice(self.available_moves(board,height))

class QLearningPlayer(Player):
    def __init__(self, epsilon=0.2, alpha=0.3, gamma=0.9):
        self.breed = "Qlearner"
        self.harm_humans = False
        self.q = {} # (state, action) keys: Q values
        self.epsilon = epsilon # e-greedy chance of random exploration
        self.alpha = alpha # learning rate
        self.gamma = gamma # discount factor for future rewards

    def start_game(self, char, width):
        self.last_board = []
        for i in range(width):
            self.last_board.append([])
        self.last_move = None

    def getQ(self, state, action):
        # encourage exploration; "optimistic" 1.0 initial values
        if self.q.get((state, action)) is None:
            self.q[(state, action)] = 1.0
        return self.q.get((state, action))

    def move(self, board, height):
        self.last_board = make_matrix(board, height)
        actions = self.available_moves(board, height)

        if random.random() < self.epsilon: # explore!
            self.last_move = random.choice(actions)
            return self.last_move

        qs = [self.getQ(self.last_board, a) for a in actions]
        maxQ = max(qs)

        if qs.count(maxQ) > 1:
            # more than 1 best option; choose among them randomly
            best_options = [i for i in range(len(actions)) if qs[i] == maxQ]
            i = random.choice(best_options)
        else:
            i = qs.index(maxQ)

        self.last_move = actions[i]
        return actions[i]

    def reward(self, value, board, height):
        if self.last_move:
            self.learn(self.last_board, self.last_move, value, board, height)

    def learn(self, state, action, reward, result_state, height):
        prev = self.getQ(state, action)
        maxqnew = max([self.getQ(make_matrix(result_state, height), a) for a in self.available_moves(result_state,height)])
        self.q[(state, action)] = prev + self.alpha * ((reward + self.gamma*maxqnew) - prev)

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
p2 = QLearningPlayer()

while True:
    t = FourInLine(p1, p2, 9, 12)
    t.play_game()
