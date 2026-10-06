from models.persona import Persona

class PersonaService:
    def __init__(self, repo):
        self.repo = repo

    def listar(self):
        return self.repo.buscar_todas()

    def obtener(self, dni):
        persona = self.repo.buscar_por_dni(dni)
        if persona is None:
            raise LookupError("Persona no encontrada")
        return persona

    def crear(self, dni, nombre):
        if self.repo.buscar_por_dni(dni):
            raise ValueError("Ya existe una persona con ese DNI")
        persona = Persona(dni, nombre)
        self.repo.guardar(persona)
        return persona

    def modificar(self, dni, nombre):
        persona = self.obtener(dni)
        persona.nombre = nombre
        self.repo.guardar(persona)
        return persona

    def eliminar(self, dni):
        self.obtener(dni)
        self.repo.eliminar(dni)