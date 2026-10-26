Nombre_Empleado=input("Ingresa tu nobre: ")
Pago_por_hora=float(input("Ingresa tu pago por hora: "))
Horas_trabajadas_al_mes=float(input("Ingresa tus horas trabajadas al mes: "))
Sueldo=Pago_por_hora*Horas_trabajadas_al_mes
print (f"Tu sueldo es de {Sueldo}")
if Sueldo>=100 and Sueldo<=300:
    Sueldo_Bono1=Sueldo+500
    print(f"Tu sueldo con bono es de {Sueldo_Bono1}")
elif Sueldo>=300 and Sueldo<=1500:
    Sueldo_Bono2=Sueldo+1700
    print(f"Tu sueldo con bono es de {Sueldo_Bono2}")
elif Sueldo>=1500 and Sueldo<=3000:
    Sueldo_Bono3=Sueldo+3500
    print(f"Tu sueldo con bono es de {Sueldo_Bono3}")
elif Sueldo>=3000 and Sueldo<=8000:
    Sueldo_Bono4=Sueldo+8500
    print(f"Tu sueldo con bono es de {Sueldo_Bono4}")
elif Sueldo>8000:
    Sueldo_Bono5=Sueldo+10000
    print(f"Tu sueldo con bono es de {Sueldo_Bono5}")
else: 
    print("No valido")