from typing import Protocol

from main import Libro


class SolicitanteProtocol(Protocol):
    def solicitar_libro(self, titulo: str) -> str: ...


class Estudiante:
    def __init__(self, nombre, cedula, carrera):
        self.nombre = nombre
        self.cedula = cedula
        self.carrera = carrera
        self.libros_prestados = []

    def solicitar_libro(self, titulo):
        self.libros_prestados.append(titulo)
        return f"Prestamo del libro: {titulo} autorizado"


class Profesor:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []

    def solicitar_libro(self, titulo):
        self.libros_prestados.append(titulo)
        return f"Prestamo del libro: {titulo} autorizado"


estudiante = Estudiante("Luis", "1123123123", "Sistemas")
estudiante_1 = Estudiante("Jose", "56789", "Salud")
profesor = Profesor("Felipe", "123123123")
# Este no se puede agregar en el listado porque no cumple el protocolo.
libro = Libro("Titlo de prueba", "Autor de prueba", isbn="123123")

usuarios: list[SolicitanteProtocol] = [estudiante, estudiante_1, profesor]

for usuario in usuarios:
    print(usuario.solicitar_libro("Titulo de ejemplo"))
