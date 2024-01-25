from app.utils.api_utils import ApiResponse
from app.clients.api_client import ApiClient


class ProductProcessor:
    def __init__(self):
        self.api_client = ApiClient()

    def process_products(self, vendor_id, data):
        job_id = self.api_client.associate_products(vendor_id, data)
        return ApiResponse.success(job_id)