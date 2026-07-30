class Profesor:

    def imprimir(self):
        print("Es un profesor.")


class ProfesorTitular(Profesor):
    """Subclase ProfesorTitular."""

    def __init__(self, años: int = 0):
        self.años = años

    def imprimir(self):
        print("Es un profesor titular.")

    def imprimir_años(self):
        print(f"Años = {self.años}")


# Clase Prueba3
if __name__ == "__main__":
    # Polimorfismo: instancia de ProfesorTitular
    profesor1: Profesor = ProfesorTitular()

    # Invocación del método exclusivo de ProfesorTitular
    profesor1.imprimir_años()