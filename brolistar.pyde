#Brólistar - A estrelinha briguenta
from mapa import *

def setup():
    global mapa, player
    mapa = Mapa() 
    size(300,300, P3D)
    player = mapa.addPersonagem('link')
    
def draw():
    cx, cy = cameraMov(player.x, player.y, mapa.largura_px, mapa.altura_px)
    camera(cx,cy,250, #olho
        cx,cy,1, #bola
        0, 1, 0); #up
    
    background(0)
    mapa.desenha()
    print(mapa.tilePersonagem(player).tipo)
    
def keyPressed():
    mapa.movePersonagem(player,keyCode)
    
def keyReleased():
    mapa.movePersonagem(player,keyCode,True)
    
def cameraMov(x,y,w,h):
    margem = 140
    x = constrain(x, margem, w-margem)
    y = constrain(y, margem, h-margem)
    
    return x,y