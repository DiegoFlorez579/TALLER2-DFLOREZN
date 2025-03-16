from models.animal import Animal

class Animal_Exotico(Animal):
    def __init__(self, nombre: str, peso: float, edad: int, pais_origen: str, impuestos: float) -> None:
        super().__init__(nombre, peso, edad)
        self.__pais_origen = pais_origen
        self.__impuestos = impuestos
    
    def cambiar_pais_origen(self, pais_origen: str) -> None:
        self.__pais_origen = pais_origen
    
    def cambiar_impuestos(self, impuestos: float) -> None:
        self.__impuestos = impuestos

    def obtener_pais_origen(self) -> str:
        return self.__pais_origen
    
    def obtener_impuestos(self) -> float:
        return self.__impuestos

    def calcular_flete(self) -> float:
        return (self.__impuestos * self.__peso)