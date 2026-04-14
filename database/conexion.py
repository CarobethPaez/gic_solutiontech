import sqlite3
from core.excepciones import DatabaseError
from logs.gestor_logs import registrar_evento, registrar_error

class DBManager:
    def __init__(self, db_name="database/clientes.db"):
        self.db_name = db_name
        self._crear_tabla()

    def _conectar(self):
        """Establece conexión con SQLite."""
        return sqlite3.connect(self.db_name)

    def guardar_cliente(self, cliente):
        query = "INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?)"
        try:
            with self._conectar() as conn:
                conn.execute(query, (cliente.id_cliente, cliente.nombre, cliente.email, cliente.telefono, cliente.tipo, "N/A"))
                registrar_evento(f"Cliente creado: {cliente.nombre} (ID: {cliente.id_cliente})")
        except sqlite3.IntegrityError as e:
            msg = f"Error de integridad en BD al guardar ID {cliente.id_cliente}: {e}"
            registrar_error(msg)
            raise DatabaseError(msg)
        except Exception as e:
            registrar_error(f"Error inesperado: {e}")
            raise DatabaseError("No se pudo completar la operación en la base de datos.")