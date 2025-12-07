from  odoo import models,fields



class Propertys(models.Model):
    _name = 'propertys'

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_available = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),

    ])

