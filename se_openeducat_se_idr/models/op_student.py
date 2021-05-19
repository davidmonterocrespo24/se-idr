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
    enrollment_number = fields.Char(string='Número de Matrícula', size=10)

    @api.constrains('enrollment_number')
    def check_number_digits(self):
        for record in self:
            if not record.enrollment_number.isdigit():
                raise ValidationError("Número de Matrícula solo puede contener números")
            if len(record.enrollment_number) < 10:
                raise ValidationError("Número de Matrícula no puede contener menos de 10 números")
    
            
    