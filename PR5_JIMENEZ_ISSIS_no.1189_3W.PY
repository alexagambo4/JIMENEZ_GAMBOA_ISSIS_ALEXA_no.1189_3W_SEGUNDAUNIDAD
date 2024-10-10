#imprime los datos de la autora
print("JIMENEZ GAMBOA ISSIS ALEXA")
print("no.1189")
print("3W")
#imprime una linea en blanco 
print("")


#5.Función que calcula el área y volumen de un círculo y cilindro
def area_circulo(radio):
    return pow.pi * radio ** 2

def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura

#Ejemplo de uso

print(area_circulo(5))  #Imprime el área de un círculo con radio 5
print(volumen_cilindro(5, 10))  #Imprime el volumen de un cilindro con radio 5 y altura 10