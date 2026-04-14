from core.tipos_clientes import ClientePremium, ClienteCorporativo
from database.conexion import DBManager
import tkinter as tk
from gui.app import GICApp

def ejecutar_demo():
    try:
        # Instanciación de clientes 
        c1 = ClientePremium(1, "Carolina Páez", "carolina@tech.com", "123456789", 20)
        c2 = ClienteCorporativo(2, "Solution Corp", "info@solution.com", "987654321", "SolutionTech SA")

        print("--- Listado de Clientes ---")
        print(c1)
        print(c2)

    except ValueError as e: # Manejo de errores 
        print(f"Error de validación: {e}")

if __name__ == "__main__":
    ejecutar_demo()

def ejecutar_paso_2():
    db = DBManager()
    
    # Creamos un cliente de prueba
    nuevo_cliente = ClientePremium(101, "Andrónico Luksic", "andronico@tech.com", "555123456", 15)
    
    # Guardamos en SQLite
    db.guardar_cliente(nuevo_cliente)
    
    # Consultamos
    print("\n--- Clientes en Base de Datos ---")
    for registro in db.obtener_todos():
        print(registro)

if __name__ == "__main__":
    ejecutar_paso_2()

def main():
    root = tk.Tk()
    app = GICApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()