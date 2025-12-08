from odoo import models, fields


class Owner(models.Model):
    _name = 'owner'

    name = fields.Char(required=True)
    phone = fields.Char(required=True)
    address = fields.Char(required=True)
    property_ids = fields.One2many('property','owner_id')
