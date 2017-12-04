from sprite import Sprite

class Personagem:
    
    def __init__(self,x,y,w,h,img_url):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.s = 35
        self.vel = 10
        self.vx = 0
        self.vy = 0
        self.dir = 0
        self.parado = False
        self.img_url = img_url
        self.setSprite()
        
    def setSprite(self):
        self.img = Sprite(self.img_url)
    
    def desenha(self):
        self.img.desenha(self.x, self.y, self.dir, self.parado)
        #fill(255,0,0)
        #ellipse(self.x, self.y, self.s, self.s)
    
            
    def update(self):
        self.x += self.vx
        self.y += self.vy
        
        if self.vx == 0 and self.vy == 0:
            self.parado = True
        else:
            self.parado = False
        
        self.x = constrain(self.x,self.s/2,self.w - self.s/2)
        self.y = constrain(self.y,self.s/2,self.h - self.s/2)
        
        self.desenha()