from flask import Flask, request, render_template
from app.processors.product_processor import ProductProcessor
from app.processors.update_product import UpdateProcessor
from app.utils.csv_handler import CsvHandler
from app.utils.product_associator import read_csv_and_associate_products
from app.utils.api_utils import ApiResponse
from app.clients.api_client import ApiClient
import json
from config.config import Config
import logging


logging.basicConfig(filename='app.log', level=logging.ERROR)

app = Flask(__name__)
app.config.from_object(Config)
WEBHOOK_SECRET_KEY = Config.SECRET_KEY
VENDOR_ID = '364124'


# TODO localmente se levanta en: http://127.0.0.1:5000/

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/v1/add_products', methods=["GET", "POST"])
def add_products():
    # data = request.get_json()    # <-- activar si recibimos el producto por postman

    try:
        json_file_path = 'app/resources/product_data.json'

        with open(json_file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                logging.error(f"Error decoding JSON: {e}")
                return ApiResponse.error("Error decoding JSON"), 500

        response = ProductProcessor().process_products(VENDOR_ID, data)
        return ApiResponse.success(response), 200

    except Exception as e:
        logging.error(e)
        return ApiResponse.error(str(e)), 500


# TODO descomentar y aplicar logica de carga recorriendo un csv
# @app.route('/v1/add_products_csv', methods=["POST"])
# def add_products_from_csv():
#     data = request.get_json()
#
#     try:
#         csv_path = data.get('csv_path')
#         with open(csv_path, 'r') as csv_file:
#             csv_content = csv_file.read()
#             read_csv_and_associate_products(VENDOR_ID, csv_content)
#         return ApiResponse.success("Asociación desde CSV completada"), 200
#
#     except Exception as e:
#         return ApiResponse.error(str(e)), 500


@app.route('/v1/actualizar_producto', methods=['PUT'])
def update_product():
    try:
        response = UpdateProcessor().update_product(VENDOR_ID)
        return ApiResponse.success(response), 200

    except Exception as e:
        return ApiResponse.error(str(e)), 500


@app.route('/v1/desactivar_producto', methods=['PUT'])
def deactivate_product():
    try:
        response = UpdateProcessor().deactivate_product(VENDOR_ID)
        return ApiResponse.success(response), 200

    except Exception as e:
        return ApiResponse.error(str(e)), 500


@app.route('/v1/actualizar_productos_lote', methods=['PUT'])
def update_products_bulk():
    try:
        json_file_path = 'app/resources/bulk_updates.json'

        with open(json_file_path, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                logging.error(f"Error decoding JSON: {e}")
                return ApiResponse.error("Error decoding JSON"), 500

        response = UpdateProcessor().update_products_bulk(VENDOR_ID, data)
        return ApiResponse.success(response), 200

    except Exception as e:
        logging.error(e)
        return ApiResponse.error(str(e)), 500


@app.route('/v1/export_catalog', methods=['GET'])
def export_catalog():
    try:
        ApiClient().export_catalog(VENDOR_ID)
        return ApiResponse.success("Exportación del catálogo solicitado"), 200
    except Exception as e:
        logging.error(f'Error al exportar el catálogo: {e}')
        return ApiResponse.error(str(e)), 500


@app.route('/webhook-pos/tech-test', methods=['POST'])
def webhook_handler():
    try:
        data = request.json
        process_webhook_notification(data)
        return 'Webhook received successfully', 200

    except Exception as e:
        return ApiResponse.error(str(e)), 500


def process_webhook_notification(notification_data):
    try:
        job_id = notification_data.get('job_id')
        download_url = notification_data.get('download_url')

        csv_content = ApiClient().download_csv(download_url)

        handle_csv_content(job_id, csv_content)

    except Exception as e:
        logging.error(f'Error en el manejo de la notificación del webhook. Detalles: {str(e)}')


def handle_csv_content(job_id, csv_content):
    csv_handler = CsvHandler(job_id=job_id, csv_content=csv_content)
    csv_handler.handle_full_catalog_csv()
    csv_handler.handle_notification_csv()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

