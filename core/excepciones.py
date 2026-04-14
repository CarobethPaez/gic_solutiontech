class GICError(Exception):
    """Clase base para excepciones del Gestor Inteligente de Clientes."""
    pass

class ValidationError(GICError):
    """Se lanza cuando un atributo (email, tel) no cumple el formato."""
    pass

class DatabaseError(GICError):
    """Se lanza cuando hay problemas con SQLite."""
    pass