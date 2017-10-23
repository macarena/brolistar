#Brólistar - A estrelinha briguenta
from personagem import *
from mapa import *

mapa = Mapa()
h = mapa.altura_px
w = mapa.largura_px
player = Personagem(w/2,h/2,w,h, "maga.png")
player2 = Personagem(w/2,h/2,w,h, "maga.png")

def setup():
    size(300,300, P3D)
    player.setSprite()
    player2.setSprite()
    
def draw():
    cx, cy = cameraMov(player.x, player.y, w, h)
    camera(cx,cy,250, #olho
        cx,cy,1, #bola
        0, 1, 0); #up
    
    background(0)
    mapa.desenha()
    
    player.update()
    player2.update()
    
def keyPressed():
    player.move(keyCode)
    
def keyReleased():
    player.move(keyCode,True)
    
def cameraMov(x,y,w,h):
    margem = 140
    x = constrain(x, margem, w-margem)
    y = constrain(y, margem, h-margem)
    
    return x,y