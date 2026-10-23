#Programa para calcular áreas
#Area de un cuadrado; lado x lado
#///Cuadrado///
print("///////////")
lado=float(input("Ingresa un lado: ")) 
area_cuadrado=lado*lado
print(f"El área del cuadrado es {area_cuadrado}")
#///Triangulo///
print("///////////")
base=float(input("Ingresa la base del triangulo: "))
altura=float(input("Ingresa la altura del triangulo: "))
area_del_triangulo=(base*altura)/2
print(f"El área del tirangulo es{area_del_triangulo}: ")
#///Trapecio///
print("///////////")
base_mayor=float(input("Ingresa la base mayor: "))
base_menor=float(input("Ingresa la base menor: "))
altur_trapecio=float(input("Ingresa la altura del trapecio: "))
area_del_rapecio=(base_mayor+base_menor)*altur_trapecio/2
print(f"El área del trapecio es {area_del_rapecio}: ")
#///Circulo///
print("///////////")
pi=3.1416
Radio=float(input("Ingresa el radio del circulo: "))
area_del_circulo=pi*(Radio*Radio)
print(f"El área del circulo {area_del_circulo} es: ")
#///Pentagono///
print("///////////")
lado_pentagono=float(input("Ingresa un lado del pentágono: "))
Perimetro=lado_pentagono*5
Apotema=float(input("Ingresa el apotema del pentágono: "))
print(f"El área del pentágono {(Perimetro*Apotema)/2}es: ")
#///Rectangulo///
print("///////////")
base_rectangulo=float(input("Ingresa la base del rectangulo: "))
altura_rectangulo=float(input("Ingresa la altura del rectangulo: "))
Area_rectangulo=base_rectangulo*altura_rectangulo
print(f"El área del rectangulo {altura_rectangulo}es: ")
#///Rombo///
print("///////////")
Diagonal_mayor=float(input("Ingresa la diagonal mayor del rombo: "))
Diagonal_menor=float(input("Ingresa la diagonal menor del rombo: "))
Área_rombo=(Diagonal_mayor*Diagonal_menor)/2