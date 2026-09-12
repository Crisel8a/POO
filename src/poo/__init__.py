class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


mi_libro = Libro("El Principito", "Antoine de Saint-Exupéry", 96)
otro_libro = Libro("1984", "George Orwell", 328)

print(
    f"Mi libro favorito es '{mi_libro.titulo}' de {mi_libro.autor}, que tiene {mi_libro.paginas} páginas."
)
print(
    f"Otro libro es '{otro_libro.titulo}' de {otro_libro.autor}, que tiene {otro_libro.paginas} páginas."
)
