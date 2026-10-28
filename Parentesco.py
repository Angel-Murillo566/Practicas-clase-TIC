parentesco=input("¿Que eres mio? ")
if parentesco=="Hermano" or parentesco=="Papá" or parentesco=="Hermana" or parentesco=="Mamá":
    print("Eres de mi familia")
else:
    print("No eres de mi familia")
print("///////////////////////////")
edad=int(input("¿Que edad tienes? "))
permiso=input("Tienes permiso de entrar? ")
acompañamiento=input("Tienes acompañamiento? ")
if edad>=18 or permiso=="Si"or acompañamiento=="Si":
    print("Puedes entrar al concierto")
else:
     print("No puedes entrar al concierto")