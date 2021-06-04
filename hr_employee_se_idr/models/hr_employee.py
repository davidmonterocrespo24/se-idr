# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    rfc = fields.Char(string='RFC')
    curp = fields.Char(string='CURP')
