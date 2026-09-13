def SolicitanteProtocol(Protocol):
    def solicitar_libro(self, titulo: str) -> str:
        """Meotodo que debe implementar cualquier clase que desee ser un Solicitante de libros."""


class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []  # Lista para almacenar los libros prestados

    def solicitar_libro(self, titulo):
        return "Solicitud de libro: {titulo}, realizada"


class Estudiante(Usuario):
    def __init__(self, nombre, cedula, carrera):
        super().__init__(
            nombre, cedula
        )  # llama métodos de la clase padre sin necesidad de repetir código
        self.carrera = carrera
        self.limite_prestamos = 3

    def solicitar_libro(self, titulo):
        if len(self.libros_prestados) < self.limite_prestamos:
            self.libros_prestados.append(titulo)
            return f"Solicitud de libro: {titulo}, realizada"
        else:
            return "Límite de préstamos alcanzado. No se puede solicitar más libros."

    def devolver_libro(self, titulo):
        if titulo in self.libros_prestados:
            self.libros_prestados.remove(titulo)
            return f"Libro {titulo} devuelto."
        else:
            return f"No se puede devolver {titulo}. No está en la lista de libros prestados."


class Profesor(Usuario):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limite_prestamos = None  # Los profesores no tienen límite de préstamos

    def solicitar_libro(self, titulo):
        return f"Solicitud de libro: {titulo}, realizada"


estudiante_1 = Estudiante("Juan Pérez", "123456789", "Ingeniería de Sistemas")
estudiante_2 = Estudiante("María Gómez", "987654321", "Medicina")
estudiante_3 = Estudiante("Carlos López", "456789123", "Derecho")
profesor_1 = Profesor("Dr. Ana Torres", "111222333")

usuarios = [estudiante_1, estudiante_2, estudiante_3, profesor_1]

for usuario in usuarios:
    print(usuario.solicitar_libro("Cien Años de Soledad"))
