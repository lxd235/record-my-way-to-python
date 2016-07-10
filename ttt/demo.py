# coding:utf-8

def drawBoard(board):    
    # "board" is a list of 10 strings representing the board (ignore index 0)
    blank_board = '|     '*3+'|'
    edge_board = '+-----'*3+'+'
    def drawLine(board_line):
        insert_sym = '|'
        print blank_board
        print "|%3s%3s%3s%3s%3s  |"%(board_line[0],insert_sym,board_line[1],insert_sym,board_line[2])
        print blank_board
        print edge_board
        
    print edge_board
    drawLine(board[7:10])
    drawLine(board[4:7])
    drawLine(board[1:4])



