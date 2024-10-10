#imprime los datos de la autora
print("JIMENEZ GAMBOA ISSIS ALEXA")
print("no.1189")
print("3W")
#imprime una linea en blanco 
print("")

#3.Función que calcula el factorial de un entero positivo
def factorial(n):
    if n < 0:
        return "Número debe ser positivo"
    elif n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

#Ejemplo de uso
if __name__ == "__main__":
    print(factorial(5))  #Imprime el factorial de 5