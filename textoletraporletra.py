import time

def print_rpg(texto, delay=0.1):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(delay)
    print()

print_rpg("e é assim que eu fiz um texto aparecer letra  por letra")
