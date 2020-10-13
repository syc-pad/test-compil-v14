from odoo import fields, models, api
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
	_name = 'product.template'
	_inherit = 'product.template'

    is_bio = fields.Char(string = 'Bio')
    is_returnable = fields.Char(string = 'Consigné')
