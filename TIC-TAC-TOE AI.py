class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A 3x3 board

    def print_board(self):
        for i in range(0, 9, 3):
            row = [str(i + j) if cell == ' ' else cell for j, cell in enumerate(self.board[i:i+3])]
            print(" | ".join(row))
            if i < 6:
                print("---------")
def play_game():
    game = TicTacToe()
    current_player = 'X'
    
    while True:
        game.print_board()
        if current_player == 'X':
            move = best_move(game.board)
        else:
            move = int(input("Enter your move (0-8): "))
        
        if move < 0 or move > 8 or game.board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        
        game.board[move] = current_player
        winner = check_winner(game.board)
        if winner != ' ':
            game.print_board()
            print(f"{winner} wins!" if winner != 'tie' else "It's a tie!")
            break
        current_player = 'O' if current_player == 'X' else 'X'
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A 3x3 board

    def print_board(self):
        for i in range(0, 9, 3):
            row = [str(i + j) if cell == ' ' else cell for j, cell in enumerate(self.board[i:i+3])]
            print(" | ".join(row))
            if i < 6:
                print("---------")

def minimax(board, depth, is_maximizing):
    scores = {'X': 1, 'O': -1, 'tie': 0}
    winner = check_winner(board)

    if winner != ' ':
        return scores[winner]

    if ' ' not in board:
        return scores['tie']

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def check_winner(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for (a, b, c) in win_conditions:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]
    return ' ' if ' ' in board else 'tie'

def play_game():
    game = TicTacToe()
    current_player = 'X'
    
    while True:
        game.print_board()
        if current_player == 'X':
            move = best_move(game.board)
        else:
            move = int(input("Enter your move (0-8): "))
        
        if move < 0 or move > 8 or game.board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        
        game.board[move] = current_player
        winner = check_winner(game.board)
        if winner != ' ':
            game.print_board()
            print(f"{winner} wins!" if winner != 'tie' else "It's a tie!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
