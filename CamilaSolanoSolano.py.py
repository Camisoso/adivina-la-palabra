#Utilice una libreria "random" para que le imprima al usuario una palabra al azar

import random

# Lista de palabras posibles
palabras = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

# Función principal del juego
def adivina_la_palabra():
    # Selecciona una palabra aleatoria
    palabra = random.choice(palabras)
    
    # Definimos las variables
    vidas = 6
    letras_incorrectas = []
    palabra_oculta = ['_'] * len(palabra)

    #Despues de definir las variables le mostramos al usuario las respuestas
    print("¡Bienvenido al juego de 'Adivina la palabra'!")
    print("Tienes", vidas, "vidas.")
    print("La palabra tiene", len(palabra), "letras.")

    #creamos un bucle para que el codigo no se caiga y el usuario pueda continuar con el juego
    while vidas > 0 and '_' in palabra_oculta:
        print("\nPalabra:", ' '.join(palabra_oculta))
        print("Letras incorrectas:", ' '.join(letras_incorrectas))
        print(f"Tienes {vidas} vidas restantes.")
        
        # Solicita una letra
        letra = input("Ingresa una letra: ").lower()
        
        # A traves de un condicional validamos el ingreso de solo una letra
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue
        
        # Verifica si la letra ya fue ingresada, seguimos con condicionales para mantener el bucle abierto y que el codigo no se caiga.
        if letra in letras_incorrectas or letra in palabra_oculta:
            print("Ya has intentado esa letra. Elige otra.")
            continue
        
        # Verifica si la letra está en la palabra
        if letra in palabra:
            print(f"La letra '{letra}' está en la palabra.")
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_oculta[i] = letra
                    
        # Si las condiciones anteriores no se cumplen el codigo salta al else y cierra con el bucle            
        else:
            print(f"La letra '{letra}' no está en la palabra.")
            letras_incorrectas.append(letra)
            vidas -= 1

    # Fin del juego, utilice otras condicionales para indicarle al usuario si acerto la palabra o por el contrario se quedo sin vidas.
    if '_' not in palabra_oculta:
        print("\n¡Felicidades! Has adivinado la palabra:", palabra)
    else:
        print("\nTe has quedado sin vidas. La palabra era:", palabra)

    # Pregunto si quiere jugar de nuevo, sino a traves del else se cierra la terminal.
    jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? (si/no): ").lower()
    if jugar_de_nuevo == 's':
        adivina_la_palabra()
    else:
        print("Gracias por jugar!!!")

# Para que el codigo funcione debo llamar a la funcion principal
adivina_la_palabra()
