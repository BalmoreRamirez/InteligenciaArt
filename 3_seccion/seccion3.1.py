x = 'global'


def miFuncion():
    x = 'local funcion'
    print(x)

    for i in range(1):
        x = 'local bucle for'
        print(x)

        def miFuncionInterna():
            # AMBITO LOCAL FUNCION miFuncionInterna
            # Esta variable x esta dentro de una funcion <miFuncionInterna> que a la vez esta dentro de un bucle for,
            # que esta dentro de una funcion <miFuncion>
            x = 'local funcion interna'
            print(x)

        miFuncionInterna()
print(x)
miFuncion()

# como utlizar global
glob = 'global'
def miFuncion():
    loc ='local'
    print(loc)
    global glob
    glob = 'global modificada'

print(glob)
miFuncion()
print(glob)
