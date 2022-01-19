from Aula07 import Calculadora
from Aula07_b import Televisao
from Aula08_a import contador_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(num1=5, num2=10)
    print(calculadora.soma())

    lista = ['Joyce', 'Gilberto']
    total_letras = contador_letras(lista)
    print(f'Total de letras de cada nome: {total_letras}')
    print(teste())
