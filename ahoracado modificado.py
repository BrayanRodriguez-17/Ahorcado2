class Ahorcado:
    def __init__(self):
        self.palabra_secreta = "Ahorcado"
        self.letras_correctas = []
        self.intentos_restantes = 8
        self.muñeco = ["  O", " \|/", "  |", " / \\"]

    def mostrar_palabra(self):
        resultado = ''
        for letra in self.palabra_secreta:
            resultado += letra if letra in self.letras_correctas else '_'
            resultado += ' '
        return resultado

    def mostrar_muñeco(self):
        resultado = ''
        for i in range(8 - self.intentos_restantes):
            resultado += self.muñeco[i]
        return resultado

    def jugar(self):
        print("¡Bienvenido al Juego del Ahorcado!")
        print("Descubre la palabra oculta. ¡Buena suerte!")

        while self.intentos_restantes > 0:
            print(f"{self.mostrar_muñeco()}")
            print(self.mostrar_palabra())

            letra_usuario = self.obtener_letra()
            if letra_usuario in self.palabra_secreta and letra_usuario not in self.letras_correctas:
                self.letras_correctas = [letra_usuario] + self.letras_correctas
                print(f"¡Correcto! Letras correctas: {', '.join(self.letras_correctas)}")
            else:
                self.intentos_restantes -= 1
                print(f"Incorrecto. Te quedan {self.intentos_restantes} intentos.")

            if set(self.palabra_secreta).issubset(self.letras_correctas):
                print("¡Felicidades! ¡Has adivinado la palabra!")
                break

        self.opcion_reiniciar()

    def obtener_letra(self):
        while True:
            letra = input("Ingresa una letra: ")
            if letra:
                return letra
            else:
                print("Por favor, ingresa un carácter.")

    def opcion_reiniciar(self):
        reiniciar = input("¿Quieres jugar de nuevo? (Sí/No): ").lower()
        if reiniciar == 'si':
            juego = Ahorcado()
            juego.jugar()
        else:
            print("Gracias por jugar. ¡Hasta luego!")

# Inicializar el juego
juego = Ahorcado()
juego.jugar()