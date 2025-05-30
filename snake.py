import curses
import time


def game_loop(window):
    window.addstr(f'Aperte alguma tecla para iniciar o jogo...')
    while True:
        window.timeout(1000)  # Tempo de espera em milissegundos
        char = window.getch()
        window.clear()
        match char:
            case curses.KEY_UP:
                window.addstr('Mover para cima')
            case curses.KEY_DOWN:
                window.addstr('Mover para baixo')
            case curses.KEY_LEFT:
                window.addstr('Mover para esquerda')
            case curses.KEY_RIGHT:
                window.addstr('Mover para direita')
            case _:
                window.addstr(f'Não mover')

if __name__ == "__main__":
    curses.wrapper(game_loop)
     