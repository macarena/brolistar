from random import randint
import csv

class Quadrado:
    tipos = ["agua", "grama", "areia", "estrada", "pedra", "arbusto"]
    amarelo = color(255, 230, 0)
    azul_escuro = color(7, 0, 255)
    marrom_escuro = color(85, 25, 27)
    verde_claro = color(10, 237, 7)
    marrom_claro = color(193, 109, 111)
    verde_escuro = color(48, 72, 36)
    cores = {
        "agua": azul_escuro,
        "pedra": marrom_escuro,
        "areia": amarelo,
        "grama": verde_claro,
        "estrada": marrom_claro,
        "arbusto": verde_escuro
    }
    
    def __init__(self, tipo, linha, coluna):
        self.cor = self.cores[tipo]
        self.tipo = tipo
        self.linha = linha
        self.coluna = coluna
        
    def desenha(self,x,y,w,h):
        fill(self.cor)
        rect(x,y,w,h)
        
class Mapa:
    quadrados = []
    
    def __init__(self, largura, altura):
        #largura e altura em numero de linhas e colunas
        self.largura = largura
        self.altura = altura
        self.escala = 40
        #self.criarQuadrados()
        self.importarQuadrados("data/mapa1.csv")
        
    def criarQuadrados(self):
        for linha in range(self.altura):
            for coluna in range(self.largura):
                tipo = Quadrado.tipos[randint(0,5)]
                self.quadrados.append(Quadrado(tipo,linha,coluna))
                
    def importarQuadrados(self, arquivo):
        f = open(arquivo, 'rb')
        conteudo = csv.reader(f)
        numLinha = 0
        for linha in conteudo:
            numColuna = 0
            for item in linha:
                tipo = Quadrado.tipos[int(item)]
                self.quadrados.append(Quadrado(tipo,numLinha,numColuna))
                numColuna += 1
            numLinha += 1
        f.close()
                
    def desenha(self):
        for quadrado in self.quadrados:
            x = self.escala * quadrado.coluna
            y = self.escala * quadrado.linha
            w = self.escala
            h = self.escala
            noStroke()
            quadrado.desenha(x,y,w,h)
    
        