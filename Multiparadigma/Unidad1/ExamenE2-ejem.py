# Función para invertir los dígitos de un número de 3 dígitos
def invertir_digitos(numero):
    # Convierte el número en una cadena de texto
    numero_str = str(numero)
    
    # Invierte la cadena
    numero_invertido = numero_str[::-1]
    
    # Convierte la cadena invertida nuevamente a un número entero
    return int(numero_invertido)

# Solicita al usuario ingresar dos números de 3 dígitos
numero1 = int(input("Ingrese el primer número de 3 dígitos: "))
numero2 = int(input("Ingrese el segundo número de 3 dígitos: "))

# Verifica que los números tengan 3 dígitos
if 100 <= numero1 <= 999 and 100 <= numero2 <= 999:
    # Invierte los dígitos de los números
    numero1_invertido = invertir_digitos(numero1)
    numero2_invertido = invertir_digitos(numero2)
    
    # Encuentra el número mayor entre los dos invertidos
    mayor = max(numero1_invertido, numero2_invertido)
    
    # Imprime el número mayor
    print(f"El número mayor después de invertir los dígitos es: {mayor}")
else:
    print("Por favor, ingrese números de 3 dígitos válidos.")