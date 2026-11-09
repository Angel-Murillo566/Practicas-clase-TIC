#Programa que agrega peliculas en una lista
#Ponerle nombre a mi lista
peliculas=[]
#Preguntar cuantas peliculas
cantidad_de_peliculas=int(input("Cuantas pelicualas vas a agreagar"))
i=0
while i<cantidad_de_peliculas:
    peli=input("Ingresa la pelicula:")
    #Preguntar pelicula
    peliculas.append(peli)
    #Muestra la lista
    print(peliculas)
    i=i+1
#Buscar una pelicula en la lista
#Pregutar la pelicula a buscar
pelibuscar=input("Que pelicula buscas")
if pelibuscar in peliculas:
    print("Si esta")
else:
    print("No etsa la pelicula amigo")
    peliculas.append(pelibuscar)
    print(peliculas)