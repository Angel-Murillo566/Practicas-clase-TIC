nombres=["Angel","Karla","Luis","Mateo","Maria","Luis","Karla"]
print(f"Los nombres que se tienen son:{nombres}")
nombresbuscar=input("¿Que nombre deseas buscar?: ")
encontrado=False
contador=0
i=0
while i<len(nombres):
    if nombres[i]==nombresbuscar:
        encontrado=True
        contador=contador+1
        print("Encontrado en la posición: ", i)
    i=i+1
if encontrado==True:
    print("Nombre encontrado")
    print("Aparece",contador, "veces")
else:
    print("Nombre no encontardo")
if contador>1:
    nombres=[nombres for nombres in nombres if nombres !=nombresbuscar]
    print("Nombre eliminado de la lista")
    print("Lista actualizada",nombres)