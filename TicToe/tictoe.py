import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("X O Game")
WHITE = (255,255,255)
BLACK = (0,0,0)
size = 200
board = [
    ["","",""],
    ["","",""],
    ["","",""]
        ]
player = "X"
font = pygame.font.Font(None,100)
run = True

def draw_board():
    screen.fill(WHITE)
    # Draw grid lines
    pygame.draw.line(screen, BLACK, (200,0), (200,600), 5)
    pygame.draw.line(screen, BLACK, (400,0), (400,600), 5)
    pygame.draw.line(screen, BLACK, (0,200), (600,200), 5)
    pygame.draw.line(screen, BLACK, (0,400), (600,400), 5)

    # Draw X and O
    for r in range(3):
        for c in range(3):
            if board[r][c] != "":
                text = font.render(board[r][c], True, BLACK)
                screen.blit(text, (c*200 + 70, r*200 + 50))

def check_winner():
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]

    # Columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != "":
            return board[0][c]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[1][1]

    return None

def is_draw():
    for row in board:
        if "" in row:
            return False
    return True

winner = None

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and winner is None:
            x, y = pygame.mouse.get_pos()
            col = x // size
            row = y // size

            if board[row][col] == "":
                board[row][col] = player
                winner = check_winner()

                if not winner:
                    if is_draw():
                        winner = "Draw"
                    else:
                        player = "O" if player == "X" else "X"

    draw_board()

    if winner:
        msg = f"{winner} Wins!" if winner != "Draw" else "It's a Draw!"
        text = font.render(msg, True, BLACK)
        screen.blit(text, (220, 280))

    pygame.display.update()

pygame.quit()