import logging
import os

# Aseguramos que la carpeta logs exista
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename='logs/sistema.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def registrar_evento(mensaje):
    logging.info(mensaje)

def registrar_error(mensaje):
    logging.error(mensaje)