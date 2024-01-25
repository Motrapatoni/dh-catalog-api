from app.utils.api_utils import ApiResponse
from app.clients.api_client import ApiClient


class UpdateProcessor:
    def __init__(self):
        self.api_client = ApiClient()

    def update_product(self, vendor_id):
        response = self.api_client.update_product(vendor_id)
        return ApiResponse.success(response)

    def deactivate_product(self, vendor_id):
        response = self.api_client.deactivate_product(vendor_id)
        return ApiResponse.success(response)

    def update_products_bulk(self, vendor_id, data):
        response = self.api_client.update_products_bulk(vendor_id, data)
        return ApiResponse.success(response)
