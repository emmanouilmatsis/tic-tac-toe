import math

def play(board, player):
    """Play game using minimiax.

    Args:
        board: A list of nine characters where each character is either o, x or space.
        player: A character representing the next player.

    Returns:
        A list of nine characters, same as input board with one o added.

    Raises:
        ValueError: An error accured when board string doesn't represent a valid
            tic tac toe board or if it is not plausibly o's turn.
    """

    if not is_valid(board):
        raise ValueError

    board, _, _ = minimax(board, player, 0)
    return board

def minimax(board, player, k):
    """Minimax reursive algorith to find next move for player on board.

    Args:
        board: A list of nine characters where each character is either o, x or space.
        player: A character representing the next player.

    Returns:
        A tuple of the resulting board and score. The board is a list of nine
        characters, same as input board with one o added. The score is -1, 0 or
        1 depending on the evaluation of the next boards against the player.
    """

    # if board is empty return center opening move.
    if is_empty(board):
        return (f"    {player}    ", 0, k)

    # If board is full or has a winner then evaluate.
    if is_game_over(board):
        return (None, evaluate(winner(board)), k)

    # Generate all possible next moves.
    results = [(move, *minimax(move, "x" if player == "o" else "o", k+1)[1:]) for move in moves(board, player)]

    # Minimaximize.
    if player == "x":
        result = min(results, key=lambda x: (x[1], -x[2]))
    else:
        result = max(results, key=lambda x: (x[1], -x[2]))

    return result

def evaluate(state):
    """Evaluate player labels.

    Args:
        player: A character or None representing the board state.

    Returns:
        A integer mapping to each board state. If x then -1, if o then 1
            else if None then 0.
    """

    return -1 if state == "x" else 1 if state == "o" else 0

def winner(board):
    """Ged the winner if any.

    Args:
        board: A list of nine characters where each character is either o, x or space.

    Returns:
        A character representing the winner of the board or None if no winner.
    """

    is_winner = lambda a: len(set(a)) == 1 and " "not in a

    # Rows
    for i in range(3):
        row = [board[i*3+j] for j in range(3)]
        if is_winner(row):
            return row[0]

    # Columns
    for i in range(3):
        column = [board[i+3*j] for j in range(3)]
        if is_winner(column):
            return column[0]

    # Diagonals
    diagonal = [board[i*2*2] for i in range(3)]
    if is_winner(diagonal):
        return diagonal[0]

    diagonal = [board[i*2+2] for i in range(3)]
    if is_winner(diagonal):
        return diagonal[0]

    return None

def moves(board, player):
    """Generate all possible new boards from board.

    Args:
        board: A list of nine characters where each character is either o, x or space.
        player: A character representing the player.

    Returns:
        A list of boards where each board is a list of nine characters, same as
        input board with the one player character added.
    """

    indices = [i for i, v in enumerate(board) if v == " "]

    moves = []
    for index in indices:
        tmp = board.copy()
        tmp[index] = player
        moves.append(tmp)

    return moves

def is_game_over(board):
    """Test if board is full or has a winner."""

    return is_full(board) or winner(board) is not None

def is_full(board):
    """Test if board is full."""

    return " " not in board

def is_empty(board):
    """Test if board is empty."""

    return len(set(board)) == 1 and " " in board

def is_valid(board):
    """Test if board is valid."""

    # Board string has valid length.
    if len(board) != 9:
        return False

    # Board string has valid characters.
    if not (set(board) <= set("xo ")):
        return False

    # Is o's turn.
    x = board.count("x")
    o = board.count("o")
    if not (x - 1 == o or x == o):
        return False

    # Board is not full.
    if is_full(board):
        return False

    # Board has no winner.
    if winner(board) is not None:
        return False

    return True
