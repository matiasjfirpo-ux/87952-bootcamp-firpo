class Persona:
    def __init__(self, dni: int, nombre: str):
        self.dni = dni
        self.nombre = nombre

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor: int):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("El DNI debe ser un número entero positivo")
        self._dni = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not isinstance(valor, str) or not valor:
            raise ValueError("El nombre no puede estar vacío")
        if len(valor) > 30:
            raise ValueError("El nombre no puede tener más de 30 caracteres")
        if not valor[0].isupper() or valor[1:] != valor[1:].lower():
            raise ValueError(
                "El nombre debe comenzar con mayúscula y el resto en minúscula"
            )
        self._nombre = valor

    def to_dict(self):
        return {"dni": self.dni, "nombre": self.nombre}