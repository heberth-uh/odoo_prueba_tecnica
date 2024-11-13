import requests
import json

from odoo import models, fields
from odoo.exceptions import ValidationError
import logging

_logger = logging.getLogger(__name__)

class SaleOrderApi(models.Model):
    _inherit = 'sale.order'

    def dhl_tracking(self):
        api_url = "https://api-eu.dhl.com/track/shipments"
        api_key = 'm7KogdsWTlQG3xucKQqo9YD13QVSQJhy'
        auth = requests.auth.HTTPBasicAuth(api_key, '')
        payload = {
            'trackingNumber': '7777777770'
            }
        headers = {
            'DHL-API-Key': api_key
        }

        response = requests.get(
            api_url,
            payload,
            headers=headers,
            auth=auth
        )

        data = response.json()
        _logger.info(f'data: {data}')

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                        'title': 'Seguimiento DHL',
                        'message': 'Se registró el estatus de envío de DHL en el log',
                        'sticky': False,
                    }
            }
