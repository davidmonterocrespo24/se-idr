from odoo import fields, models, api


class Estudiante(models.Model):
    _inherit = 'op.student'

    name = fields.Char()

    @api.onchange('course_id')
    def autocompletar_asignaturas(self):
        pass
