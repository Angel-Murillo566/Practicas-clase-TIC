numeros=[]
resultados=[]
i=0
while i<5:
    num=int(input("Ingresa un numero"))
    numeros.append(num)
    i=i+1
multiplicador=int(input("Por cuando deseas multiplicar?? "))
for num in numeros:
    resultado=num*multiplicador
    resultados.append(resultado)
print("Numeros originales: ",numeros)
print("Resultado:",resultado)
numbuscar=int(input("¿Que numero buscas?: "))
if numbuscar in numeros:
    print("Si esta el numero")
else:
    print("No esta el numero")
    