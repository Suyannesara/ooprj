## 🚀 Entrega_1 - Pseudocódigo

**Tags**: Herança, Encapsulamento, Polimorfismo, Classes, Objetos...


### ✨ Features - O que esse projeto comtempla:

- [x] Classe Linha (Base)
    - Métodos:
        - desenharLinha - define uma linha no plano (__init__)
        - setInicioLinha - alterar valor do atributo `ponto_inicial`
        - setFimLinha - alterar valor do atributo `ponto_final`
        - getParCoordenadas - retorna os atributos `ponto_inicial` ou `ponto_final`

- [x] Classe Forma (Classe mãe para a definição de qualquer forma)
    - Métodos:
        - iniciarForma (__init__)
        - setPoligono - desenha um poligono no plano
        - setNumeroLados - alterar valor do atributo `numero_lados`
        - getNumeroLados - retorna o atributo `numero_lados`
        - getLinhas - retorna o array de linhas criadas para a construção da forma

- [x] Classe Triangulo (Classe filha que herda de Forma)
    - Métodos:
        - iniciarTriangulo (__init__)
        - setTriangulo - desenha um triângulo no plano
        - calcularComprimentoLados - função intermediária usada em setTipo(). Define o valor do atributo `comprimento_linhas`
        - setTipo - define o atributo `tipo` do triângulo como sendo "isósceles", "escaleno" ou "equilátero"
        - getTipo - retorna o atributo `tipo`

- [x] main() - função de execução principal, exemplifica o uso das classes, seus métodos e atributos com o exeplo do triângulo




