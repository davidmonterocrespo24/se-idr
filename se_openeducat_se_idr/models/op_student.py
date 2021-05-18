#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class OpStudent(models.Model):
    _inherit = "op.student"

    rfc = fields.Float(string='RFC', digits=(12, 2))
    curp = fields.Float(string='CURP', digits=(12, 2))
    registration_date = fields.Date('Registration date', readonly=True, 
                                    default=fields.Date.today())
    institutional_email = fields.Char('Institutional email', size=256)
    enrollment_number = fields.Integer(string='Enrollment number')

    @api.constrains('enrollment_number')
    def check_number_digits(self):
        for record in self:
            if record.enrollment_number and len(str(abs(record.enrollment_number)))< 11:
                raise ValidationError("Enrollment number can't be less than 11")
    
            
    