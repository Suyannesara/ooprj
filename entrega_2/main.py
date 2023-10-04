
# 🚀 Essa é a versão final para avaliação

#ENTREGA 2 - Codigo python criação de formas (v.2.0)
import math

class Linha:
    def __init__(self, ponto_inicial, ponto_final):
        self.ponto_inicial = ponto_inicial
        self.ponto_final = ponto_final
        self.inclinacao_linha = None

    def calcularCoordenadasIntermediarias(self):
        diferenca_x = self.ponto_final["x"] - self.ponto_inicial["x"]
        diferenca_y = self.ponto_final["y"] - self.ponto_inicial["y"]
        qtd_pontos_intermediarios = round(diferenca_x)
        passo_x = diferenca_x / qtd_pontos_intermediarios
        passo_y = diferenca_y / qtd_pontos_intermediarios
        coordenadas = []
        for i in range(qtd_pontos_intermediarios):
            x = self.ponto_inicial["x"] + i * passo_x
            y = self.ponto_inicial["y"] + i * passo_y
            coordenadas.append({"x": x, "y": y})
        return coordenadas

    def setInicioLinha(self, ponto_inicial):
        self.ponto_inicial = ponto_inicial
    
    def setFimLinha(self, ponto_final):
        self.ponto_final = ponto_final

    def getParCoordenadas(self, tipo):
        if tipo == 'inicioLinha':
            return self.ponto_inicial
        elif tipo == 'fimLinha':
            return self.ponto_final
        return [self.ponto_inicial, self.ponto_final]

class Forma:
    def __init__(self):
        self.numero_lados = None
        self.pontos = None
        self.linhas = []

    def iniciarForma(self, numero_lados, pontos):
        self.numero_lados = numero_lados
        self.pontos = pontos

    def setPoligono(self, pontos):
        for i in range(len(self.pontos)):
            ponto_inicial_linha = self.pontos[i]
            ponto_final_linha = self.pontos[(i + 1) % len(self.pontos)]
            linha = Linha(ponto_inicial_linha, ponto_final_linha)
            self.linhas.append(linha)
    
    def setNumeroLados(self, numero_lados):
        self.numero_lados = numero_lados
    
    def getNumeroLados(self):
        return self.numero_lados
    
    def getLinhas(self):
        return self.linhas

class Triangulo(Forma):
    def __init__(self, pontos):
        super().__init__()
        self.tipo = None
        self.comprimento_linhas = []
        self.numero_lados = 3
        self.pontos = pontos

    def iniciarTriangulo(self):
        if len(self.pontos) != 3:
            print("Não é possível definir um triângulo que não possui 3 lados")
        else:
            self.setPoligono(self.pontos)

    def calcularComprimentoLados(self):
        for i in range(len(self.linhas)):
            linha = self.linhas[i]
            diferenca_x = linha.getFimLinha()["x"] - linha.getInicioLinha()["x"]
            diferenca_y = linha.getFimLinha()["y"] - linha.getInicioLinha()["y"]
            comprimento = math.sqrt(diferenca_x ** 2 + diferenca_y ** 2)
            self.comprimento_linhas.append(comprimento)

    def setTipo(self):
        if len(set(self.comprimento_linhas)) == 1:
            self.tipo = "equilátero"
        elif len(set(self.comprimento_linhas)) == 2:
            self.tipo = "isósceles"
        else:
            self.tipo = "escaleno"
    
    def getTipo(self):
        if self.tipo:
            return self.tipo
        return "Sem tipo definido, é necessário setarTipo()"

def main():
    pontos_triangulo = [
        {"x": 0, "y": 0},
        {"x": 3, "y": 3},
        {"x": 3, "y": 6}
    ]
    triangulo = Triangulo(pontos_triangulo)
    triangulo.iniciarTriangulo()
    print(triangulo.getNumeroLados())  # "3"
    print(triangulo.getTipo())  # "Sem tipo definido, é necessário setarTipo()"
    triangulo.calcularComprimentoLados()
    triangulo.setTipo()
    print(triangulo.getTipo())  # "equilátero"

if __name__ == "__main__":
    main()
