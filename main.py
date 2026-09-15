from typing import Protocol

from biblioteca import Biblioteca
from libros import LibroFisico
from usuarios import Estudiante, Profesor, SolicitanteProtocol

biblioteca = Biblioteca("Platzi Biblioteca")


class LibroProtocol(Protocol):
    def prestar(self) -> str:
        """Método de prestar un libro"""
        ...

    def devolver(self) -> str:
        """Método de devolver un libro"""
        ...

    def calcular_duracion(self) -> str:
        """Calcula el tiempo de prestamo"""
        ...


class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.__veces_prestado = 0

    def __str__(self):
        return f"{self.titulo} por {self.autor} disponible: {self.disponible}"

    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.__veces_prestado += 1
            return f"'{self.titulo}' prestado exitosamente. Total préstamos: {self.__veces_prestado}"
        return f"'{self.titulo}' no está disponible"

    def devolver(self):
        self.disponible = True
        return f"'{self.titulo}' devuelto y disponible nuevamente"

    def es_popular(self):
        return self.__veces_prestado > 5

    def get_veces_prestado(self):
        return self.__veces_prestado

    def set_veces_prestado(self, veces_prestado):
        self.__veces_prestado = veces_prestado


class LibroFisico(Libro):
    def calcular_duracion(self):
        return "7 días"


class LibroDigital(Libro):
    def calcular_duracion(self):
        return "14 días"


class Biblioteca:
    def __init__(self, name) -> None:
        self.name = name
        self.libros = []
        self.usuarios = []

    def libros_disponibles(self):
        return [libro.titulo for libro in self.libros if libro.disponible]


estudiante = Estudiante("Luis", "1123123123", "Sistemas")
estudiante_1 = Estudiante("Jose", "56789", "Salud")
profesor = Profesor("Felipe", "123123123")
usuarios: list[SolicitanteProtocol] = [estudiante, estudiante_1, profesor]


mi_libro = LibroFisico("Python básico", "Ana López", "978-1")
mi_libro_no_disponible = LibroFisico(
    "Programación orientada a objetos",
    "Carlos Pérez",
    "978-2",
    disponible=False,
)
otro_libro = LibroDigital("Introducción a la informática", "María García", "978-3")

biblioteca = Biblioteca("Platzi Biblioteca")

biblioteca.libros = [mi_libro, mi_libro_no_disponible, otro_libro]
print(biblioteca.libros_disponibles())


print(biblioteca.libros)
