import random

# Lista de palabras posibles
palabras = ['python', 'java', 'ruby', 'javascript', 'html', 'css', 'flask', 'django']

# Función principal del juego
def adivina_la_palabra():
    # Selecciona una palabra aleatoria
    palabra = random.choice(palabras)
    
    # Inicializa las variables
    vidas = 6
    letras_incorrectas = []
    palabra_oculta = ['_'] * len(palabra)
    
    print("¡Bienvenido al juego de 'Adivina la palabra'!")
    print("Tienes", vidas, "vidas.")
    print("La palabra tiene", len(palabra), "letras.")
    
    while vidas > 0 and '_' in palabra_oculta:
        print("\nPalabra:", ' '.join(palabra_oculta))
        print("Letras incorrectas:", ' '.join(letras_incorrectas))
        print(f"Tienes {vidas} vidas restantes.")
        
        # Solicita una letra
        letra = input("Ingresa una letra: ").lower()
        
        # Validación de la letra
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue
        
        # Verifica si la letra ya fue ingresada
        if letra in letras_incorrectas or letra in palabra_oculta:
            print("Ya has intentado esa letra. Elige otra.")
            continue
        
        # Verifica si la letra está en la palabra
        if letra in palabra:
            print(f"La letra '{letra}' está en la palabra.")
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_oculta[i] = letra
        else:
            print(f"La letra '{letra}' no está en la palabra.")
            letras_incorrectas.append(letra)
            vidas -= 1

    # Fin del juego
    if '_' not in palabra_oculta:
        print("\n¡Felicidades! Has adivinado la palabra:", palabra)
    else:
        print("\nTe has quedado sin vidas. La palabra era:", palabra)

    # Preguntar si quiere jugar de nuevo
    jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo == 's':
        adivina_la_palabra()
    else:
        print("Gracias por jugar. ¡Hasta la próxima!")

# Llamada al juego
adivina_la_palabra()
