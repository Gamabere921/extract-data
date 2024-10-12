from flask import Flask, request, render_template, redirect, url_for
from db import get_db_connection
import sqlite3
from lxml import etree  # Cambia a lxml
import os

# Establecer la ruta correcta para las plantillas
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Página de inicio de sesión (vulnerable a inyección SQL)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Consulta SQL vulnerable a inyección
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Aquí está la vulnerabilidad de inyección SQL
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)

        user = cursor.fetchone()
        
        if user:
            return f"Bienvenido, {user[1]}!"  # Asumiendo que el username es el segundo campo
        else:
            return "Usuario o contraseña incorrectos."

    return render_template('login.html')

# Endpoint vulnerable a XXE
@app.route('/xxe', methods=['POST'])
def xxe():
    xml_data = request.data
    print("XML recibido:", xml_data)  # <-- Imprime el XML recibido
    try:
        parser = etree.XMLParser(resolve_entities=True)
        root = etree.fromstring(xml_data, parser)
        payload = root.find('payload').text
        return f"Payload recibido: {payload}"
    except etree.XMLSyntaxError as e:
        return f"Error al parsear el XML: {e}"
    except Exception as e:
        return f"Error inesperado: {e}"


if __name__ == '__main__':
    app.run(debug=True)
