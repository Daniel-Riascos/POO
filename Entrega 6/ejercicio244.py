from abc import ABC, abstractmethod

# Clase Raíz: Animal
class Animal(ABC):
    """Clase abstracta que modela un animal genérico."""

    def __init__(self):
        self._sonido: str = None
        self._alimentos: str = None
        self._habitat: str = None
        self._nombre_cientifico: str = None

    @abstractmethod
    def get_nombre_cientifico(self) -> str:
        """Obtiene el nombre científico del animal."""
        pass

    @abstractmethod
    def get_sonido(self) -> str:
        """Obtiene el sonido emitido por el animal."""
        pass

    @abstractmethod
    def get_alimentos(self) -> str:
        """Obtiene los alimentos que consume el animal."""
        pass

    @abstractmethod
    def get_habitat(self) -> str:
        """Obtiene el hábitat del animal."""
        pass



# Subclases Animal
class Canido(Animal, ABC):
    """Clase abstracta que representa a la familia de los cánidos."""

    pass


class Felino(Animal, ABC):
    """Clase abstracta que representa a la familia de los felinos."""

    pass


# Subclases Cánido
class Perro(Canido):
    """Clase concreta que representa a un Perro."""

    def get_sonido(self) -> str:
        return "Ladrido"

    def get_alimentos(self) -> str:
        return "Carnívoro"

    def get_habitat(self) -> str:
        return "Doméstico"

    def get_nombre_cientifico(self) -> str:
        return "Canis lupus familiaris"


class Lobo(Canido):
    """Clase concreta que representa a un Lobo."""

    def get_sonido(self) -> str:
        return "Aullido"

    def get_alimentos(self) -> str:
        return "Carnívoro"

    def get_habitat(self) -> str:
        return "Bosque"

    def get_nombre_cientifico(self) -> str:
        return "Canis lupus"


# Subclases Felino
class Leon(Felino):
    """Clase concreta que representa a un León."""

    def get_sonido(self) -> str:
        return "Rugido"

    def get_alimentos(self) -> str:
        return "Carnívoro"

    def get_habitat(self) -> str:
        return "Praderas"

    def get_nombre_cientifico(self) -> str:
        return "Panthera leo"


class Gato(Felino):
    """Clase concreta que representa a un Gato."""

    def get_sonido(self) -> str:
        return "Maullido"

    def get_alimentos(self) -> str:
        return "Ratones"

    def get_habitat(self) -> str:
        return "Doméstico"

    def get_nombre_cientifico(self) -> str:
        return "Felis silvestris catus"


# Clase Prueba
if __name__ == "__main__":
    animales: list[Animal] = [Gato(), Perro(), Lobo(), Leon()]

    # Recorrido del vector e impresión de los métodos polimórficos
    for animal in animales:
        print(animal.get_nombre_cientifico())
        print(f"Sonido: {animal.get_sonido()}")
        print(f"Alimentos: {animal.get_alimentos()}")
        print(f"Hábitat: {animal.get_habitat()}")
        print()