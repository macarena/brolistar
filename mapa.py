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
        