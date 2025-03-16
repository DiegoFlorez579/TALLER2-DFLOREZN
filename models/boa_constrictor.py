from models.animal_exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos:float) -> None:
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.__ratones_comidos = 0

    @staticmethod
    def hacer_sonido() -> str:
        return('Tsss!')

    def comer_raton(self, ratones_comidos) -> None:
        self.__ratones_comidos += ratones_comidos

    def obtener_ratones_comidos(self) -> int:
        return self.__ratones_comidos