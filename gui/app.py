import tkinter as tk
from tkinter import messagebox, ttk
from database.conexion import DBManager
from core.tipos_clientes import ClienteRegular
from logs.gestor_logs import registrar_evento

class GICApp:
    def __init__(self, root):
        self.db = DBManager()
        self.root = root
        self.root.title("SolutionTech - Gestor Inteligente de Clientes")
        self.root.geometry("700x500")

        # --- Componentes de la Interfaz ---
        self._crear_formulario()
        self._crear_tabla()
        self._cargar_datos()

    def _crear_formulario(self):
        frame = tk.LabelFrame(self.root, text="Nuevo Cliente", padx=10, pady=10)
        frame.pack(fill="x", padx=20, pady=10)

        # Campos de entrada
        tk.Label(frame, text="ID:").grid(row=0, column=0)
        self.ent_id = tk.Entry(frame)
        self.ent_id.grid(row=0, column=1)

        tk.Label(frame, text="Nombre:").grid(row=0, column=2)
        self.ent_nombre = tk.Entry(frame)
        self.ent_nombre.grid(row=0, column=3)

        tk.Label(frame, text="Email:").grid(row=1, column=0)
        self.ent_email = tk.Entry(frame)
        self.ent_email.grid(row=1, column=1)

        btn_guardar = tk.Button(frame, text="Guardar Cliente", command=self._guardar, bg="green", fg="white")
        btn_guardar.grid(row=1, column=3, pady=5)

    def _crear_tabla(self):
        self.tabla = ttk.Treeview(self.root, columns=("ID", "Nombre", "Email", "Tipo"), show='headings')
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Email", text="Email")
        self.tabla.heading("Tipo", text="Tipo")
        self.tabla.pack(fill="both", expand=True, padx=20, pady=10)

    def _guardar(self):
        try:
            # Creamos el objeto cliente (Validaciones automáticas por nuestra clase Cliente)
            nuevo = ClienteRegular(
                self.ent_id.get(), 
                self.ent_nombre.get(), 
                self.ent_email.get(), 
                "00000000" # Teléfono por defecto para demo
            )
            self.db.guardar_cliente(nuevo)
            messagebox.showinfo("Éxito", f"Cliente {nuevo.nombre} guardado correctamente.")
            self._cargar_datos()
            registrar_evento(f"Interfaz: Cliente {nuevo.id_cliente} agregado.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _cargar_datos(self):
        # Limpiar tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        # Cargar desde SQLite
        for row in self.db.obtener_todos():
            self.tabla.insert("", "end", values=(row[0], row[1], row[2], row[4]))

if __name__ == "__main__":
    root = tk.Tk()
    app = GICApp(root)
    root.mainloop()