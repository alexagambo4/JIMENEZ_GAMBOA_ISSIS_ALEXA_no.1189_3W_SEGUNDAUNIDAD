#imprime los datos de la autora
print("JIMENEZ GAMBOA ISSIS ALEXA")
print("no.1189")
print("3W")
#imprime una linea en blanco 
print("")

#6.Verificar dirección de email
def validar_email(email):
    if "@" in email and email.count("@") == 1 and email.endswith(".com"):
        return "Email válido"
    else:
        return "Email inválido"
print(validar_email("ejemplo@dominio.com"))  #Verifica si el email es válido