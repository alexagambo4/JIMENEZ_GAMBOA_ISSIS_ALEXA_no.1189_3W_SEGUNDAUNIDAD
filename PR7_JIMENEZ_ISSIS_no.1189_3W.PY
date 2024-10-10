#imprime los datos de la autora
print("JIMENEZ GAMBOA ISSIS ALEXA")
print("no.1189")
print("3W")
#imprime una linea en blanco 
print("")
#7.Longitud de la última palabra
def longitud_ultima_palabra(texto):
    palabras = texto.strip().split()
    if palabras:
        return len(palabras[-1])
    return 0
#Ejemplo de uso 
print(longitud_ultima_palabra("Hola mundo!"))  #Imprime la longitud de la última palabra