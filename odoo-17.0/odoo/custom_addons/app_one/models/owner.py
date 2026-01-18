from odoo import models, fields


class Owner(models.Model):
    _name = 'owner'

    name = fields.Char()
    phone = fields.Char()
    address = fields.Char()
    property_ids = fields.One2many('property','owner_id')
