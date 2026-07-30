class Pedido:
    

    def calcular_pedido(self, *args):
        # Caso 1: Primer plato + Bebida 
        if len(args) == 4:
            primer_plato, costo_primer_plato, bebida, costo_bebida = args
            total = costo_primer_plato + costo_bebida
            print(f"El costo de {primer_plato} y {bebida} es = ${total}")

        # Caso 2: Primer plato + Segundo plato + Bebida 
        elif len(args) == 6:
            (
                primer_plato,
                costo_primer_plato,
                segundo_plato,
                costo_segundo_plato,
                bebida,
                costo_bebida,
            ) = args
            total = costo_primer_plato + costo_segundo_plato + costo_bebida
            print(
                f"El costo de {primer_plato} + {segundo_plato} + {bebida} es = ${total}"
            )

        # Caso 3: Primer plato + Segundo plato + Postre + Bebida 
        elif len(args) == 8:
            (
                primer_plato,
                costo_primer_plato,
                segundo_plato,
                costo_segundo_plato,
                postre,
                costo_postre,
                bebida,
                costo_bebida,
            ) = args
            total = (
                costo_primer_plato
                + costo_segundo_plato
                + costo_bebida
                + costo_postre
            )
            print(
                f"El costo de {primer_plato} + {segundo_plato} + {bebida} + {postre} es = ${total}"
            )


#  Método Main 
if __name__ == "__main__":
    # Pedido 1: Plato principal y bebida
    pedido1 = Pedido()
    pedido1.calcular_pedido("Sancocho", 5000, "Gaseosa", 2000)

    # Pedido 2: Primer plato, segundo plato y bebida
    pedido2 = Pedido()
    pedido2.calcular_pedido(
        "Crema de verduras", 5000, "Churrasco", 6000, "Gaseosa", 2000
    )

    # Pedido 3: Primer plato, segundo plato, postre y bebida
    pedido3 = Pedido()
    pedido3.calcular_pedido(
        "Crema de espinacas",
        5000,
        "Salmón",
        10000,
        "Tiramisú",
        5000,
        "Gaseosa",
        2000,
    )