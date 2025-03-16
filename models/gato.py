from models.animal import Animal

class Gato(Animal):
    def __init__(self, nombre: str, peso: float, edad: int) -> None:
        super().__init__(nombre, peso, edad)

    @staticmethod
    def hacer_sonido() -> str:
        return('Miau Miau!')
