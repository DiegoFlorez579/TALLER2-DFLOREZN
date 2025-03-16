from models.animal_exotico import Animal_Exotico

class Huron(Animal_Exotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos:float) -> None:
        super().__init__(nombre, peso, edad, pais_origen, impuestos)

    @staticmethod
    def hacer_sonido() -> str:
        return('Eek Eek!')
