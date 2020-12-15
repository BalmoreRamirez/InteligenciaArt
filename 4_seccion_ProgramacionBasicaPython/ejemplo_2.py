# cambalanches
class Empleado:
    # declaracion null que no require unicializar los atributos
    pass


Pedro = Empleado()
Pedro.puesto = 'CEO'
Pedro.profesion = 'ingeniero'

Laura = Empleado()
Laura.puesto = 'CTO'
Laura.salario = '1000'

print('Pedro es el ' + Pedro.puesto)
print('Laura gana: ' + Laura.salario)
