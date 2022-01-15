from odoo import fields, models, api


class OpstudentInherit(models.Model):
    _name = 'op.subject'

    nota = fields.Float(string='Nota', required=False)