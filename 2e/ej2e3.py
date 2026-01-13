"""
Enunciado:
Desarrolla una aplicación web con Flask que procese diferentes tipos MIME (Multipurpose Internet Mail Extensions)
recibidos en solicitudes HTTP. Esta aplicación te permitirá entender cómo recibir y procesar
diferentes formatos de datos enviados por los clientes.

Los tipos MIME son fundamentales en el desarrollo web ya que indican cómo interpretar los datos
recibidos en las solicitudes HTTP. Una API robusta debe poder manejar diversos formatos de entrada.

Tu aplicación debe implementar los siguientes endpoints:

1. `POST /text`: Recibe un texto plano con el tipo MIME `text/plain` y lo devuelve en la respuesta.
   - Ejemplo de uso: Procesar mensajes simples o logs enviados por el cliente.

2. `POST /html`: Recibe un fragmento HTML con el tipo MIME `text/html` y lo devuelve en la respuesta.
   - Ejemplo de uso: Recibir contenido HTML para almacenar o procesar.

3. `POST /json`: Recibe un objeto JSON con el tipo MIME `application/json` y lo devuelve en la respuesta.
   - Ejemplo de uso: Procesar datos estructurados en APIs RESTful.

4. `POST /xml`: Recibe un documento XML con el tipo MIME `application/xml` y lo devuelve en la respuesta.
   - Ejemplo de uso: Procesar configuraciones o datos estructurados en formato XML.

5. `POST /image`: Recibe una imagen con el tipo MIME `image/png` o `image/jpeg` y la guarda en el servidor.
   - Ejemplo de uso: Subir imágenes para un perfil de usuario o una galería.

6. `POST /binary`: Recibe datos binarios con el tipo MIME `application/octet-stream` y confirma su recepción.
   - Ejemplo de uso: Recibir archivos genéricos como PDFs o archivos comprimidos.

Tu tarea es completar la implementación de la función create_app() y de los endpoints solicitados,
asegurándote de identificar correctamente el tipo MIME de cada solicitud y procesarla adecuadamente.

Esta actividad te enseñará cómo recibir y manejar diferentes tipos de datos en solicitudes HTTP,
una habilidad esencial para desarrollar APIs web que interactúan con diversos clientes.
"""

from flask import Flask, jsonify, request, Response, make_response
import os

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    # Crear un directorio para guardar archivos subidos si no existe
    uploads_dir = os.path.join(app.instance_path, 'uploads')
    os.makedirs(uploads_dir, exist_ok=True)

    @app.route('/text', methods=['POST'])
    def post_text():
        """
        Recibe un texto plano con el tipo MIME `text/plain` y lo devuelve en la respuesta.
        """
        # Implementa este endpoint:
        # 1. Verifica que el Content-Type sea text/plain
        # 2. Lee el contenido de la solicitud usando request.data
        # 3. Devuelve el mismo texto con Content-Type text/plain
        if request.content_type and 'text/plain' in request.content_type:
            response = make_response(request.data)
            response.headers['Content-Type'] = 'text/plain'
            return response
        return Response("Invalid content type", status=400)

    @app.route('/html', methods=['POST'])
    def post_html():
        """
        Recibe un fragmento HTML con el tipo MIME `text/html` y lo devuelve en la respuesta.
        """
        # Implementa este endpoint:
        # 1. Verifica que el Content-Type sea text/html
        # 2. Lee el contenido de la solicitud
        # 3. Devuelve el mismo HTML con Content-Type text/html
        if request.content_type and 'text/html' in request.content_type:
            response = make_response(request.data)
            response.headers['Content-Type'] = 'text/html'
            return response
        return Response("Invalid content type", status=400)

    @app.route('/json', methods=['POST'])
    def post_json():
        """
        Recibe un objeto JSON con el tipo MIME `application/json` y lo devuelve en la respuesta.
        """
        # Implementa este endpoint:
        # 1. Accede al contenido JSON usando request.get_json()
        # 2. Devuelve el mismo objeto JSON usando jsonify()
        data = request.get_json()
        return jsonify(data)

    @app.route('/xml', methods=['POST'])
    def post_xml():
        """
        Recibe un documento XML con el tipo MIME `application/xml` y lo devuelve en la respuesta.
        """
        # Implementa este endpoint:
        # 1. Verifica que el Content-Type sea application/xml
        # 2. Lee el contenido XML de la solicitud
        # 3. Devuelve el mismo XML con Content-Type application/xml
        if request.content_type and 'application/xml' in request.content_type:
            response = make_response(request.data)
            response.headers['Content-Type'] = 'application/xml'
            return response
        return Response("Invalid content type", status=400)

    @app.route('/image', methods=['POST'])
    def post_image():
        """
        Recibe una imagen con el tipo MIME `image/png` o `image/jpeg` y la guarda en el servidor.
        """
        # Implementa este endpoint:
        # 1. Verifica que el Content-Type sea image/png o image/jpeg
        # 2. Lee los datos binarios de la imagen
        # 3. Guarda la imagen en el directorio 'uploads' con un nombre único
        # 4. Devuelve una confirmación con el nombre del archivo guardado
        if request.content_type and ('image/png' in request.content_type or 'image/jpeg' in request.content_type):
            archivo = f"image_{os.urandom(4).hex()}.{'png' if 'png' in request.content_type else 'jpg'}"
            filepath = os.path.join(uploads_dir, archivo)
            with open(filepath, 'wb') as f:
                f.write(request.data)
            return jsonify({"archivo": archivo, "mensaje": "Imagen guardada"}), 200
        return jsonify({"error": "Invalid content type"}), 400

    @app.route('/binary', methods=['POST'])
    def post_binary():
        """
        Recibe datos binarios con el tipo MIME `application/octet-stream` y confirma su recepción.
        """
        # Implementa este endpoint:
        # 1. Verifica que el Content-Type sea application/octet-stream
        # 2. Lee los datos binarios de la solicitud
        # 3. Guarda los datos en un archivo o simplemente verifica su tamaño
        # 4. Devuelve una confirmación con información sobre los datos recibidos
        if request.content_type and 'application/octet-stream' in request.content_type:
            data = request.data
            archivo = f"binary_{os.urandom(4).hex()}.bin"
            filepath = os.path.join(uploads_dir, archivo)
            with open(filepath, 'wb') as f:
                f.write(data)
            return jsonify({"archivo": archivo, "tamaño": len(data), "mensaje": "Datos guardados"}), 200
        return jsonify({"error": "Invalid content type"}), 400

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
