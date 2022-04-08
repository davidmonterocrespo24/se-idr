# -*- coding: utf-8 -*-

from odoo import models, fields, api

class prueba(models.Model):
    _inherit = 'op.student'

    edad = fields.Integer(string='Edad', required=False)
    observaciones = fields.Text(string="Observaciones", required=False)