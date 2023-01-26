print("============================")
print("Menú de opciones")
print("============================ \n")

print("Selecciona una opcion")
print("Si quieres convertir un numero a letras presiona 1: ")
print("Si quieres convertir de letras a numero presiona 2: \n")

opcion = int(input("Que opcion quieres?: "))


if (opcion == 1):
    print("Conversor de numero a letras \n")

    opcion_uno = int(input("Elija el numero que quiere convertir a letras: "))

    if (opcion_uno == 1):
            print("el numero que ha elegido es el uno")

    elif (opcion_uno == 2):
            print("el numero que ha elegido es el dos")

    else:
        print("numero no disponible")
                     

elif (opcion == 2):
    print("Conversor de letras a numeros \n")

    opcion_dos = input("escriba la palabra que quiere pasar a numeros: ")
    opcion_dos = opcion_dos.lower()

    if (opcion_dos == "uno"):
            print("el numero que ha elegido es el 1")

    elif (opcion_dos == "dos"):
            print("el numero que ha elegido es el 2")

    else:
            print("numero no disponible")


print("Fin")




    
    
