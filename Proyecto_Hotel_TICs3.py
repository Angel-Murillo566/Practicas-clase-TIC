huespedes={}
habitaciones={
    101:{
        "tipo": "Individual",
        "precio": 500,
        "estado": "Disponible"
    },
    102:{
        "tipo": "Doble",
        "precio": 800,
        "estado": "Disponible"
    },
    103:{
        "tipo": "Suite",
        "precio": 1200,
        "estado": "Disponible"
    }
}
def registrar_huesped():
       id = input("Ingresa el ID del huésped: ")
       if id in huespedes:
          print("Este huésped ya está registrado")
       else:
          nombre=input("Nobre: ")
          edad=int(input("Edad: "))
          telefono=input("Telefono: ")
          huespedes[id]={
             "nombre": nombre,
             "edad": edad,
             "telefono": telefono
          }
          print("Huésped registrado correctamente")
def eliminar_huesped():
   id = input("Ingresa la ID del huésped a eliminar: ")
   if id in huespedes:
      del huespedes[id]
      print("Huésped eliminado correctamente")
   else:
      print("No se encontro algun huesped con esa ID")
def buscar_huesped():
   id=input("Ingresa la ID del huésped que deseas buscar: ")
   if id in huespedes:
      print("=====HUÉSPED ENCONTRADO=====")
      print("ID:", id)
      print("Nombre:", huespedes[id]["nombre"])
      print("Edad:", huespedes[id]["edad"])
      print("Telefono:", huespedes[id]["telefono"])
   else:
      print("No se encontro ningun huésped con esa ID")
def mostrar_huespedes():
   if len(huespedes) == 0:
      print("No hay huéspedes registrados")
   else:
      print("=====LISTA DE HUÉSPEDES=====")
      for id, datos in huespedes.items():
         print("    ")
         print("ID: ",id)
         print("Nombre: ",datos["nombre"])
         print("Edad: ",datos["edad"])
         print("Telefono: ",datos["telefono"])
def consultar_habitaciones():
   print("=====HABITACIONES DEL HOTEL=====")
   for numero, datos in habitaciones.items():
      print("Habitacion:", numero)
      print("Tipo: ", habitaciones["tipo"])
      print("Precio: ", habitaciones["precio"])
      print("Estado: ",habitaciones["estado"])
      
reservaciones={}
while True:
    print("=====Hotel el gran hotel=====")
    print(" ")
    print("1. Regiatrar huésped")
    print(" ")
    print("2. Eliminar huésped")
    print(" ")
    print("3. Buscar huésped")
    print(" ")
    print("4. Mostrar huéspedes")
    print(" ")
    print("5. Consultar habitaciones")
    print(" ")
    print("6. Realizar reservación")
    print(" ")
    print("7. Cancelar reservación")
    print(" ")
    print("8. Mostrar reservación")
    print(" ")
    print("9. Salir")
    opcion=input("Selecciona una opción: ")
    if opcion == "1":
       registrar_huesped()
    elif opcion == "2":
       eliminar_huesped()
    elif opcion == "3":
       buscar_huesped()
    elif opcion == "4":
       mostrar_huespedes()
    elif opcion =="5":
       consultar_habitaciones()
    elif opcion == "6":
       print("6. Realizar reservación")
    elif opcion == "7":
       print("7. Cancelar reservación")
    elif opcion == "8":
       print("8. Mostrar reservación")
    elif opcion == "9":
       print("9. Gracias por usar Hotel el gran Hotel")
    else:
       print("Opción no valida")
    