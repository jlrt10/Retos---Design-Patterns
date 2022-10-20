# Topic A = Vehicles
# Pattern B = Factory Method

from __future__ import annotations
from abc import ABC, abstractmethod

#Creator
class Fabrica(ABC):
    @abstractmethod
    def fabrica(self):
        pass

    def solicitar_ensamble(self) -> str:
        vehiculo = self.fabrica()
        result = f"Fabrica: {vehiculo.ensamblar()} satisfactoriamente"
        return result

#Concrete Creator
class EnsamblarCarro(Fabrica):
    def fabrica(self) -> Vehiculo:
        return Carro()

class EnsamblarMoto(Fabrica):
    def fabrica(self) -> Vehiculo:
        return Moto()

class EnsamblarAvion(Fabrica):
    def fabrica(self) -> Vehiculo:
        return Avion()

#Product
class Vehiculo(ABC):
    @abstractmethod
    def ensamblar(self) -> str:
        pass

#Concrete Product
class Carro(Vehiculo):
    def ensamblar(self) -> str:
        return "El carro ha sido ensamblado"

class Moto(Vehiculo):
    def ensamblar(self) -> str:
        return "La moto ha sido ensamblada"

class Avion(Vehiculo):
    def ensamblar(self) -> str:
        return "El avión ha sido ensamblado"

#Main
def solicitud(fabrica: Fabrica) -> None:
    print(f"Concesionario: Se solicita a la fabrica el proceso de ensamble del vehiculo.\n"
          f"{fabrica.solicitar_ensamble()}", end="")

if __name__ == "__main__":
    print("Vendedor: Se ha vendido un carro.")
    solicitud(EnsamblarCarro())
    print("\n")
    print("Vendedor: Se ha vendido una moto.")
    solicitud(EnsamblarMoto())
    print("\n")
    print("Vendedor: Se ha vendido un avión.")
    solicitud(EnsamblarAvion())
    print("\n")