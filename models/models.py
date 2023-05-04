# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class testModul(models.Model):
    _name = 'material.material'
    _description = 'material.material'

    name = fields.Char('Material Name', required=True)
    code = fields.Char('Material Code', required=True)
    type = fields.Selection([
        ('Fabric', 'Fabric'),
        ('Jeans', 'Jeans'),
        ('Cotton', 'Cotton')
    ], required=True)
    price = fields.Integer(string='Buy Price', required=True)

    @api.model
    def create(self, vals):
        if vals['price'] < 100:
            raise ValidationError('Buy price tidak boleh kurang dari 100')
        result = super(testModul, self).create(vals)
        return result

    def write(self, vals):
        if vals['price'] < 100:
            raise ValidationError('Buy price tidak boleh kurang dari 100')
        result = super(testModul, self).write(vals)
        return result
