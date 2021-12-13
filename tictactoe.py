  
"""
Tic Tac Toe Player
"""

import math
import copy
import time

X="X"
O ="O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    coux=0 
    couo=0   
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                coux+=1  
            elif board[i][j]==O:
                couo+=1    
    if coux>couo:
        return O
    elif coux==couo:
        return X    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    sett=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                sett.add((i,j))
    return sett            


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action==None:
        return None
    bc=copy.deepcopy(board)
    if bc[action[0]][action[1]]==X or bc[action[0]][action[1]]==O:
        raise Exception
    h=player(bc)
    if h==X:
        bc[action[0]][action[1]]=X
    elif h==O:
        bc[action[0]][action[1]]=O
    return bc    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    counthx=0
    countho=0
    countvx=0
    countvo=0
    countdx=0
    countdo=0
    countd2x=0
    countd2o=0
    countxx=0
    # for testing horizontally
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
               counthx+=1
            elif board[i][j]==O:
                countho+=1  
            if board[j][i]==O:
                countvo+=1
            elif board[j][i]==X:
                countvx+=1
            if i==j:
                if board[i][j]==X:
                    countdx+=1
                elif board[i][j]==O:
                    countdo+=1            
            if i==0 and j==2:
                if board[i][j]==X:
                    countd2x+=1
                elif board[i][j]==O: 
                    countd2o+=1   
            elif i==1 and j==1:
                if board[i][j]==X:
                    countd2x+=1
                elif board[i][j]==O: 
                    countd2o+=1 
            elif i==2 and j==0: 
                if board[i][j]==X:
                    countd2x+=1
                elif board[i][j]==O: 
                    countd2o+=1   
        if counthx==3:
            return X
        elif countho==3:
            return O
        elif countvo==3:
            return O
        elif countvx==3:
            return X       
        elif countdo==3:
            return O
        elif countdx==3:
            return X 
        elif countd2o==3:
            return O
        elif countd2x==3:
            return X                 
        else:    
            countxx+=1
        counthx=0
        countho=0
        countvo=0
        countvx=0    
    if countxx==3:        
        return None
    else:
        return None    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    cp=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==X or board[i][j]==O:
                cp+=1
    if cp==9:
        return True            
    k=winner(board)
    if k==X or k==O :
        return True
    if k==None:
        return False        

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    p=winner(board)
    if p==X:
        return 1
    elif p==O:
        return -1
    cpo=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==X or board[i][j]==O:
                cpo+=1
    if cpo==9:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board)==X:
            t=0
            mv=-math.inf
            for action in actions(board):
                st=time.perf_counter()
                x=minvalue(result(board,action))
                et=time.perf_counter()
                at=(et-st)
                print(action)
                print(x)
                print(at)
                if mv<1 and x>1:
                    mv=math.inf
                    sa=action
                    t=at
                    continue
                elif mv<1 and x==1:
                    mv=1
                    sa=action
                    t=at
                    continue
                elif mv==-1 and x==0:
                    mv=0
                    sa=action
                    t=at
                    continue
                if max(mv,x)==x:
                    if at>t:
                        mv=x
                        sa=action
                        t=at
            return sa

    elif player(board)==O:
            t2=0
            mv2=math.inf
            for action in actions(board):
                st2=time.perf_counter()
                y=maxvalue(result(board,action))
                ed2=time.perf_counter()
                at2=ed2-st2
                print(action)
                print(y)
                print(at2)
                if mv2>-1 and y<-1:
                    mv2=-math.inf
                    sa2=action
                    t2=at2
                    continue
                elif mv2>-1 and y==-1:
                    mv2=-1
                    sa2=action
                    t2=at2
                    continue
                elif mv2==1 and y==0:
                    mv2=0
                    sa2=action
                    t2=at2
                    continue
                if min(mv2,y)==y:
                    if at2>t2:    
                        mv2=y
                        sa2=action
                        t2=at2
            
            return sa2                     
    

def maxvalue(board):
    if terminal(board):
        return utility(board)
    v=-math.inf
    for action in actions(board):    
        v=max(v,minvalue(result(board,action)))
    return v        

def minvalue(board):
    if terminal(board):
        return utility(board)
    v=math.inf
    for action in actions(board):
        v=min(v,maxvalue(result(board,action)))
    return v   