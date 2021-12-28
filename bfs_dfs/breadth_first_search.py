import numpy as np
from tools import Board, Node
from datetime import datetime

with open(r'..\unsolved_sudoku_samples\top50.txt','r') as amostras:
    amostra = amostras.read()
    
amostra1 = [int(x) for x in amostra[0:81].replace('.','0')]
sudoku = np.reshape(amostra1, (-1,9))

def BSF(sudoku: np.ndarray):
    
    queue = []
    start_state = Node(Board(sudoku))

    start_state.create_chindren()
    
    for parent_node in start_state.children:

        queue.append(parent_node)
    while len(queue) != 0:
        
        state = Node(Board(queue[0]))
        queue.pop(0)
      
        if not state.initial_state.get_empty():
            print('Found the solution!')
            print(state.initial_state.board)
            return True
        
        if state.create_chindren():
            for child in state.children:
                queue.append(child)
                
    print("Solution not found")
    return False

if __name__ == "__main__":
    
    print('Problema:\n')
    print(sudoku)
    print("\nResolvendo...\n")
    start = datetime.now()
    BSF(sudoku)
    end = datetime.now()
    print("\nTempos decorrido: ",end - start)