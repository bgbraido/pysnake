import curses
import time


def game_loop(window):
    #Initial setup
    curses.curs_set(0) #hidden cursor
    personagem = [10, 15]

    while True:
        draw_screen(window=window)
        draw_actor(actor=personagem, window=window)
        direction = get_new_direction(window=window, timeout=1000)
        if direction is not None:
            move_actor(actor=personagem, direction=direction)
        if actor_hit_border(actor=personagem, window=window):
            return
        

def draw_screen(window):
    window.clear()
    window.border(0)  # Draw border


def draw_actor(actor, window):
    window.addch(actor[0], actor[1], curses.ACS_DIAMOND)  # Draw the actor at its position
        

def get_new_direction(window, timeout):
    window.timeout(timeout)  # Set the timeout for key input
    direction = window.getch()  # Get the key pressed
    if direction in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
        return direction
    return None


def move_actor(actor, direction):
    match direction:
        case curses.KEY_UP:
            actor[0] -= 1
        case curses.KEY_DOWN:
            actor[0] += 1
        case curses.KEY_LEFT:
            actor[1] -= 1
        case curses.KEY_RIGHT:
            actor[1] += 1


def actor_hit_border(actor, window):
    height, width = window.getmaxyx() #get height and width of the window
    if (actor[0] <= 0 or actor[0] >= height - 1):
        return True
    if (actor[1] <= 0 or actor[0] >= width - 1):
        return True
    return False
    

if __name__ == "__main__":
    curses.wrapper(game_loop)
    print ("Game Over!")  # Print Game Over message after exiting the game loop
     