#Poyecto de validacion de la longitud de una palabra
#utiliza if y elif para validar las palabras q se introduzcan

print("Hola, por favor introduce una palabra que contenga de 4 a 8 caracteres")

palabra = input("introduce una palabra:")

contador = len(palabra)
print(f"la palabra {palabra} tiene {contador} letras")

if len(palabra) < 4:
    print("La palabra es invalida faltan letras")
    
elif len(palabra) > 8:
    print("La palabra es invalida sobran letras")
    
elif len(palabra) >= 4:
    print("La palabra esta dentro de la longitud permitida")
    
elif len(palabra) <= 8:
    print("La palabra esta dentro de la longitud permitida")
    