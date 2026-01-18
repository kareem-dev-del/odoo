from odoo import models, fields

class Car(models.Model):
    _name = "car.rental"
    _description = "Car Rental"  # مهم لتجنب Warning
    name = fields.Char("Car Name", required=True)
    price = fields.Float("Price Per Day")
