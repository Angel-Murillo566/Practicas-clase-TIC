#Listas
alumnos=["Juanito","Angelito"]
#Diccionarios
alumno1={
    "nombre":"Juanito",
    "edad":15,
    "promedio":8.2
}
alumno2={
    "nombre":"Angelito",
    "edad":18,
    "promedio":10
}
#Consulatar valores
#Forma1
print("Nombre:", alumno1["nombre"])
#Forma2
print("Nombre:", alumno1.get("nombre"))
#Modificar/editar algun campo
alumno1["nombre"]="Pedrito"
print("Nombre:", alumno1.get("nombre"))
#Mostar CLAVE:Valor
for clave, valor in alumno1.items():
    print(clave, ":", valor)
