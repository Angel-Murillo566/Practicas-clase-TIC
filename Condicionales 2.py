#Programa
print("///////////////")
calificaciones=float(input("Dame tu calificación: "))
if calificaciones==10:
     print("Exelente")
elif calificaciones==9:
     print("Muy bien")
elif calificaciones==8:
     print("Bien")
elif calificaciones==7:
     print("Puedes mejorar")
elif calificaciones==6:
     print("Ay mijo")
else:
     print("Muy mal")
 #Temperaturas
print("///////////////")
Temperatura=float(input("Coloca la temperatura: "))
if Temperatura==40:
     print("Hace mucho calor")
elif Temperatura>=30 and Temperatura<40:
     print("Esta templado")
elif Temperatura==20 and Temperatura<30:
     print("Esta fresco")
elif Temperatura<=10 and Temperatura<20:
     print("Hace frio")
else:
     print("No valido")
print("///////////////")
sexo=input("Coloca tu sexo/genero: ")
edad=int(input("Coloca tu edad: "))
if sexo=="Hombre" and edad>=18:
     print("Puedes sacar tu cartilla militar")
else:
     print("No puedes")