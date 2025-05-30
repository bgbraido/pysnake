import curses
import time


def game_loop(window):
    window.addstr(f'Aperte alguma tecla para iniciar o jogo...\n')
    while True:
        window.timeout(1000)  # Tempo de espera em milissegundos
        char = window.getch()
        window.clear()
        if char == -1:
            window.addstr(f'Nenhuma tecla pressionada. Pressione uma tecla para continuar...\n')
        else:
            window.addstr(f'Você pressionou: {char}\n')


if __name__ == "__main__":
    curses.wrapper(game_loop)
     