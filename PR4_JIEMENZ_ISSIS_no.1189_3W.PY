#imprime los datos de la autora
print("JIMENEZ GAMBOA ISSIS ALEXA")
print("no.1189")
print("3W")
#imprime una linea en blanco 
print("")

#4.Calcular total de una factura luego del IVA
def factura_total(cantidad_sin_iva, porcentaje_iva=21):
    total_iva = cantidad_sin_iva * (porcentaje_iva / 100)
    total = cantidad_sin_iva + total_iva
    return total
#Ejemplo de uso

print(factura_total(100))  #Imprime el total de una factura de 100 con IVA