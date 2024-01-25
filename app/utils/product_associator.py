import csv
from app.clients.api_client import ApiClient


def read_csv_and_associate_products(vendor_id, csv_content):
    csv_rows = csv.DictReader(csv_content.splitlines())

    for row in csv_rows:
        product_data = {
            'barcode': row['barcode'],
            'category_ids': [row['category']],
            'sku': row['sku'],
            'price': float(row['price']),
            'active': row['active'].lower() == 'true',
            'maximum_sales_quantity': int(row['maximum_sales_quantity']),
            'sales_buffer': int(row['sales_buffer'])
        }

        response = ApiClient().associate_products(vendor_id, [product_data])

        handle_associate_response(response)


def handle_associate_response(response):
    if response.get('success', False):
        print(f"Producto asociado correctamente. Job ID: {response.get('job_id')}")
    else:
        print(f"Error al asociar producto. Detalles: {response}")