import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    PEDIDOSYA_TOKEN = os.environ.get('PEDIDOSYA_TOKEN')
    URL_BASE = os.environ.get('URL_BASE_CATALOG')
