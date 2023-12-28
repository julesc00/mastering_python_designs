import time
import requests
from pprint import pprint


now = time.time()

def get_sendgrid_response_headers(api_key):
    """Obtiene los encabezados de respuesta de una solicitud a la API de SendGrid."""

    # Endpoint de la API de SendGrid para la versión v3
    url = 'https://api.sendgrid.com/v3/user/profile'

    # Encabezados para la solicitud, incluyendo la autenticación con la API key
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    # Realiza la solicitud GET
    response = requests.get(url, headers=headers)

    # Retorna los encabezados de respuesta
    return response.headers


api_key = "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"

# Uso de la función
# Reemplaza 'your_api_key' con tu API key real de SendGrid
sendgrid_headers = get_sendgrid_response_headers(api_key)
pprint(sendgrid_headers)
print(sendgrid_headers.get("X-Ratelimit-Limit"))
print(sendgrid_headers.get("X-Ratelimit-Remaining"))
