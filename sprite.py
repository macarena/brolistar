class Sprite:
    def __init__(self, img_url):
        self.img = loadImage(img_url)
        self.recorte()
        self.pose = 0
        
    def desenha(self, x, y, dir):
        i = self.imgs[dir][int(self.pose)]
        x = x - i.width/2
        y = y - i.height + 20
        image(i, x, y)
        self.pose += 0.1
        if self.pose >= len(self.imgs) + 1:
            self.pose = 1
        
    def recorte(self):
        cols = 5
        lines = 4
        w = self.img.width / cols
        h = self.img.height / lines
        self.imgs = []
        
        for lin in range(lines):
            linha = []
            for col in range(cols):
                x = col * w
                y = lin * h
                recorte = self.img.get(x,y,w,h)
                linha.append(recorte)
            self.imgs.append(linha)
        