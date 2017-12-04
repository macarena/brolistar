from random import randint
import csv
from personagem import *

class Quadrado:
    tipos = ["agua", "grama", "areia", "estrada", "pedra", "arbusto", "lava", "pedra_agua", "pedra_estrada"]

    pos_terreno = {
        "agua": {'x': 18, 'y': 5, 'andavel': False},
        "pedra": {'x': 20, 'y': 19, 'bg': 'grama', 'andavel': False},
        "pedra_agua": {'x': 20, 'y': 19, 'bg': 'agua', 'andavel': False},
        "pedra_estrada": {'x': 20, 'y': 19, 'bg': 'estrada', 'andavel': False},
        "areia": {'x': 0, 'y': 17, 'andavel': True},
        "grama": {'x': 0, 'y': 11, 'andavel': True},
        "estrada": {'x': 10, 'y': 18, 'andavel': True},
        "arbusto": {'x': 11, 'y': 11, 'bg': 'grama', 'andavel': True},
        "lava": {'x': 10, 'y': 17, 'andavel': True}
    }
    
    def __init__(self, tipo, linha, coluna, tiles):
        self.tipo = tipo
        self.linha = linha
        self.coluna = coluna
        x = self.pos_terreno[tipo]['x']
        y = self.pos_terreno[tipo]['y']
        self.img = tiles[y][x]
        self.andavel = self.pos_terreno [tipo]['andavel']
        if 'bg' in self.pos_terreno[tipo]:
            bg = self.pos_terreno[tipo]['bg']
            img = createGraphics(32,32)
            img.beginDraw()
            x = self.pos_terreno[bg]['x']
            y = self.pos_terreno[bg]['y']
            img.image(tiles[y][x], 0, 0)
            img.image(self.img, 0, 0)
            img.endDraw()
            self.img = img
        
    def desenha(self,x,y,w,h):
        image(self.img,x,y)
        
class Mapa:
    quadrados = []
    personagens = []
    
    def __init__(self):
        self.importarTiles()
        self.importarQuadrados("data/mapa3.csv")
        #largura e altura em numero de linhas e colunas
        self.escala = 32
        self.largura_px = self.largura * self.escala
        self.altura_px = self.altura * self.escala
    
    def addPersonagem(self, p):
        personagem = Personagem(self.largura_px/2, self.altura_px/2, self.largura_px ,self.altura_px, "link.png")
        self.personagens.append(personagem)
        return personagem
    
    def movePersonagem(self, p, tecla, para=False):
        if para:
            vel = 0
        else:
            vel = p.vel
        
        if tecla == "a":
            p.vx = -vel
        if tecla == "w":
            p.vy = -vel
        if tecla == "d":
            p.vx = vel
        if tecla == "s":
            p.vy = vel
            
        if p.vx < 0:
            p.dir = 0
        if p.vx > 0:
            p.dir = 1
        if p.vy < 0:
            p.dir = 2
        if p.vy > 0:
            p.dir = 3
            
            
    def verificarMovimento(self,p):
        novoX = p.x + p.vx
        novoY = p.y + p.vy
        quadrado_futuro = self.tileXY(novoX, novoY)
        if not quadrado_futuro.andavel:
            p.vx = 0
            p.vy = 0
        
    def tileXY(self, x, y):
        coluna = x / self.escala
        linha = y / self.escala
        for q in self.quadrados:
            if q.coluna == coluna and q.linha == linha:
                return q
            
    def tilePersonagem(self, p):
        coluna = p.x / self.escala
        linha = p.y / self.escala
        for q in self.quadrados:
            if q.coluna == coluna and q.linha == linha:
                return q
    
    def importarTiles(self):
        self.img = loadImage("terrain.png")
        cols = 21
        lines = 23
        w = self.img.width / cols
        h = self.img.height / lines
        self.tiles = []
        
        for lin in range(lines):
            linha = []
            for col in range(cols):
                x = col * w
                y = lin * h
                recorte = self.img.get(x,y,w,h)
                linha.append(recorte)
            self.tiles.append(linha)
                
    def importarQuadrados(self, arquivo):
        f = open(arquivo, 'rb')
        conteudo = csv.reader(f)
        numLinha = 0
        for linha in conteudo:
            numColuna = 0
            for item in linha:
                tipo = Quadrado.tipos[int(item)]
                self.quadrados.append(Quadrado(tipo,numLinha,numColuna,self.tiles))
                numColuna += 1
            numLinha += 1
        f.close()
        self.largura = numColuna
        self.altura = numLinha
                
    def desenha(self):
        for quadrado in self.quadrados:
            x = self.escala * quadrado.coluna
            y = self.escala * quadrado.linha
            w = self.escala
            h = self.escala
            noStroke()
            quadrado.desenha(x,y,w,h)
        for p in self.personagens:
            self.verificarMovimento(p)
            p.update()
            
    
        