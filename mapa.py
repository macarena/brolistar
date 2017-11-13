from random import randint
import csv

class Quadrado:
    tipos = ["agua", "grama", "areia", "estrada", "pedra", "arbusto", "lava"]

    pos_terreno = {
        "agua": {'x': 18, 'y': 5},
        "pedra": {'x': 20, 'y': 17},
        "areia": {'x': 0, 'y': 17},
        "grama": {'x': 0, 'y': 11},
        "estrada": {'x': 10, 'y': 18},
        "arbusto": {'x': 11, 'y': 11},
        "lava": {'x': 10, 'y': 17}
    }
    
    def __init__(self, tipo, linha, coluna, tiles):
        self.tipo = tipo
        self.linha = linha
        self.coluna = coluna
        x = self.pos_terreno[tipo]['x']
        y = self.pos_terreno[tipo]['y']
        self.img = tiles[x][y]
        
    def desenha(self,x,y,w,h):
        image(self.img,x,y)
        
class Mapa:
    quadrados = []
    
    def __init__(self):
        self.importarTiles()
        self.importarQuadrados("data/mapa3.csv")
        #largura e altura em numero de linhas e colunas
        self.escala = 32
        self.largura_px = self.largura * self.escala
        self.altura_px = self.altura * self.escala
    
    def importarTiles(self):
        self.img = loadImage("terrain.png")
        cols = 21
        lines = 22
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
    
        