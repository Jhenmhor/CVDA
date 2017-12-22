from termcolor import *


def init():
    height = int(input("Quelle largeur de tableau ?\n"))
    width = int(input("Quelle hauteur de tableau ?\n"))
    tab = []

    for i in range(width):
        tab.append(['O'] * height)

    tab[0][0] = 'X'
    return width, height, tab


def move(width, height, tab, key):
    for i in range(width):
        for j in range(height):
            if tab[i][j] == 'X':
                if key == 'z':
                    tab[i][j] = 'O'
                    tab[i - 1][j] = 'X'
                elif key == 'q':
                    tab[i][j] = 'O'
                    tab[i][j - 1] = 'X'
                elif key == 's':
                    tab[i][j] = 'O'
                    if i != width - 1:
                        tab[i + 1][j] = 'X'
                    else:
                        tab[0][j] = 'X'
                elif key == 'd':
                    tab[i][j] = 'O'
                    if j != height - 1:
                        tab[i][j + 1] = 'X'
                    else:
                        tab[i][0] = 'X'
                return tab


def intelligence_test(nberror):
    if nberror > 5:
        raise StupidError("Stupidity Overflow")
        return -1
    else:
        return nberror

def main():
    width, height, niveau_stupidite = 0, 0, 0
    while (width, height) == (0, 0):
        try:
            width, height, tab = init()
        except:
            print("Stupide Animal")
            niveau_stupidite += 1
            width, height = 0, 0

    key = 't'
    while key != 'e':
        for i in range(width):
            for j in range(height):
                if tab[i][j] == 'X':
                    cprint(tab[i][j], 'red', end="")
                else:
                    print(tab[i][j], end="")
            print('\n')
        while 1:
            key = input("z,q,s,d pour se deplacer ou e pour sortir\n")
            tab = move(width, height, tab, key)
            if key in {'z', 'q', 's', 'd', 'e'}:
                break
            print('Stupide Animal')
            niveau_stupidite += 1

    if intelligence_test(niveau_stupidite) == 0:
        print("Bravo vous n'êtes pas un stupide animal")
    elif intelligence_test(niveau_stupidite) != -1:
        print("Vous êtes un stupide animal de niveau " + str(niveau_stupidite))

    return 0


class StupidError(Exception):
    pass


main()
# augustinchateauricherd@gmail.com
