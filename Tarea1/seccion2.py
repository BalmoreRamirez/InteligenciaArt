def calcula():
    celsius = ['32.5', '40.7', '23.0', '44.0', '15.9', '33.8', '45.6', '67.0', '70.4']
    celsius = list(map(float, celsius))
    fahrenheit = []
    for x in celsius:
        z = (x * 1.8) + 32
        fahrenheit = z
        print(fahrenheit)


calcula()
