# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api
from odoo.tools.translate import _
from odoo.exceptions import UserError, ValidationError

import requests



class account_payment(models.Model):
    _inherit = 'account.payment'


    comprobantes = fields.Many2many("ir.attachment", string="Comprobante")
    comprobantes_imagen = fields.Image(string="Comprobante(Imagen)")
