class PersonaRepository:
    def __init__(self):
        self._personas = {}

    def guardar(self, persona):
        self._personas[persona.dni] = persona

    def buscar_por_dni(self, dni):
        return self._personas.get(dni)

    def buscar_todas(self):
        return list(self._personas.values())

    def eliminar(self, dni):
        self._personas.pop(dni, None)