#Programa que muestra el valor de (x.y) y en que cuadrante se encuentran

x = int(input("Ingresa el valor de x: "))
y = int(input("Ingresa el valor de y: "))

print(f"({x},{y})")
 

if x==0 and y==0:
    print("Los valores estan en el origen")

if x>0 and y>0:
    print("Los valore se encuentran en el cuadrante I")

if x<0 and y>0:
    print("Los valores se encuentran en el caudrante II")

if x<0 and y<0:
    print("Los valores se encuentran en el caudrante III")

if x>0 and y<0:
    print("Los valores se esncuentran en el cuadrante IV")