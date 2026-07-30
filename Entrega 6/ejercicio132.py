class ArticuloCientifico:
    

    def __init__(
        self,
        titulo,
        autor,
        palabras_claves=None,
        publicacion=None,
        año=None,
        resumen=None,
    ):
        # 1. Atributos obligatorios (Primer constructor)
        self.titulo = titulo
        self.autor = autor

        # 2. Atributos opcionales (Segundo constructor)
        self.palabras_claves = (
            palabras_claves if palabras_claves is not None else []
        )
        self.publicacion = publicacion
        self.año = año

        # 3. Atributo adicional (Tercer constructor)
        self.resumen = resumen

    def imprimir(self):
        """Imprime en pantalla los datos del artículo científico."""
        print(f"Titulo del artículo = {self.titulo}")
        print(f"Autor del artículo = {self.autor}")
        print("Palabras clave = ")

        # Recorre la lista de palabras clave
        if self.palabras_claves:
            for palabra in self.palabras_claves:
                print(palabra)

        print(f"Publicación = {self.publicacion}")
        print(f"Año = {self.año}")
        print(f"Resumen = {self.resumen}")


# Main
if __name__ == "__main__":
    # Creación del arreglo de palabras clave
    palabras = ["Fisica", "Espacio", "Tiempo"]

    # Instanciación usando el equivalente al "tercer constructor"
    articulo = ArticuloCientifico(
        "La teoría especial de la relatividad",
        "Albert Einstein",
        palabras,
        "Anales de Fisica",
        1913,
        "Las leyes de la fisica son las mismas en todos los sistemas de referencia inerciales.",
    )

    # Imprimir datos
    articulo.imprimir()