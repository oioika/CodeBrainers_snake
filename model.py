import random

def initialize_board():
    _board = {}
    for x in range(20):
        for y in range(20):
            _board[(x,y)] = None

    return _board

def initialize_snake(_board):
    _snake = [(random.randint(8,12), random.randint(8,12))]
    print(_snake[0])
    _board[_snake[0]] = "SnakeHead"
    return _snake

def initialize_apple(_board):
    apple = (random.randint(0, 19), random.randint(0, 19))
    while _board[apple] is not None:
        apple = (random.randint(0, 19), random.randint(0, 19))
    _board[apple] = "Apple"
    return apple

def game_over(board, coordinate):
    if 0 > coordinate[0] or coordinate[0] > 19 or 0 > coordinate[1] or coordinate[1] > 19 or board[coordinate] == "SnakeHead":
        exit(2)

def move_tail(snake):
    return snake[:-1]

def set_new_position(direction, snake, board):
    move_tail(snake)
    head_x, head_y = snake[0]
    board[(head_x, head_y)] = None
    if direction == 0:
        head_y = head_y - 1
    if direction == 1:
        head_x = head_x + 1
    if direction == 2:
        head_y = head_y + 1
    if direction == 3:
        head_x = head_x - 1
    game_over(board, coordinate = (head_x, head_y))
    board[(head_x, head_y)] = "SnakeHead"
    snake = [(head_x, head_y)] + move_tail(snake)
    for elem in snake:
        board[elem] = "SnakeHead"

    return snake

def eat_apple(board, snake, apple):
    if snake[0] == apple:
        snake.append(apple)
        return initialize_apple(board)
    return apple
