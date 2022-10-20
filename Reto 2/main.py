# Topic A = Food
# Pattern B = Bridge

from __future__ import annotations
from abc import ABC, abstractmethod

#Abstraction
class Pizza:
    def __init__(self, ingredientes: Ingredientes) -> None:
        self.ingredientes = ingredientes

    def solicitar_preparacion(self) -> str:
        return (f"Pizza de {self.ingredientes.adicion()} en masa delgada")

#Refined Abstraction
class PizzaGruesa(Pizza):
    def solicitar_preparacion(self) -> str:
        return (f"Pizza de {self.ingredientes.adicion()} en masa gruesa")

#Implementation
class Ingredientes(ABC):
    @abstractmethod
    def adicion(self) -> str:
        pass

#Concrete Implementation
class Pollo(Ingredientes):
    def adicion(self) -> str:
        return "Adición de pollo"

class Pepperoni(Ingredientes):
    def adicion(self) -> str:
        return "Adición de pepperoni"

#Main
def preparacion(pizza: Pizza) -> None:
    print(pizza.solicitar_preparacion(), end="")

if __name__ == "__main__":
    proteina = Pollo()
    producto = Pizza(proteina)
    preparacion(producto)
    print("\n")
    proteina = Pepperoni()
    producto = PizzaGruesa(proteina)
    preparacion(producto)
    print("\n")