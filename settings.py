# Game Settings -------
NUM_ROWS = 6
NUM_COLS = 7
CELL_SIZE = 80
BUFFER_AROUND = 20  # The amount of padding outside the game
GAME_WIDTH = NUM_COLS * CELL_SIZE + 2 * BUFFER_AROUND
SIDE_PANEL_WIDTH = 3 * 80 + 2 * 20
TRAINER_WIDTH = GAME_WIDTH + SIDE_PANEL_WIDTH
GAME_HEIGHT = NUM_ROWS * CELL_SIZE + 2 * BUFFER_AROUND
BUBBLE_TEXT_SIZE = (200, 200)
BUBBLE_TEXT_TL_ANCHOR = (GAME_WIDTH + BUFFER_AROUND, 5 * BUFFER_AROUND)
BUBBLE_TEXT_CONTENT_TL_ANCHOR = (BUBBLE_TEXT_TL_ANCHOR[0] + BUFFER_AROUND, BUBBLE_TEXT_TL_ANCHOR[1] + BUFFER_AROUND)
TEXT_SIZE = 15
BUBBLE_TEXT_WRAP = 18
# ----------------------

# Minimax Settings -----
AI_DEPTH = 4
# ----------------------

# Level Selector Settings ---
LEVEL_WIDTH = 120
LEVEL_HEIGHT = 70
# -------------------------

# Color Settings ----------------------
YELLOW_PLAYER_COLOR = (240, 230, 140)
BACKGROUND_COLOR = (81, 81, 81)
LEVEL_COLOR = (130, 130, 130)
# ----------------------

# Debug Settings ----------------------
DEBUG_PRINT_DEPTH_BOARDS = False
DEBUG_KEYBOARD_GET_BOARD_INPS = True
# ----------------------

# Asserts
assert NUM_ROWS > 0 and NUM_COLS > 0 and CELL_SIZE > 0 and BUFFER_AROUND >= 0 and AI_DEPTH > 0
