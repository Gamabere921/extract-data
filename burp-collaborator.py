from flask import Flask, request
import logging

app = Flask(__name__)

# Configurar logging para capturar todas las solicitudes y guardarlas en un archivo
logging.basicConfig(
    filename='captured_requests.log',  # Archivo donde se guardarán los logs
    level=logging.INFO,                # Nivel de logging (INFO para capturar detalles de las solicitudes)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato de los logs
)

# También configurar logging para mostrar en la consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
app.logger.addHandler(console_handler)

# Aceptar tanto solicitudes GET como POST
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def capture_request(path):
    # Capturar la IP de origen
    ip_address = request.remote_addr
    # Capturar la URL solicitada
    request_url = request.url
    # Capturar las cabeceras HTTP
    request_headers = request.headers

    # Capturar el cuerpo de la solicitud
    if request.method == 'POST':
        # Si la solicitud es POST, intentamos obtener datos del formulario
        request_body = request.form  # Para datos form-urlencoded
    else:
        request_body = {}

    # Registrar la información capturada en consola
    print(f"Request from {ip_address}")
    print(f"URL: {request_url}")
    print(f"Headers: {request_headers}")
    print(f"Body: {request_body}")

    # Registrar la información capturada en el archivo de logs
    logging.info(f"Request from {ip_address}")
    logging.info(f"URL: {request_url}")
    logging.info(f"Headers: {request_headers}")
    logging.info(f"Body: {request_body}")

    # Responder algo al cliente
    return "Request captured!", 200

if __name__ == '__main__':
    # Asegúrate de habilitar el modo debug para ver más información en consola
    app.run(host='0.0.0.0', port=80, debug=True)
