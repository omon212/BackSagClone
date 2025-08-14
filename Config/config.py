import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv("DEBUG")
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')