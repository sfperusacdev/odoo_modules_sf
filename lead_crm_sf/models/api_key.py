from odoo import models, fields
import secrets

class ApiKey(models.Model):
    _name = 'api.key'
    _description = 'API Keys'

    name = fields.Char(required=True)
    key = fields.Char(default=lambda self: secrets.token_hex(32), readonly=True)
