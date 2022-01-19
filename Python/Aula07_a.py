num1 = float(input('Primeiro termo: '))
num2 = float(input('Segundo termo: '))

class Calculadora:
    def __init__(self):
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.soma(num1, num2))
print(calculadora.subtracao(num1, num2))
print(calculadora.multiplicacao(num1, num2))
print(calculadora.divisao(num1, num2))
