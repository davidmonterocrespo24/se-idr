#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class OpStudent(models.Model):
    _inherit = "op.student"

    rfc = fields.Char(string='RFC')
    curp = fields.Char(string='CURP')
    registration_date = fields.Date('Fecha de registro', readonly=True,
                                    default=fields.Date.today())
    institutional_email = fields.Char('Email Institucional', size=256)
    enrollment_number = fields.Integer(string='Numero de Matrícula')

    @api.constrains('enrollment_number')
    def check_number_digits(self):
        for record in self:
            if record.enrollment_number and len(str(abs(record.enrollment_number)))< 11:
                raise ValidationError("Enrollment number can't be less than 10")
    
            
    