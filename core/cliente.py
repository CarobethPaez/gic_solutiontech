import re

class Cliente:
    def __init__(self, id_cliente, nombre, email, telefono):
        self.__id = id_cliente # Atributo privado 
        self.nombre = nombre
        self.__email = self.validar_email(email)
        self.__telefono = self.validar_telefono(telefono)

    @property
    def id_cliente(self):
        return self.__id

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nuevo_email):
        self.__email = self.validar_email(nuevo_email)

    def validar_email(self, email):
        # Validación avanzada solicitada 
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if not re.match(regex, email):
            raise ValueError(f"Email no válido: {email}")
        return email

    def validar_telefono(self, telefono):
        # Aseguramos que solo sean números y largo mínimo 
        tel_limpio = re.sub(r'\D', '', str(telefono))
        if len(tel_limpio) < 8:
            raise ValueError("El teléfono debe tener al menos 8 dígitos.")
        return tel_limpio

    def __str__(self): # Método especial para representar el objeto como cadena
        return f"ID: {self.__id} | Nombre: {self.nombre} | Email: {self.__email}"