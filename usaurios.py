from typing import Protocol


class LibroProtocol(Protocol):
    def prestar(self) -> str: ...

    def calcular_duracion(self) -> str: ...


class Libro:
    def __init__(
        self, titulo: str, autor: str, isbn: str, disponible: bool = True
    ) -> None:
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def __str__(self) -> str:
        return f"{self.titulo} por {self.autor} disponibilidad: {self.disponible}"

    def prestar(self) -> str:
        if self.disponible:
            self.disponible = False
        return f"el libro {self.titulo} ha sido prestado exitosamente!"

    def devolver(self) -> str:
        if not self.disponible:  # == False:
            self.disponible = True
        return f"el libro {self.titulo} ha sido devuelto y ahora está disponible!"


# LibroFisico
class LibroFisico:
    def __init__(
        self, titulo: str, autor: str, isbn: str, disponible: bool = True
    ) -> None:
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def prestar(self) -> str:
        if self.disponible:
            self.disponible = False
        return f"el libro físico {self.titulo} ha sido prestado exitosamente!"

    def calcular_duracion(self) -> str:
        DURACION_PRESTAMO_FISICO = 4
        return (
            f"el libro físico tiene una vigencia de '{DURACION_PRESTAMO_FISICO}' días"
        )

    def devolver(self) -> str:
        if not self.disponible:
            self.disponible = True
        return f"el libro {self.titulo} ha sido devuelto y ahora está disponible!"


# LibroElectronico
class LibroElectronico:
    def __init__(
        self, titulo: str, autor: str, isbn: str, disponible: bool = True
    ) -> None:
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def prestar(self) -> str:
        if self.disponible:
            self.disponible = False
        return f"el libro digital {self.titulo} ha sido prestado exitosamente!"

    def calcular_duracion(self) -> str:
        DURACION_PRESTAMO_DIGITAL = 8
        return (
            f"el libro digital tiene una vigencia de '{DURACION_PRESTAMO_DIGITAL}' días"
        )

    def devolver(self) -> str:
        if not self.disponible:  # == False:
            self.disponible = True
        return f"el libro {self.titulo} ha sido devuelto y ahora está disponible!"


mi_libro_fisico = LibroFisico(
    "El principito", "Saint-Exupéry", "978-84-376-0494-8", True
)
mi_libro_elctron = LibroElectronico(
    "Control", "Freddy Vega", "978-84-376-0494-10", True
)


catalogo_libros: list[LibroProtocol] = [mi_libro_fisico, mi_libro_elctron]

for catalogo in catalogo_libros:
    print(catalogo.prestar())
    print(catalogo.calcular_duracion())
