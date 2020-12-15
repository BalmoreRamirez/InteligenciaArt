# Los métodos pueden llamar a otros métodos de la instancia
# usando el argumento self

class Calculadora:
    def __init__(self):
        self.resultado = 0
        self.contador = 0

    def sumarDosVeces(self, numero1, numero2):
        self.sumar(numero1, numero2)
        self.sumar(numero1, numero2)

    def sumar(self, numero1, numero2):
        self.resultado = self.resultado + numero1 + numero2

    def sumaxVeces(self, num1, num2):
        for x in range(10):
            self.sumar(num1, num2)


x = Calculadora()
x.sumar(5, 4)
print("El resultado de la suma es: " + str(x.resultado))

x2 = Calculadora()
x2.sumarDosVeces(5, 4)

x3 = Calculadora()
x3.sumaxVeces(2, 2)
print("El resultado de la suma es: " + str(x2.resultado))
print("El resultado de la suma usando for es: "+str(x3.resultado))
