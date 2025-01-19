from kogi_canvas import play_othello
import random

BLACK = 1
WHITE = 2

# 四隅の座標を定義
CORNERS = [(0, 0), (0, 5), (5, 0), (5, 5)]


def can_place_x_y(board, stone, x, y):
    """
    石を置けるかどうかを調べる関数。
    """
    if board[y][x] != 0:
        return False  # 既に石がある場合は置けない

    opponent = 3 - stone  # 相手の石 (1なら2、2なら1)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        found_opponent = False

        while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == opponent:
            nx += dx
            ny += dy
            found_opponent = True

        if found_opponent and 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == stone:
            return True  # 石を置ける条件を満たす

    return False


def can_place(board, stone):
    """
    石を置ける場所を調べる関数。
    """
    for y in range(len(board)):
        for x in range(len(board[0])):
            if can_place_x_y(board, stone, x, y):
                return True
    return False


def valid_moves(board, stone):
    """
    石を置けるすべての座標をリストで返す。
    """
    moves = []
    for y in range(len(board)):
        for x in range(len(board[0])):
            if can_place_x_y(board, stone, x, y):
                moves.append((x, y))
    return moves


class kerokeroAI(object):
    def face(self):
        return "🦾"  # 強いAIを示すアイコン

    def place(self, board, stone):
        # まず四隅が取れるかチェック
        for corner in CORNERS:
            x, y = corner
            if can_place_x_y(board, stone, x, y):
                return x, y

        # 取れる四隅がない場合、他の有効な手からランダムに選択
        moves = valid_moves(board, stone)
        if moves:
            return random.choice(moves)

        # どこにも置けない場合は(-1, -1)を返す（通常はここに到達しない）
        return -1, -1


# ゲーム実行
play_othello(kerokeroAI())
