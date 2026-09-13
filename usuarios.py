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


class Profesor(Usuario):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limite_prestamos = None  # Los profesores no tienen límite de préstamos

    def solicitar_libro(self, titulo):
        return f"Solicitud de libro: {titulo}, realizada"


estudiante = Estudiante("Alice", "123456789", "Ingeniería")
profesor = Profesor("Bob", "987654321")

print(estudiante.solicitar_libro("Cien Años de Soledad"))
print(estudiante.solicitar_libro("Don Quijote de la Mancha"))
print(estudiante.solicitar_libro("Harry Potter y la Piedra Filosofal"))
print(estudiante.solicitar_libro("El Principito"))  # Debería indicar
print(profesor.solicitar_libro("El Quijote"))
