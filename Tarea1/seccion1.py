class Calculadora:
    def suma(num1, num2):
        return num1 + num2

    def resta(num1, num2):
        return num1 - num2

    def multiplicacion(num1, num2):
        return num1 * num2

    def division(num1, num2):
        return num1 / num2

    def potencia(num1, num2):
        return num1 ** num2


operacion = Calculadora
print('La suma de  es: ' + str(operacion.suma(2, 2)))
print('La Resta es:' + str(operacion.resta(3, 1)))
print('La multiplicacion es:' + str(operacion.multiplicacion(2, 2)))
print('La division es:' + str(operacion.division(4, 2)))
print('La potencia es:' + str(operacion.potencia(2, 2)))
