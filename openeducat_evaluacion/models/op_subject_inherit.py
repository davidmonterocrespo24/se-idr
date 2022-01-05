from odoo import fields, models, api


class Course(models.Model):
    _inherit = 'op.subject'

    calificacion = fields.Float(string=u'Calificación', required=False)
