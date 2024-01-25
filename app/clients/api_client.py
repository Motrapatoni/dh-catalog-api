import requests
import logging
from urllib.parse import urljoin
from config.config import Config
import os


def handle_response(response, action):
    try:
        response.raise_for_status()  # Esto generará una excepción para códigos de error HTTP
        return response.json()
    except requests.exceptions.HTTPError as errh:
        logging.error(f'Error HTTP en la acción {action}: {errh}')
    except requests.exceptions.ConnectionError as errc:
        logging.error(f'Error de conexión en la acción {action}: {errc}')
    except requests.exceptions.Timeout as errt:
        logging.error(f'Timeout en la acción {action}: {errt}')
    except requests.exceptions.RequestException as err:
        logging.error(f'Otro error en la acción {action}: {err}')

    return None


def create_headers():
    return {
        'Accept': 'application/json',
        'Authorization': f'{ApiClient.PEDIDOSYA_TOKEN}',
        'Content-Type': 'application/json'
    }


class ApiClient:
    BASE_URL = Config.URL_BASE
    PEDIDOSYA_TOKEN = Config.PEDIDOSYA_TOKEN

    def associate_products(self, vendor_id, products):
        url = urljoin(self.BASE_URL, f'{vendor_id}/products')

        try:
            response = requests.post(url, json={"products": [products]}, headers=create_headers())
            return handle_response(response, 'associate_products')
        except Exception as e:
            logging.error(f'Error en la acción associate_products: {e}')
            return None

    def update_product(self, vendor_id):
        data = {
            'sku': 'SKUTESTMOI',
            'price': 100
        }
        url = urljoin(self.BASE_URL, f'{vendor_id}/product')
        response = requests.put(url, json=data, headers=create_headers())
        return handle_response(response, 'update_product')

    def deactivate_product(self, vendor_id):
        data = {
            'sku': 'SKUTESTMOI',
            'active': False
        }
        url = urljoin(self.BASE_URL, f'{vendor_id}/product')
        response = requests.put(url, json=data, headers=create_headers())
        return handle_response(response, 'deactivate_product')

    def update_products_bulk(self, vendor_id, products):
        url = urljoin(self.BASE_URL, f'{vendor_id}/products-bulk')
        response = requests.put(url, json=products, headers=create_headers())
        return handle_response(response, 'update_products_bulk')

    def download_csv(self, download_url):
        response = requests.get(download_url,
                                headers={'Accept': 'text/csv', 'Authorization': f'{self.PEDIDOSYA_TOKEN}'})
        return response.content.decode('utf-8')

    def export_catalog(self, vendor_id):
        url = urljoin(self.BASE_URL, f'{vendor_id}/products/export')
        headers = {
            'Accept': 'application/json',
            'Authorization': f'{self.PEDIDOSYA_TOKEN}',
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers)
        data = handle_response(response, 'export_catalog')
        return handle_response(response, 'export_catalog')

