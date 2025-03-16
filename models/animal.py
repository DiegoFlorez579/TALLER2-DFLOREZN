from models.ianimal import IAnimal

class Animal(IAnimal):
    def __init__(self, nombre: str, peso: float, edad: int) -> None:
        self.__nombre = nombre
        self.__peso = peso
        self.__edad = edad
        self.__kilos_comidos = 0

    def cambiar_kilos_comidos(self, kilos_comidos:int) -> None:
        self.__kilos_comidos = kilos_comidos
    
    def cambiar_nombre(self, nombre: str) -> None:
        self.__nombre = nombre
    
    def cambiar_peso(self, peso:float) -> None:
        self.__peso = peso
    
    def cambiar_edad(self, edad: int) -> None:
        self.__edad = edad
    
    def obtener_kilos_comidos(self) -> int:
        return self.__kilos_comidos
    
    def obtener_nombre(self) -> str:
        return self.__nombre
    
    def obtener_peso(self) -> float:
        return self.__peso
    
    def obtener_edad(self) -> int:
        return self.__edad
    
    def comer(self, kilos:int) -> None:
        self.__kilos_comidos+=kilos

    @staticmethod
    def hacer_sonido():
        pass