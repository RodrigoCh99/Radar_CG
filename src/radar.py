from graphics import *
from ponto import Ponto

def main():

    # Definindo as confgurações da tela:
    Xmax = 500
    Ymax = 500

    # definção das dores de fundo:
    corFundo = color_rgb(99,33,99)

    # criação da tela em si:
    win = GraphWin("Radar", Xmax, Ymax)
    win.setBackground(corFundo)

    # teste da rotina ponto:
    Ponto(100, 100, Xmax, Ymax, 'red', 3, Win=win)

    # definição da tela como interativa com o mouse
    # fechavel com o botão do canto superior direito:
    win.getMouse()
    win.close()

if __name__ == '__main__':

    main()
