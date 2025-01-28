import os
from dotenv import load_dotenv

load_dotenv("../.env")

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_MAIL = os.environ.get('EMAIL_HOST_USER')

print(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, DEFAULT_FROM_MAIL)