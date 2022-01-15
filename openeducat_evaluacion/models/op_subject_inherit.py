from odoo import fields, models, api


class Course(models.Model):
    _inherit = 'op.subject'

    nota = fields.Float(string=u'Nota', required=False)

class Course(models.Model):
    _inherit = 'op.exam.attendees'

    evaluacion = fields.Float(string=u'Evaluación', required=False)
