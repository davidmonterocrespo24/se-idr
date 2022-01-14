from odoo import fields, models, api


class Course(models.Model):
    _inherit = 'op.subject'

    # calificacion = fields.Float(string=u'Calificación', required=False)
    pass

class Course(models.Model):
    _inherit = 'op.exam.attendees'

    evaluacion = fields.Float(string=u'Evaluación', required=False)
