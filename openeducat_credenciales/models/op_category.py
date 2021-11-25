# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CategoryInherit(models.Model):
    _inherit = 'op.category'

    clave_carrera = fields.Char(string='Clave Carrera', required=False)
    imagen_qr = fields.Binary(string="Imagen Qr de la carrera", )