'''
Enunciado: Suma de dos números

Escribe un programa en Python que solicite al usuario ingresar dos números. Luego, calcula la suma de esos dos números y la imprime en la pantalla. Asegúrate de manejar adecuadamente la entrada del usuario.
'''

while True:
    try:
        number_1 = float(input("Escribe el primer número: "))
        break
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")

while True:
    try:
        number_2 = float(input("Escribe el segundo número: "))
        break
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")

try:
    sum_numbers = number_1 + number_2
    print(f"El resultado de sumar los números {number_1} y {number_2} es {sum_numbers}")
except:
    print("Uy algo salió mal...")
