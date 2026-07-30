class Profesor:

    def imprimir(self):
        print("Es un profesor.")


class ProfesorTitular(Profesor):
    #Subclase que hereda de Profesor y sobrescribe el método imprimir


    def imprimir(self):
        # Sobrescribe el método de la clase padre
        print("Es un profesor titular.")


# Prueba 
if __name__ == "__main__":
    # Polimorfismo: la variable 'profesor1' hace referencia
    # a un objeto de la clase hija (ProfesorTitular)
    profesor1: Profesor = ProfesorTitular()

    # Se ejecuta el método de ProfesorTitular
    profesor1.imprimir()