import sqlite3
from core.tipos_clientes import ClientePremium, ClienteCorporativo
from core.excepciones import DatabaseError
from logs.gestor_logs import registrar_evento, registrar_error

class DBManager:
    def __init__(self, db_name="database/clientes.db"):
        self.db_name = db_name
        self._crear_tabla() # 

    def _conectar(self):
        """Establece la conexión con la base de datos SQLite[cite: 30]."""
        return sqlite3.connect(self.db_name)

    def _crear_tabla(self):
        """Crea la tabla de clientes si no existe[cite: 19, 37]."""
        query = """
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            telefono TEXT,
            tipo TEXT,
            extra_info TEXT
        )
        """
        try:
            with self._conectar() as conn:
                conn.execute(query)
        except sqlite3.Error as e:
            registrar_error(f"Error al crear tabla: {e}") 

    def guardar_cliente(self, cliente):
        """Guarda un objeto cliente en la base de datos[cite: 28]."""
        extra = ""
        # Polimorfismo para guardar datos específicos 
        if isinstance(cliente, ClientePremium):
            extra = f"Descuento: {cliente.descuento}%"
        elif isinstance(cliente, ClienteCorporativo):
            extra = f"Empresa: {cliente.empresa}"
        
        query = "INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?)"
        try:
            with self._conectar() as conn:
                conn.execute(query, (cliente.id_cliente, cliente.nombre, 
                                   cliente.email, cliente.telefono, 
                                   cliente.tipo, extra))
                registrar_evento(f"Cliente guardado: {cliente.nombre}") 
        except sqlite3.IntegrityError:
            registrar_error("Error de duplicación de ID o Email") 
            raise DatabaseError("El ID o Email ya existe.") 

    def obtener_todos(self):
        """
        Recupera todos los registros para mostrarlos en la GUI.
        Este es el método que faltaba y causaba el error.
        """
        query = "SELECT * FROM clientes"
        try:
            with self._conectar() as conn:
                cursor = conn.execute(query)
                return cursor.fetchall()
        except sqlite3.Error as e:
            registrar_error(f"Error al recuperar datos: {e}") 
            return []