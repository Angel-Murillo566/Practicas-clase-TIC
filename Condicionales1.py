#Programa que me indica si reprobe o aprobe 
#Solisitar una calif
calificacion=float(input("Ingresa la calificación"))
#Si la calificación es >=6aprob
if calificacion >=6: 
    print("Aprobaste")
else:
        print("Reprobaste")
#Edad, si e smayor o menor de edad
edad=int(input("Ingresa tu edad: "))
if edad >=18:
      print("Eres mayor de edad")
else:
      print("No eres mayor de edad")
#temperatura >35 hace mucho claor
      temperatura=float(input("Ingresa la temeperatura que hay en el ambiente: "))
      if temperatura >=35:
      print("Hace demaciado calor")
      else:
      print("No hace tanto calor")