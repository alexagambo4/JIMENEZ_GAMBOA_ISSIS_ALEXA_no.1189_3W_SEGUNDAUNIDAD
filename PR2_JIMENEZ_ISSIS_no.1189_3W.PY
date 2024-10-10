#imprime los datos de la autora
print("JIMENEZ GAMBOA ISSIS ALEXA")
print("no.1189")
print("3W")
#imprime una linea en blanco 
print("")


#2.Función que despliega un saludo con un nombre
def saludo_personalizado(nombre: str) -> str:
    return f"¡Hola {nombre}!"  #Retorna un saludo personalizado utilizando el nombre dado
#Ejemplo de uso
if __name__ == "__main__":
    print(saludo_personalizado("Juan"))  #Imprime un saludo personalizado para Juan