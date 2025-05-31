import curses
import time
import random

def game_loop(window):
    #Initial setup
    curses.curs_set(0) #hidden cursor
    snake = [
        [10, 15],
        [9, 15],
        [8, 15],
        [7, 15],

    ]  # Initial position of the snake
    fruit = get_new_fruit(window=window)
    current_direction = curses.KEY_DOWN  # Initial direction
    snake_ate_fruit = False

    while True:
        draw_screen(window=window)
        draw_snake(snake=snake, window=window)
        draw_actor(actor=fruit, window=window, char=curses.ACS_DIAMOND)
        direction = get_new_direction(window=window, timeout=1000)
        if direction is None:
            direction = current_direction
        if direction_is_opposite(direction=direction, current_direction=current_direction):
            direction = current_direction
        move_snake(snake=snake, direction=direction, snake_ate_fruit=snake_ate_fruit)
        if snake_hit_border(snake=snake, window=window):
            return
        if snake_hit_itself(snake=snake):
            return
        if snake_hit_fruit(snake=snake, fruit=fruit):
            snake_ate_fruit = True
            fruit = get_new_fruit(window=window)
        else:
            snake_ate_fruit = False         
        current_direction = direction


def direction_is_opposite(direction, current_direction):
    match direction:
        case curses.KEY_UP:
            return current_direction == curses.KEY_DOWN
        case curses.KEY_LEFT:
            return current_direction == curses.KEY_RIGHT
        case curses.KEY_DOWN:
            return current_direction == curses.KEY_UP
        case curses.KEY_RIGHT:
            return current_direction == curses.KEY_LEFT


def get_new_fruit(window):
    height, width = window.getmaxyx() #get height and width of the window
    return [random.randint(1, height-2), random.randint(1, width-2)]


def snake_hit_border(snake, window):
    head = snake[0]  # Get the head of the snake
    return actor_hit_border(actor=head, window=window)  # Check if the head hits the border


def snake_hit_fruit(snake, fruit):
    return fruit in snake # It will check if fruit belong to snake list


def snake_hit_itself(snake):
    head = snake[0]
    body = snake[1:]
    return head in body


def draw_screen(window):
    window.clear()
    window.border(0)  # Draw border


def draw_snake(snake, window):
    head = snake[0]
    draw_actor(actor=head, window=window, char='@')  # Draw the head of the snake
    body = snake[1:]  # Get the body of the snake
    for body_part in body:
        draw_actor(actor=body_part, window=window, char='s')


def draw_actor(actor, window, char):
    window.addch(actor[0], actor[1], char)  # Draw the actor at its position
        

def get_new_direction(window, timeout):
    window.timeout(timeout)  # Set the timeout for key input
    direction = window.getch()  # Get the key pressed
    if direction in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
        return direction
    return None


def move_snake(snake, direction, snake_ate_fruit):
    head = snake[0].copy()  # Copy the head of the snake
    move_actor(actor=head, direction=direction)  # Move the head in the specified direction    
    snake.insert(0, head)  # Insert the new head at the beginning of the snake
    if not snake_ate_fruit:
        snake.pop()  # Remove the last segment of the snake to keep its length constant


def move_actor(actor, direction):
    match direction:
        case curses.KEY_UP:
            actor[0] -= 1
        case curses.KEY_LEFT:
            actor[1] -= 1
        case curses.KEY_DOWN:
            actor[0] += 1
        case curses.KEY_RIGHT:
            actor[1] += 1


def actor_hit_border(actor, window):
    height, width = window.getmaxyx() #get height and width of the window
    if (actor[0] <= 0) or (actor[0] >= height - 1):
        return True
    if (actor[1] <= 0) or (actor[1] >= width - 1):
        return True
    return False
    

if __name__ == "__main__":
    curses.wrapper(game_loop)
    print ("Game Over!")  # Print Game Over message after exiting the game loop
     