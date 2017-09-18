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
        self.img_url = img_url
        
    def setSprite(self):
        self.img = Sprite(self.img_url)
    
    def desenha(self):
        self.img.desenha(self.x, self.y, self.dir)
        #fill(255,0,0)
        #ellipse(self.x, self.y, self.s, self.s)
    
    def move(self, tecla, para = False):
        if para:
            vel = 0
        else:
            vel = self.vel
        
        if tecla == 37:
            self.vx = -vel
        if tecla == 38:
            self.vy = -vel
        if tecla == 39:
            self.vx = vel
        if tecla == 40:
            self.vy = vel
            
        if self.vx < 0:
            self.dir = 0
        if self.vx > 0:
            self.dir = 1
        if self.vy < 0:
            self.dir = 2
        if self.vy > 0:
            self.dir = 3
            
    def update(self):
        self.x += self.vx
        self.y += self.vy
        
        self.x = constrain(self.x,self.s/2,self.w - self.s/2)
        self.y = constrain(self.y,self.s/2,self.h - self.s/2)
        
        self.desenha()