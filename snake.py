import time


def game_loop():
    for i in range(10):
        print(f'O valor de i é: {i}')
        time.sleep(1)  # Pausa de 1 segundo entre iterações


if __name__ == "__main__":
    game_loop()
    