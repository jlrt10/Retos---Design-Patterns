# Topic A = Services
# Pattern B = Command

from __future__ import annotations
from abc import ABC, abstractmethod

#Command
class Comando(ABC):
    @abstractmethod
    def ejecutar(self) -> None:
        pass

#Application
class SubirRecursos(Comando):
    def __init__(self, sincronizarRecursos: SincronizarRecursos, bd: str, app: str) -> None:
        self._bd = bd
        self._app = app
        self._sincronizarRecursos = sincronizarRecursos

    def ejecutar(self) -> None:
        print(f"Tareas en ejecución: \nSubiendo {self._bd} - Subiendo {self._app} - [DONE]")
        print("Iniciando sincronización de recursos... ")
        print("Tareas en ejecución: ", end="")
        self._sincronizarRecursos.sincronizar_bd(self._bd)
        self._sincronizarRecursos.sincronizar_app(self._app)
        print("[DONE]")

class BajarRecursos(Comando):
    def __init__(self, bd: str, app: str) -> None:
        self._bd = bd
        self._app = app

    def ejecutar(self) -> None:
        print(f"Tareas en ejecución: \nBajando {self._bd} - Bajando {self._app} - [DONE]")

class SincronizarRecursos:
    def sincronizar_bd(self, bd: str) -> None:
        print(f"Sincronizando {bd} - ", end="")

    def sincronizar_app(self, app: str) -> None:
        print(f"Sincronizando {app} - ", end="")

class Servicios:
    _subir_servicios = None
    _bajar_servicios = None

    def subir_servicios(self, comando: Comando):
        self._subir_servicios = comando

    def bajar_servicios(self, comando: Comando):
        self._bajar_servicios = comando

    def acciones(self) -> None:
        print("Inicializando sistema...")
        if isinstance(self._subir_servicios, Comando):
            self._subir_servicios.ejecutar()

        print("Sistema inicializado\n")
        print("Cerrando sistema")

        if isinstance(self._bajar_servicios, Comando):
            self._bajar_servicios.ejecutar()

        print("Sistema detenido") 

#Main
if __name__ == "__main__":
    servicios = Servicios()
    sincronizarRecursos = SincronizarRecursos()
    servicios.subir_servicios(SubirRecursos(sincronizarRecursos, "base de datos", "servidor de aplicaciones"))    
    servicios.bajar_servicios(BajarRecursos("base de datos", "servidor de aplicaciones"))
    servicios.acciones()