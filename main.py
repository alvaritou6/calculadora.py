import time
from datetime import datetime

print("Fecha y Hora: ", datetime.now().strftime('%d-%m-%Y %H:%M'))

n1 = float(input("Introduce tu primer numero: "))
n2 = float(input("Introduce tu segundo numero: "))
option = 0

while True:
    print("""
    Dime, ¿Que quieres hacer?
    
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Dividir los dos numeros
    5) Cambiar los números elegidos
    6) Apagar calculadora
    """)
    option = int(input("Elige una opcion: "))

    if option == 1:
        print("")
        print("La suma de ", n1, "+", n2, "es igual a", n1+n2)
    elif option == 2:
        print("")
        print("La resta de ", n1, "-", n2, "es igual a", n1 - n2)
    elif option == 3:
        print("")
        print("La multiplicacion de ", n1, "por", n2, "es igual a", n1 * n2)
    elif option == 4:
        print("")
        print("La division de ", n1, ":", n2, "es igual a", n1 / n2)
    elif option == 5:
       n1 = float(input("Introduce tu primer numero: "))
       n2 = float(input("Intrroduce tu segundo numero: "))
    elif option == 6:
        print("La calculadora será apagada en 3 segundos. Nos vemos pronto :D")
        time.sleep(3)
        break
    else:
        print("")
        print("Opcion Incorrecta")