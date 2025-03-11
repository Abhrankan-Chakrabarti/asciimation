import time

with open('asciimation/film.js', encoding='Latin-1') as f:
    exec(f.read()[4:])  

for i in range(0, len(film) - 2, 14):
    print('\n'.join(line.ljust(79) for line in film[i + 1:i + 14]))
    time.sleep(int(film[i]) / 15)
    print('\033[H', end='')
