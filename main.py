import tkinter as tk
from gui.app import GICApp
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    try:
        root = tk.Tk()
        app = GICApp(root)
        root.mainloop()
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")

if __name__ == "__main__":
    main()