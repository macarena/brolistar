#Brólistar - A estrelinha briguenta
from personagem import *

w = 600
h = 600
player = Personagem(w/2,h/2,w,h, "link.png")
player2 = Personagem(w/2,h/2,w,h, "maga.png")

def setup():
    size(w,h, P3D)
    player.setSprite()
    player2.setSprite()
    
def draw():
    cx, cy = cameraMov(player.x, player.y, w, h)
    camera(cx,cy,250, #olho
        cx,cy,1, #bola
        0, 1, 0); #up
    
    background(0)
    fill(0,255,0)
    rect(0,0,w,h/2)
    fill(0,0,255)
    rect(0,h/2,w,h/2)
    
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