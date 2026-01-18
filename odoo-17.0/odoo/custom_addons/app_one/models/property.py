from email.policy import default

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Property(models.Model):
    _name = 'property'
    name = fields.Char(required=True, default='kareem')
    description = fields.Text()
    postcode = fields.Char()
    date_available = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean(default=False)
    garden = fields.Boolean(default=False)
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West'),
    ])

    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')

    state =fields.Selection([
        ('draft','Draft'),
        ('pending','Pending'),
        ('sold','Sold'),

    ],default='draft')




    _sql_constraints = [
        ('unique_name', 'unique(name)', 'The name already exists!')
    ]

    @api.constrains('bedrooms')
    def _check_bedrooms_greater_zero(self):
        for i in self:
            if i.bedrooms < 1:
                raise ValidationError('Please enter a valid number of bedrooms!')


    def action_draft(self):
        for rec in self:
          print("inside action draft ")
          rec.state = 'draft'
          # rec.write({
          #     'state': 'draft',
          # })
    def action_pending(self):
        for rec in self:
          print("inside action pending  ")
          # rec.state = 'draft'
          rec.write({
              'state': 'pending',
          })
    def action_sold(self):
        for rec in self:
          print("inside action sold  ")
          # rec.state = 'draft'
          rec.write({
              'state': 'sold',
          })



#*********CRUD**************
    # @api.model_create_multi
    # def create(self, vals_list):
    #     res = super(Property,self).create(vals_list)
    #     #logic
    #     print("valid ")
    #     return res
    #
    # @api.model
    # def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
    #     res = super(Property, self). _search(domain, offset=0, limit=None, order=None, access_rights_uid=None)
    #     print("valid2 ")
    #     return (res)
    #
    #
    # def write(self, vals):
    #     res =super(Property,self).write(vals)
    #     print("valid3")
    #     return res
    #
    #
    # def unlink(self):
    #     res =super(Property,self).unlink()
    #     print("valid4")
    #     return res