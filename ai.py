import numpy as np

# ボードサイズ
BOARD_SIZE = 6

# ボードの初期配置
def create_initial_board():
    board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
    mid = BOARD_SIZE // 2
    board[mid-1][mid-1] = board[mid][mid] = 1
    board[mid-1][mid] = board[mid][mid-1] = -1
    return board

# 方向のリスト
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# 角の位置
CORNERS = [(0, 0), (0, BOARD_SIZE-1), (BOARD_SIZE-1, 0), (BOARD_SIZE-1, BOARD_SIZE-1)]

# ボードの表示
def display_board(board):
    for row in board:
        print(' '.join(['.' if x == 0 else 'O' if x == 1 else 'X' for x in row]))
    print()

# 石を置けるか判定
def is_valid_move(board, row, col, player):
    if board[row][col] != 0:
        return False
    opponent = -player
    for dr, dc in DIRECTIONS:
        r, c = row + dr, col + dc
        if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == opponent:
            while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
                r += dr
                c += dc
                if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
                    return True
                if r < 0 or r >= BOARD_SIZE or c < 0 or c >= BOARD_SIZE or board[r][c] == 0:
                    break
    return False

# すべての有効な動きを取得
def get_valid_moves(board, player):
    valid_moves = []
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if is_valid_move(board, row, col, player):
                valid_moves.append((row, col))
    return valid_moves

# 石を置く
def place_move(board, row, col, player):
    board[row][col] = player
    opponent = -player
    for dr, dc in DIRECTIONS:
        r, c = row + dr, col + dc
        flip_positions = []
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == opponent:
            flip_positions.append((r, c))
            r += dr
            c += dc
        if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
            for fr, fc in flip_positions:
                board[fr][fc] = player

# ゲームの終了判定
def is_game_over(board):
    return not get_valid_moves(board, 1) and not get_valid_moves(board, -1)

# 勝者の判定
def get_winner(board):
    player1_score = np.sum(board == 1)
    player2_score = np.sum(board == -1)
    if player1_score > player2_score:
        return 1
    elif player2_score > player1_score:
        return -1
    else:
        return 0

# AIの動き選択
def choose_ai_move(valid_moves):
    # 角を優先
    for move in valid_moves:
        if move in CORNERS:
            return move
    # ランダムな動きを選択
    return valid_moves[np.random.randint(len(valid_moves))]

# メインゲームループ
def main():
    board = create_initial_board()
    current_player = 1
    while not is_game_over(board):
        display_board(board)
        valid_moves = get_valid_moves(board, current_player)
        if valid_moves:
            if current_player == 1:
                # プレイヤー1の動き（AI）
                row, col = choose_ai_move(valid_moves)
            else:
                # プレイヤー2の動き（ランダムAI）
                row, col = valid_moves[np.random.randint(len(valid_moves))]
            place_move(board, row, col, current_player)
        current_player = -current_player
    display_board(board)
    winner = get_winner(board)
    if winner == 1:
        print("Player 1 (O) wins!")
    elif winner == -1:
        print("Player 2 (X) wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
