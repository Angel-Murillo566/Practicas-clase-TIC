sexo=input("Ingresa tu sexo: ")
edad=int(input("Ingresa tu edad: "))
estado_civil=input("Ingresa tu estado civil: ")
cantidad_de_hijos=int(input("Cuantos hijos tienes: "))
if sexo=="Mujer" and cantidad_de_hijos>1 and edad<18:
    print("Eres mujer, tienes más de un hijo y eres menor de edad entonces el apoyo es de $1500")
elif sexo=="Mujer" and cantidad_de_hijos>1 and edad>=18:
    print("Eres mujer, tines más de un hijo y ya eres mayor de edad entonces tu opoyo es de $500")
elif sexo=="Hombre" and cantidad_de_hijos>=1 and estado_civil=="Soltero":
    print ("Eres hombre y tienes hijos el apoyo es de $780")
else:
    print("No valido")