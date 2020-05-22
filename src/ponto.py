from graphics import *

def Ponto(x, y, Xmax, Ymax, cor, tamanho, Win):

    x = x+Xmax/2
    y = Ymax/2 - y

    if tamanho == 1:
        Win.plotPixel(x,y,cor)

    if tamanho == 2:
        Win.plotPixel(x,y,cor)
        Win.plotPixel(x+1,y,cor)
        Win.plotPixel(x,y-1,cor)
        Win.plotPixel(x+1,y-1,cor)

    if tamanho == 3:
        Win.plotPixel(x,y,cor)
        Win.plotPixel(x+1,y,cor)
        Win.plotPixel(x+1,y-1,cor)
        Win.plotPixel(x+1, y+1, cor)
        Win.plotPixel(x,y-1,cor)
        Win.plotPixel(x, y+1, cor)
        Win.plotPixel(x-1,y,cor)
        Win.plotPixel(x-1,y-1,cor)
        Win.plotPixel(x-1,y+1,cor)

        return
