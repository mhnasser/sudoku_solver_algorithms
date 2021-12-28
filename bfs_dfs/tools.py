import copy
import numpy as np

class Board:
    
    def __init__(self, board: np.ndarray):
        self.board = board
        
    def get_empty(self):
        
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        
        return False
    
    def check_valid(self, n, pos):
        
        # Check row
        for i in range(9):
            if self.board[pos[0]][i] == n and pos[1] != i:
                return False
            
        # Check column
        for i in range(9):
            if self.board[i][pos[1]] == n and pos[0] != i:
                return False
            
        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if self.board[i][j] == n and (i,j) != pos:
                    return False
                
        return True

class Node:
    
    def __init__(self, initial_state: Board):
        self.initial_state = initial_state
        self.children = []
            
    def create_chindren(self):
        pos = self.initial_state.get_empty()
        
        for i in range(1,10):
            state = copy.deepcopy(self.initial_state.board)
            if self.initial_state.check_valid(i, pos):
                state[pos[0]][pos[1]] = i
                self.children.append(state)
        
        if i == 9 and len(self.children) == 0:
            return False
        
        else:
            return True